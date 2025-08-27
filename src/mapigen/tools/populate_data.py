from __future__ import annotations
import json
import argparse
import yaml
import shutil
import hashlib
from pathlib import Path
import logging
from datetime import datetime, timezone
from typing import Any, Optional, cast

from mapigen.metadata.fetcher import fetch_spec
from mapigen.metadata.converter import normalize_spec
from mapigen.metadata.extractor import extract_operations_and_components, save_metadata
from mapigen.tools.utils import count_openapi_operations, load_spec, compress_metadata, extract_auth_info
from mapigen.cache.ranking import get_rank

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define paths
ROOT_DIR = Path(__file__).resolve().parent.parent.parent.parent
SRC_DIR = ROOT_DIR / "src" / "mapigen"
DATA_DIR = SRC_DIR / "data"
REGISTRY_DIR = SRC_DIR / "registry"
CUSTOM_SOURCES_PATH = REGISTRY_DIR / "custom_sources.json"
GITHUB_SOURCES_PATH = REGISTRY_DIR / "github_sources.json"
OVERRIDES_PATH = REGISTRY_DIR / "overrides.json"
SERVICES_JSON_PATH = SRC_DIR / "services.json"

def process_service(service_name: str, url: str, service_data_dir: Path) -> dict[str, Any]:
    """Fetches and processes a single service spec, returning results and logs."""
    notes: list[str] = []
    try:
        notes.append(f"Fetching spec from {url}...")
        raw_spec_path = fetch_spec(service_name, url, service_data_dir)

        raw_content = raw_spec_path.read_bytes()
        api_hash = hashlib.sha256(raw_content).hexdigest()
        raw_spec = load_spec(raw_spec_path)
        
        notes.append("Extracting auth info...")
        auth_info = extract_auth_info(raw_spec)

        servers: list[dict[str, Any]] = raw_spec.get("servers", [])
        raw_spec_typed: dict[str, Any] = raw_spec # Explicitly cast
        raw_op_count = count_openapi_operations(raw_spec_typed)
        notes.append(f"Found {raw_op_count} operations in raw spec.")

        notes.append("Normalizing and validating spec...")
        normalized_spec = normalize_spec(raw_spec_path)

        notes.append("Extracting lightweight 'utilize' metadata...")
        processed_data: dict[str, Any] = extract_operations_and_components(service_name, cast(dict[str, Any], normalized_spec))
        processed_data['servers'] = servers
        op_count = len(processed_data['operations'])
        param_count = len(processed_data['components']['parameters'])
        notes.append(f"Extracted {op_count} operations and {param_count} reusable parameters.")

        coverage = f"{op_count / raw_op_count:.1%}" if raw_op_count > 0 else "N/A"

        return {
            "status": "success",
            "api_hash": api_hash,
            "servers": servers,
            "auth_info": auth_info,
            "processed_op_count": op_count,
            "reusable_param_count": param_count,
            "coverage": coverage,
            "processed_data": processed_data,
            "notes": notes
        }

    except Exception as e:
        error_message = f"ERROR at step '{notes[-1] if notes else 'initialization'}': {e}"
        logging.error(f"Failed to process service {service_name}: {error_message}")
        return {
            "status": "failure",
            "notes": notes + [error_message]
        }

def main():
    """
    Main function to orchestrate the data population process.
    """
    parser = argparse.ArgumentParser(description="Fetch and process API specifications.")
    parser.add_argument("--keep-raw-specs", action="store_true", help="Keep original downloaded spec files.")
    parser.add_argument("--no-compress", action="store_true", help="Do not compress the final utilize.json file.")
    parser.add_argument("--rank", type=int, default=2, help="The rank at which to start compressing service data. Ranks below this value will not be compressed.")
    parser.add_argument("--cache", action="store_true", help="Skip processing services if metadata already exists.")
    args = parser.parse_args()

    logging.info("Starting data population process...")

    DATA_DIR.mkdir(parents=True, exist_ok=True)

    all_sources: dict[str, str] = {}
    if CUSTOM_SOURCES_PATH.exists():
        all_sources.update(json.loads(CUSTOM_SOURCES_PATH.read_text()))
    if GITHUB_SOURCES_PATH.exists():
        all_sources.update(json.loads(GITHUB_SOURCES_PATH.read_text()))

    overrides: dict[str, Any] = {}
    if OVERRIDES_PATH.exists():
        logging.info(f"Loading overrides from {OVERRIDES_PATH}")
        overrides = json.loads(OVERRIDES_PATH.read_text())

    if not all_sources:
        logging.warning("No sources found in registry. Exiting.")
        return

    logging.info(f"Found {len(all_sources)} services to process.")
    
    service_registry: dict[str, Any] = {}
    services_requiring_override_fix: list[str] = []
    services_with_active_override: list[str] = []

    for service_name, url in all_sources.items():
        service_data_dir: Path = DATA_DIR / service_name
        metadata_yml_path: Path = service_data_dir / "metadata.yml"
        utilize_json_path = service_data_dir / f"{service_name}.utilize.json"
        utilize_lz4_path = service_data_dir / f"{service_name}.utilize.json.lz4"

        is_cached = args.cache and metadata_yml_path.exists() and (utilize_json_path.exists() or utilize_lz4_path.exists())

        original_auth_info = {}
        
        if is_cached:
            logging.info(f"[CACHED] Skipping service processing for: {service_name}")
            metadata = yaml.safe_load(metadata_yml_path.read_text())
            original_auth_info = {
                "auth_types": metadata.get("auth_types", []),
                "primary_auth": metadata.get("primary_auth", "none")
            }
        else:
            raw_spec_path: Optional[Path] = next(service_data_dir.glob(f"{service_name}.openapi.*"), None)
            if service_data_dir.exists() and not raw_spec_path:
                shutil.rmtree(service_data_dir)
            service_data_dir.mkdir(parents=True, exist_ok=True)

            logging.info(f"--- Processing: {service_name} ---")
            result: dict[str, Any] = process_service(service_name, url, service_data_dir)

            if result["status"] == "success":
                original_auth_info = result["auth_info"]
            
                first_accessed_time: str = datetime.now(timezone.utc).isoformat()
                if metadata_yml_path.exists():
                    try:
                        existing_metadata: dict[str, Any] = yaml.safe_load(metadata_yml_path.read_text())
                        first_accessed_time = existing_metadata.get("first_accessed", first_accessed_time)
                    except (IOError, yaml.YAMLError):
                        pass

                final_auth_info_for_meta = original_auth_info.copy()
                if service_name in overrides and "auth" in overrides[service_name]:
                    final_auth_info_for_meta.update(overrides[service_name]["auth"])

                rank = get_rank(service_name)
                metadata_content: dict[str, Any] = {
                    "format_version": 2,
                    "first_accessed": first_accessed_time,
                    "updated_at": datetime.now(timezone.utc).isoformat(),
                    "api_reference": url,
                    "status": result["status"],
                    "api_hash": result["api_hash"],
                    "operation_count": result["processed_op_count"],
                    "reusable_parameter_count": result["reusable_param_count"],
                    "coverage": result["coverage"],
                    "auth_types": final_auth_info_for_meta["auth_types"],
                    "primary_auth": final_auth_info_for_meta["primary_auth"],
                    "popularity_rank": rank,
                }
                metadata_yml_path.write_text(yaml.dump(metadata_content, indent=2, sort_keys=False), encoding="utf-8")

                utilize_path: Path = save_metadata(service_name, result["processed_data"], service_data_dir)
                if rank >= args.rank and not args.no_compress:
                    logging.info(f"Compressing {service_name} data (rank {rank} >= threshold {args.rank}).")
                    compress_metadata(utilize_path)
                    if utilize_path.exists():
                        utilize_path.unlink()
            
            logging.info(f"Finished processing: {service_name} with status: {result.get('status', 'unknown')}")

        # --- Notice Logic (runs for all services) ---
        if original_auth_info:
            if not original_auth_info.get("auth_types"):
                if service_name in overrides and "auth" in overrides[service_name]:
                    services_with_active_override.append(service_name)
                else:
                    services_requiring_override_fix.append(service_name)

        # --- Registry Population (runs for all services) ---
        if metadata_yml_path.exists():
            final_auth_info_for_registry = original_auth_info.copy()
            if service_name in overrides and "auth" in overrides[service_name]:
                final_auth_info_for_registry.update(overrides[service_name]["auth"])
            
            metadata = yaml.safe_load(metadata_yml_path.read_text())
            service_registry[service_name] = {
                "path": f"data/{service_name}",
                "operation_count": metadata.get("operation_count", 0),
                "auth_types": final_auth_info_for_registry["auth_types"],
                "primary_auth": final_auth_info_for_registry["primary_auth"],
                "popularity_rank": metadata.get("popularity_rank", 999)
            }

    if service_registry:
        logging.info(f"Writing global service registry to {SERVICES_JSON_PATH}...")
        SERVICES_JSON_PATH.write_text(json.dumps(service_registry, indent=2))

    # Generate authentication notice file
    AUTH_NOTICE_PATH = REGISTRY_DIR / "AUTH_NOTICE.md"
    if not services_requiring_override_fix and not services_with_active_override:
        if AUTH_NOTICE_PATH.exists():
            AUTH_NOTICE_PATH.unlink()
            logging.info("All services have auth info; removing old notice file.")
    else:
        notice_content = """# Authentication Override Notice

This notice provides a summary of authentication configurations for the processed services.
"""

        if services_with_active_override:
            notice_content += "\n---\n\n### Active Overrides\n\nThe following services have incomplete OpenAPI specifications. Manual authentication overrides were successfully found and applied from `src/mapigen/registry/overrides.json`. No action is needed for these services.\n\n"

            for service in sorted(services_with_active_override):
                notice_content += f"- `{service}`\n"

        if services_requiring_override_fix:
            notice_content += "\n---\n\n### ACTION REQUIRED: Add Override\n\nThe following services were processed but have no declared authentication methods, and no override was found.\n\nTo ensure the SDK can work with these services, you must add a manual override to `src/mapigen/registry/overrides.json`.\n\n**Services needing an override:**\n\n"
            for service in sorted(services_requiring_override_fix):
                notice_content += f"- `{service}`\n"
            
            notice_content += "\n**How to fix:**\n\n1. Consult the service's API documentation to determine the correct authentication method(s).\n2. Add an entry to `src/mapigen/registry/overrides.json`.\n\n"

        AUTH_NOTICE_PATH.write_text(notice_content)
        logging.warning(f"Auth Notice generated at {AUTH_NOTICE_PATH}. Action may be required.")

    logging.info("Data population process finished.")

if __name__ == "__main__":
    main()
