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
from mapigen.metadata.fetcher import fetch_specs_concurrently, fetch_postman_specs
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
OVERRIDES_PATH = REGISTRY_DIR / "overrides.json"
SERVICES_JSON_PATH = SRC_DIR / "services.json"

def setup_arg_parser() -> argparse.Namespace:
    """Sets up the argument parser for the script."""
    parser = argparse.ArgumentParser(description="Fetch and process API specifications.")
    parser.add_argument("--batch-size", type=int, default=None, help="Number of specs to process in a batch. Disables dynamic batching.")
    parser.add_argument("--download-workers", type=int, default=25, help="Concurrent download workers.")
    parser.add_argument("--process-workers", type=int, default=mp.cpu_count(), help="Parallel processing workers.")
    parser.add_argument("--skip-download", action="store_true", help="Skip download, use existing specs.")
    parser.add_argument("--force-reprocess", action="store_true", help="Force reprocessing of all specs.")
    parser.add_argument("--postman", action="store_true", help="Only process Postman sources.")
    parser.add_argument("--update-all", action="store_true", help="Update all missing services from the registry.")
    parser.add_argument("--cache", action="store_true", help="Use cached downloads but force reprocessing.")
    parser.add_argument("--no-compress-utilize", action="store_true", help="Do not compress final utilize.json files.")
    parser.add_argument("--no-compress-original", action="store_true", help="Do not compress original downloaded specs, for debugging.")
    parser.add_argument("--memory-threshold", type=float, default=2048.0, help="Memory threshold in MB to trigger garbage collection.")
    return parser.parse_args()

def load_configuration() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Loads configuration from the YAML source files."""
    all_sources: list[dict[str, Any]] = []
    source_files = {
        "github": REGISTRY_DIR / "github_sources.yaml",
        "custom": REGISTRY_DIR / "custom_sources.yaml",
        "postman": REGISTRY_DIR / "postman_sources.yaml",
    }
    for source, path in source_files.items():
        if path.exists():
            try:
                entries = msgspec.yaml.decode(path.read_bytes(), type=List[Dict[str, Any]])
                for entry in entries:
                    if source == "postman" and "collections" in entry:
                        for collection in entry["collections"]:
                            all_sources.append({
                                "provider": entry["provider"], 
                                "url": entry["url"], 
                                "api": collection["name"], 
                                "uid": collection["uid"],
                                "source": source
                            })
                    else:
                        entry["source"] = source
                        all_sources.append(entry)
            except (msgspec.ValidationError, TypeError) as e:
                logging.error(f"Failed to parse {path}: {e}")
    overrides: dict[str, Any] = {}
    if OVERRIDES_PATH.exists():
        overrides = msgspec.json.decode(OVERRIDES_PATH.read_bytes())
    return all_sources, overrides

def discover_sources_to_fetch(all_sources: list[dict[str, Any]], args: argparse.Namespace) -> list[dict[str, Any]]:
    """Determines which sources to fetch based on script arguments."""
    if args.update_all:
        logging.info("Discovering missing services to update...")
        missing_sources = []
        for source_info in all_sources:
            if source_info["source"] == "postman":
                # Postman collections are discovered and cached in the fetch phase
                missing_sources.append(source_info)
                continue

            service_data_dir = get_service_data_path(source_info["provider"], source_info["api"], source_info["source"])
            if not (service_data_dir / "metadata.yml").exists():
                missing_sources.append(source_info)
        logging.info(f"Found {len(missing_sources)} services to update.")
        return missing_sources

    if args.postman:
        logging.info("Filtering for Postman sources only.")
        return [s for s in all_sources if s.get("source") == "postman"]
    
    return all_sources

def run_fetch_phase(sources_to_fetch: list[dict[str, Any]], args: argparse.Namespace) -> list[dict[str, Any]]:
    """Runs the fetchers for the given sources."""
    if args.skip_download:
        logging.info("Skipping download phase.")
        return []

    logging.info(f"Fetching {len(sources_to_fetch)} sources...")
    postman_sources = [s for s in sources_to_fetch if s.get("source") == "postman"]
    other_sources = [s for s in sources_to_fetch if s.get("source") != "postman"]
    
    download_results: List[Dict[str, Any]] = []
    if postman_sources:
        # We pass the workspace-level sources to fetch_postman_specs for discovery
        postman_workspaces = {s["url"]: s for s in postman_sources}.values()
        download_results.extend(fetch_postman_specs(list(postman_workspaces), args))
    if other_sources:
        download_batch_size = 50
        download_results.extend(fetch_specs_concurrently(other_sources, download_batch_size, args))
    
    return download_results

def discover_services_to_process(download_results: list[dict[str, Any]], args: argparse.Namespace) -> list[dict[str, Any]]:
    """Determines which services need to be processed."""
    services_to_process = []
    
    # Process all successfully downloaded services
    successful_downloads = [r for r in download_results if r["status"] == "success"]
    services_to_process.extend(successful_downloads)

    # If force_reprocess is on, also process skipped services
    if args.force_reprocess:
        logging.info("Forcing reprocessing of all downloaded and skipped specs.")
        skipped_downloads = [r for r in download_results if r["status"] == "skipped"]
        services_to_process.extend(skipped_downloads)
    else:
        # Check skipped services to see if they are missing processed files
        logging.info("Checking for cached services that need reprocessing...")
        skipped_downloads = [r for r in download_results if r["status"] == "skipped"]
        for s in skipped_downloads:
            if "api" not in s:
                continue
            
            utilize_zst_path = get_service_data_path(s['provider'], s['api'], s['source']) / f"{s['api']}.utilize.json.zst"
            utilize_json_path = get_service_data_path(s['provider'], s['api'], s['source']) / f"{s['api']}.utilize.json"

            if not utilize_zst_path.exists() and not utilize_json_path.exists():
                services_to_process.append(s)

    return services_to_process

def run_process_phase(services_to_process: list[dict[str, Any]], args: argparse.Namespace) -> list[dict[str, Any]]:
    """Runs the processing pipeline for the given services."""
    if not services_to_process:
        logging.info("No new services to process.")
        return []

    logging.info(f"Processing {len(services_to_process)} services...")
    for entry in services_to_process:
        try:
            if "api" in entry and "source" in entry:
                size_path = get_service_data_path(entry['provider'], entry['api'], entry['source']) / f"{entry['api']}.openapi.json.zst"
                entry['size'] = size_path.stat().st_size if size_path.exists() else 0
            else:
                entry['size'] = 0
        except FileNotFoundError:
            logging.warning(f"Could not find compressed spec for {entry.get('api', '<dynamic>')}. It will be skipped during processing.")
            entry['size'] = 0
            
    return run_processing_pipeline(services_to_process, args)

def run_aggregation_phase(download_results: list[dict[str, Any]], processing_results: list[dict[str, Any]], overrides: dict[str, Any], overall_start_time: float, args: argparse.Namespace):
    """Handles metadata writing, registry generation, and reporting."""
    logging.info("Starting aggregation and reporting phase...")

    # Report discrepancies
    skipped_downloads = [r for r in download_results if r["status"] == "skipped"]
    if not args.update_all and skipped_downloads:
        logging.warning(f"Found {len(skipped_downloads)} services that were skipped due to existing cache.")
        logging.warning("Run with --update-all to download and process these services.")

    logging.info("--- Download Failures ---")
    failures = [r for r in download_results if r["status"] == "failure"]
    if not failures:
        logging.info("No download failures.")
    else:
        for f in failures:
            logging.warning(f"Provider: {f.get('provider')}, API: {f.get('api')}, Source: {f.get('source')}, Reason: {f.get('reason')}")
    logging.info("-------------------------")
    
    services_requiring_override_fix: list[str] = []
    services_with_active_override: list[str] = []

    for result in processing_results:
        if result["status"] == "success":
            write_metadata(result, overrides)
            handle_utilize_compression(result["utilize_path"], result)
            
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

def write_metadata(result: dict[str, Any], overrides: dict[str, Any]):
    """Writes the metadata.yml file for a processed service."""
    provider, api, source = result["provider"], result["api"], result["source"]
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
        "api_reference": result.get("url", ""), "status": result["status"],
        "operation_count": result.get("processed_op_count", 0),
        "reusable_parameter_count": result.get("reusable_param_count", 0),
        "coverage": result.get("coverage", "N/A"),
        "auth_types": final_auth_info.get("auth_types", []),
        "primary_auth": final_auth_info.get("primary_auth", "none"),
        "popularity_rank": get_rank(api),
    }
    metadata_yml_path.write_bytes(msgspec.yaml.encode(metadata_content))

def handle_utilize_compression(utilize_path: Path, result: dict[str, Any]):
    """Handles the compression of the utilize.json file."""
    if not result.get("no_compress_utilize", False):
        compressed_data = compress_with_zstd(utilize_path.read_bytes())
        compressed_path = utilize_path.with_suffix(".json.zst")
        compressed_path.write_bytes(compressed_data)
        utilize_path.unlink()

def main():
    """Main function to orchestrate the data population pipeline."""
    args = setup_arg_parser()
    overall_start_time = time.perf_counter()
    
    if args.cache:
        args.skip_download = True
        args.force_reprocess = True
        
    all_sources, overrides = load_configuration()
    if not all_sources:
        logging.warning("No sources found. Exiting.")
        return

    sources_to_fetch = discover_sources_to_fetch(all_sources, args)
    download_results = run_fetch_phase(sources_to_fetch, args)
    services_to_process = discover_services_to_process(download_results, args)
    processing_results = run_process_phase(services_to_process, args)
    
    run_aggregation_phase(download_results, processing_results, overrides, overall_start_time, args)

    logging.info("Data population process finished.")

if __name__ == "__main__":
    main()