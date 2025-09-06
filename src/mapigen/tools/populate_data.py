from __future__ import annotations
import argparse
import logging
import multiprocessing as mp
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

import msgspec

from mapigen.cache.ranking import get_rank
from mapigen.metadata.fetcher import fetch_specs_concurrently
from mapigen.services.registry_service import RegistryService
from mapigen.tools.pipeline import run_processing_pipeline
from mapigen.tools.reporting import generate_auth_notice, generate_performance_report
from mapigen.utils.compression_utils import compress_with_zstd
from mapigen.utils.path_utils import get_service_data_path, get_data_dir

FORMAT_VERSION = 3

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# Define paths
ROOT_DIR = Path(__file__).resolve().parent.parent.parent.parent
SRC_DIR = ROOT_DIR / "src" / "mapigen"
DATA_DIR = get_data_dir()
REGISTRY_DIR = SRC_DIR / "registry"
CUSTOM_SOURCES_PATH = REGISTRY_DIR / "custom_sources.json"
GITHUB_SOURCES_PATH = REGISTRY_DIR / "github_sources.yaml"
OVERRIDES_PATH = REGISTRY_DIR / "overrides.json"
SERVICES_JSON_PATH = SRC_DIR / "services.json"

def setup_arg_parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Fetch and process API specifications.")
    parser.add_argument("--batch-size", type=int, default=None, help="Number of specs to process in a batch. Disables dynamic batching.")
    parser.add_argument("--download-workers", type=int, default=25, help="Concurrent download workers.")
    parser.add_argument("--process-workers", type=int, default=mp.cpu_count(), help="Parallel processing workers.")
    parser.add_argument("--skip-download", action="store_true", help="Skip download, use existing specs.")
    parser.add_argument("--force-reprocess", action="store_true", help="Force reprocessing of all specs.")
    parser.add_argument("--cache", action="store_true", help="Use cached downloads but force reprocessing.")
    parser.add_argument("--no-compress-utilize", action="store_true", help="Do not compress final utilize.json files.")
    parser.add_argument("--no-compress-original", action="store_true", help="Do not compress original downloaded specs, for debugging.")
    parser.add_argument("--memory-threshold", type=float, default=2048.0, help="Memory threshold in MB to trigger garbage collection.")
    return parser.parse_args()

def load_configuration() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Loads configuration from the new YAML source files."""
    all_sources: list[dict[str, Any]] = []

    source_files = {
        "github": REGISTRY_DIR / "github_sources.yaml",
        "custom": REGISTRY_DIR / "custom_sources.yaml",
    }

    for source, path in source_files.items():
        if path.exists():
            try:
                entries = msgspec.yaml.decode(path.read_bytes(), type=List[Dict[str, str]])
                for entry in entries:
                    entry["source"] = source
                all_sources.extend(entries)
            except (msgspec.ValidationError, TypeError) as e:
                logging.error(f"Failed to parse {path}: {e}")

    overrides: dict[str, Any] = {}
    if OVERRIDES_PATH.exists():
        overrides = msgspec.json.decode(OVERRIDES_PATH.read_bytes())
    return all_sources, overrides

def write_metadata(result: dict[str, Any], overrides: dict[str, Any]):
    provider = result["provider"]
    api = result["api"]
    source = result["source"]
    service_data_dir = get_service_data_path(provider, api, source)
    service_data_dir.mkdir(parents=True, exist_ok=True)
    metadata_yml_path = service_data_dir / "metadata.yml"
    first_accessed_time = datetime.now(timezone.utc).isoformat()
    if metadata_yml_path.exists():
        try:
            existing_metadata = msgspec.yaml.decode(metadata_yml_path.read_text(), type=Dict[str, Any])
            first_accessed_time = existing_metadata.get("first_accessed", first_accessed_time)
        except (IOError, msgspec.ValidationError, TypeError):
            pass
    final_auth_info = result["auth_info"].copy()
    if api in overrides and "auth" in overrides[api]:
        final_auth_info.update(overrides[api]["auth"])
    metadata_content = {
        "format_version": FORMAT_VERSION, "first_accessed": first_accessed_time,
        "updated_at": datetime.now(timezone.utc).isoformat(),
        "api_reference": result["url"], "status": result["status"],
        "operation_count": result.get("processed_op_count", 0),
        "reusable_parameter_count": result.get("reusable_param_count", 0),
        "coverage": result.get("coverage", "N/A"),
        "auth_types": final_auth_info["auth_types"],
        "primary_auth": final_auth_info["primary_auth"],
        "popularity_rank": get_rank(api),
    }
    metadata_yml_path.write_bytes(msgspec.yaml.encode(metadata_content))

def handle_utilize_compression(utilize_path: Path, args: argparse.Namespace):
    if not args.no_compress_utilize:
        compressed_data = compress_with_zstd(utilize_path.read_bytes())
        compressed_path = utilize_path.with_suffix(".json.zst")
        compressed_path.write_bytes(compressed_data)
        utilize_path.unlink()

def main():
    args = setup_arg_parser()
    overall_start_time = time.perf_counter()
    all_sources, overrides = load_configuration()
    if not all_sources:
        logging.warning("No sources found. Exiting.")
        return

    if args.cache:
        args.skip_download = True
        args.force_reprocess = True

    # --- Download Phase ---
    download_results: List[Dict[str, Any]] = []
    if not args.skip_download:
        download_batch_size = 50
        download_results = fetch_specs_concurrently(all_sources, download_batch_size, args)
    
    # --- Processing Phase ---
    services_to_process = all_sources
    if not args.force_reprocess:
        services_to_process = [
            s for s in all_sources 
            if not (get_service_data_path(s['provider'], s['api'], s['source']) / f"{s['api']}.utilize.json.zst").exists() and 
               not (get_service_data_path(s['provider'], s['api'], s['source']) / f"{s['api']}.utilize.json").exists()
        ]

    if not services_to_process:
        logging.info("All services are already processed. Exiting.")
        return

    for entry in services_to_process:
        try:
            size_path = get_service_data_path(entry['provider'], entry['api'], entry['source']) / f"{entry['api']}.openapi.json.zst"
            entry['size'] = size_path.stat().st_size if size_path.exists() else 0
        except FileNotFoundError:
            logging.warning(f"Could not find compressed spec for {entry['api']}. It will be skipped during processing.")
            entry['size'] = 0

    processing_results = run_processing_pipeline(services_to_process, args)

    # --- Aggregation & Reporting Phase ---
    logging.info("Aggregating results...")
    services_requiring_override_fix: list[str] = []
    services_with_active_override: list[str] = []

    for result in processing_results:
        if result["status"] == "success":
            write_metadata(result, overrides)
            
            handle_utilize_compression(result["utilize_path"], args)
            
            auth_info = result.get("auth_info", {})
            if auth_info and not auth_info.get("auth_types"):
                service_name = result["api"]
                if service_name in overrides and "auth" in overrides[service_name]:
                    services_with_active_override.append(service_name)
                else:
                    services_requiring_override_fix.append(service_name)

    registry_service = RegistryService(data_dir=DATA_DIR, registry_path=SERVICES_JSON_PATH)
    service_registry = registry_service.build_registry()
    registry_service.save_registry(service_registry)

    generate_auth_notice(services_requiring_override_fix, services_with_active_override)
    total_duration = time.perf_counter() - overall_start_time
    generate_performance_report(download_results, processing_results, total_duration)

    logging.info("Data population process finished.")

if __name__ == "__main__":
    main()