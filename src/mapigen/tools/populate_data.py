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
from mapigen.tools.pipeline import run_processing_pipeline
from mapigen.tools.reporting import generate_auth_notice, generate_performance_report
from mapigen.utils.compression_utils import compress_with_zstd

FORMAT_VERSION = 3

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# Define paths
ROOT_DIR = Path(__file__).resolve().parent.parent.parent.parent
SRC_DIR = ROOT_DIR / "src" / "mapigen"
DATA_DIR = SRC_DIR / "data"
REGISTRY_DIR = SRC_DIR / "registry"
CUSTOM_SOURCES_PATH = REGISTRY_DIR / "custom_sources.json"
GITHUB_SOURCES_PATH = REGISTRY_DIR / "github_sources.json"
OVERRIDES_PATH = REGISTRY_DIR / "overrides.json"
SERVICES_JSON_PATH = SRC_DIR / "services.json"

def setup_arg_parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Fetch and process API specifications.")
    parser.add_argument("--batch-size", type=int, default=None, help="Number of specs to process in a batch. Disables dynamic batching.")
    parser.add_argument("--download-workers", type=int, default=25, help="Concurrent download workers.")
    parser.add_argument("--process-workers", type=int, default=mp.cpu_count(), help="Parallel processing workers.")
    parser.add_argument("--skip-download", action="store_true", help="Skip download, use existing specs.")
    parser.add_argument("--force-reprocess", action="store_true", help="Force reprocessing of all specs.")
    parser.add_argument("--no-compress-utilize", action="store_true", help="Do not compress final utilize.json files.")
    parser.add_argument("--memory-threshold", type=float, default=2048.0, help="Memory threshold in MB to trigger garbage collection.")
    return parser.parse_args()

def load_configuration() -> tuple[dict[str, Any], dict[str, Any]]:
    all_sources: dict[str, str] = {}
    json_decoder = msgspec.json.Decoder()
    if CUSTOM_SOURCES_PATH.exists():
        all_sources.update(json_decoder.decode(CUSTOM_SOURCES_PATH.read_bytes()))
    if GITHUB_SOURCES_PATH.exists():
        all_sources.update(json_decoder.decode(GITHUB_SOURCES_PATH.read_bytes()))
    overrides: dict[str, Any] = {}
    if OVERRIDES_PATH.exists():
        overrides = json_decoder.decode(OVERRIDES_PATH.read_bytes())
    return all_sources, overrides

def write_metadata(service_name: str, result: dict[str, Any], overrides: dict[str, Any]):
    service_data_dir = DATA_DIR / service_name
    metadata_yml_path = service_data_dir / "metadata.yml"
    first_accessed_time = datetime.now(timezone.utc).isoformat()
    if metadata_yml_path.exists():
        try:
            existing_metadata = msgspec.yaml.decode(metadata_yml_path.read_text())
            first_accessed_time = existing_metadata.get("first_accessed", first_accessed_time)
        except (IOError, msgspec.ValidationError):
            pass
    final_auth_info = result["auth_info"].copy()
    if service_name in overrides and "auth" in overrides[service_name]:
        final_auth_info.update(overrides[service_name]["auth"])
    metadata_content = {
        "format_version": FORMAT_VERSION, "first_accessed": first_accessed_time,
        "updated_at": datetime.now(timezone.utc).isoformat(),
        "api_reference": result["url"], "status": result["status"],
        "operation_count": result.get("processed_op_count", 0),
        "reusable_parameter_count": result.get("reusable_param_count", 0),
        "coverage": result.get("coverage", "N/A"),
        "auth_types": final_auth_info["auth_types"],
        "primary_auth": final_auth_info["primary_auth"],
        "popularity_rank": get_rank(service_name),
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

    # --- Download Phase ---
    download_results: List[Dict[str, Any]] = []
    if not args.skip_download:
        download_batch_size = 50
        download_results = fetch_specs_concurrently(all_sources, download_batch_size, args.download_workers)
    
    # --- Processing Phase ---
    services_to_process_tuples = list(all_sources.items())
    if not args.force_reprocess:
        services_to_process_tuples = [(name, url) for name, url in services_to_process_tuples if not (DATA_DIR / name / f"{name}.utilize.json.zst").exists() and not (DATA_DIR / name / f"{name}.utilize.json").exists()]

    if not services_to_process_tuples:
        logging.info("All services are already processed. Exiting.")
        return

    services_to_process: List[Dict[str, Any]] = []
    for name, url in services_to_process_tuples:
        try:
            size = (DATA_DIR / name / f"{name}.openapi.json.zst").stat().st_size
            services_to_process.append({"name": name, "url": url, "size": size})
        except FileNotFoundError:
            logging.warning(f"Could not find compressed spec for {name}. It will be skipped during processing.")
            services_to_process.append({"name": name, "url": url, "size": 0})

    processing_results = run_processing_pipeline(services_to_process, args)

    # --- Aggregation & Reporting Phase ---
    logging.info("Aggregating results...")
    service_registry: Dict[str, Any] = {}
    services_requiring_override_fix: list[str] = []
    services_with_active_override: list[str] = []

    for result in processing_results:
        if result["status"] == "success":
            service_name = result["service_name"]
            write_metadata(service_name, result, overrides)
            handle_utilize_compression(result["utilize_path"], args)
            
            auth_info = result.get("auth_info", {})
            if auth_info and not auth_info.get("auth_types"):
                if service_name in overrides and "auth" in overrides[service_name]:
                    services_with_active_override.append(service_name)
                else:
                    services_requiring_override_fix.append(service_name)

    for service_dir in DATA_DIR.iterdir():
        if service_dir.is_dir() and (service_dir / "metadata.yml").exists():
            metadata = msgspec.yaml.decode((service_dir / "metadata.yml").read_text())
            service_registry[service_dir.name] = {
                "path": f"data/{service_dir.name}",
                "operation_count": metadata.get("operation_count", 0),
                "auth_types": metadata.get("auth_types", []),
                "primary_auth": metadata.get("primary_auth", "none"),
                "popularity_rank": metadata.get("popularity_rank", 999),
            }

    if service_registry:
        logging.info(f"Writing global service registry to {SERVICES_JSON_PATH}...")
        SERVICES_JSON_PATH.write_bytes(msgspec.json.encode(service_registry))

    generate_auth_notice(services_requiring_override_fix, services_with_active_override)
    total_duration = time.perf_counter() - overall_start_time
    generate_performance_report(download_results, processing_results, total_duration)

    logging.info("Data population process finished.")

if __name__ == "__main__":
    main()
