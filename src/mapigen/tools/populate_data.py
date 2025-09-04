from __future__ import annotations
import argparse
import logging
import multiprocessing as mp
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

import msgspec

import glob

from mapigen.cache.ranking import get_rank
from mapigen.metadata.fetcher import fetch_specs_concurrently, fetch_postman_specs
from mapigen.services.registry_service import RegistryService
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
OVERRIDES_PATH = REGISTRY_DIR / "overrides.json"
SERVICES_JSON_PATH = SRC_DIR / "services.json"

def setup_arg_parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Fetch and process API specifications.")
    parser.add_argument("--source", type=str, nargs='+', help="Optional: The specific source type(s) to run (e.g., github, postman). Runs all if not specified.")
    parser.add_argument("--download-workers", type=int, default=25, help="Concurrent download workers.")
    parser.add_argument("--process-workers", type=int, default=mp.cpu_count(), help="Parallel processing workers.")
    parser.add_argument("--force-download", action="store_true", help="Force re-download of all specs, overwriting cached versions.")
    parser.add_argument("--force-reprocess", action="store_true", help="Force reprocessing of all downloaded specs.")
    parser.add_argument("--no-compress-utilize", action="store_true", help="Do not compress final utilize.json files.")
    parser.add_argument("--no-compress-original", action="store_true", help="Do not compress original downloaded specs.")
    parser.add_argument("--memory-threshold", type=float, default=2048.0, help="Memory threshold in MB to trigger garbage collection.")
    return parser.parse_args()

def load_configuration() -> tuple[dict[str, Any], dict[str, Any]]:
    """Loads all _sources.yaml files from the registry directory and categorizes them."""
    all_sources: Dict[str, List[Dict[str, Any]]] = {
        "github": [],
        "custom": [],
        "postman": [],
    }

    for fpath in glob.glob(f"{REGISTRY_DIR}/*_sources.yaml"):
        source_type = Path(fpath).stem.split("_")[0]
        if source_type in all_sources:
            try:
                content = Path(fpath).read_bytes()
                decoded_content = msgspec.yaml.decode(content)
                all_sources[source_type].extend(decoded_content.get(source_type, []))
            except (IOError, msgspec.ValidationError) as e:
                logging.error(f"Failed to load or parse {fpath}: {e}")

    overrides: dict[str, Any] = {}
    if OVERRIDES_PATH.exists():
        overrides = msgspec.json.decode(OVERRIDES_PATH.read_bytes())
    
    return all_sources, overrides

def write_metadata(result: dict[str, Any], overrides: dict[str, Any]):
    """Writes metadata for a single processed collection to its directory."""
    provider = result["provider"]
    source = result["source"]
    api = result["api"]
    service_key = result["service_key"]

    service_data_dir = DATA_DIR / provider / source / api
    metadata_yml_path = service_data_dir / "metadata.yml"
    
    # API reference URL might not be present for all sources, e.g., Postman
    api_reference_url = result.get("url", "")

    first_accessed_time = datetime.now(timezone.utc).isoformat()
    if metadata_yml_path.exists():
        try:
            existing_metadata = msgspec.yaml.decode(metadata_yml_path.read_text())
            first_accessed_time = existing_metadata.get("first_accessed", first_accessed_time)
        except (IOError, msgspec.ValidationError):
            pass

    final_auth_info = result["auth_info"].copy()
    if service_key in overrides and "auth" in overrides[service_key]:
        final_auth_info.update(overrides[service_key]["auth"])
    
    metadata_content = {
        "format_version": FORMAT_VERSION,
        "provider": provider,
        "api": api,
        "source": source,
        "first_accessed": first_accessed_time,
        "updated_at": datetime.now(timezone.utc).isoformat(),
        "api_reference": api_reference_url,
        "status": result["status"],
        "operation_count": result.get("processed_op_count", 0),
        "reusable_parameter_count": result.get("reusable_param_count", 0),
        "coverage": result.get("coverage", "N/A"),
        "auth_types": final_auth_info["auth_types"],
        "primary_auth": final_auth_info["primary_auth"],
        "popularity_rank": get_rank(api), # Rank by api name
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
    
    # Determine which sources to run
    sources_to_run = args.source if args.source else all_sources.keys()

    if not any(all_sources.get(s) for s in sources_to_run):
        logging.warning(f"No sources found for specified types: {sources_to_run}. Exiting.")
        return

    # --- Download Phase ---
    download_results: List[Dict[str, Any]] = []
    
    if "postman" in sources_to_run and all_sources.get("postman"):
        logging.info("Fetching specs from Postman...")
        download_results.extend(fetch_postman_specs(all_sources["postman"], args))

    url_source_types = [s for s in ["github", "custom"] if s in sources_to_run]
    for source_type in url_source_types:
        sources = all_sources.get(source_type, [])
        if sources:
            download_results.extend(fetch_specs_concurrently(sources, source_type, 50, args))

    # --- Processing Phase ---
    specs_to_process = list(DATA_DIR.glob("**/*.openapi.json.zst"))
    
    # This logic needs to be updated to handle the new structure and --force-reprocess
    # For now, we process all found specs.

    processing_results: List[Dict[str, Any]] = []
    if not specs_to_process:
        logging.info("No specs found to process.")
    else:
        processing_results = run_processing_pipeline(specs_to_process, args)


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
                service_key = result["service_key"]
                if service_key in overrides and "auth" in overrides[service_key]:
                    services_with_active_override.append(service_key)
                else:
                    services_requiring_override_fix.append(service_key)

    registry_service = RegistryService(data_dir=DATA_DIR, registry_path=SERVICES_JSON_PATH)
    service_registry = registry_service.build_registry()
    registry_service.save_registry(service_registry)

    generate_auth_notice(services_requiring_override_fix, services_with_active_override)
    total_duration = time.perf_counter() - overall_start_time
    generate_performance_report(download_results, processing_results, total_duration)

    logging.info("Data population process finished.")

if __name__ == "__main__":
    main()
