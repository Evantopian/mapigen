from __future__ import annotations
import orjson as json
import argparse
import yaml
import shutil
import hashlib
from pathlib import Path
import logging
from datetime import datetime, timezone
from typing import Any, cast

from mapigen.metadata.fetcher import fetch_spec
from mapigen.metadata.converter import normalize_spec
from mapigen.metadata.extractor import extract_operations_and_components, save_metadata
from mapigen.tools.utils import count_openapi_operations, load_spec, compress_metadata, extract_auth_info
from mapigen.cache.ranking import get_rank

FORMAT_VERSION = 3

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
AUTH_NOTICE_PATH = REGISTRY_DIR / "AUTH_NOTICE.md"

def setup_arg_parser() -> argparse.Namespace:
    """Sets up and parses command-line arguments."""
    parser = argparse.ArgumentParser(description="Fetch and process API specifications.")
    parser.add_argument("--keep-raw-specs", action="store_true", help="Keep original downloaded spec files.")
    parser.add_argument("--no-compress", action="store_true", help="Do not compress the final utilize.json file.")
    parser.add_argument("--rank", type=int, default=None, help="The minimum rank required to compress service data. If not set, all services are compressed unless --no-compress is used.")
    parser.add_argument("--cache", action="store_true", help="Skip processing services if metadata already exists.")
    return parser.parse_args()

def load_configuration() -> tuple[dict[str, Any], dict[str, Any]]:
    """Loads service sources and overrides from JSON files."""
    all_sources: dict[str, str] = {}
    if CUSTOM_SOURCES_PATH.exists():
        all_sources.update(json.loads(CUSTOM_SOURCES_PATH.read_text()))
    if GITHUB_SOURCES_PATH.exists():
        all_sources.update(json.loads(GITHUB_SOURCES_PATH.read_text()))

    overrides: dict[str, Any] = {}
    if OVERRIDES_PATH.exists():
        logging.info(f"Loading overrides from {OVERRIDES_PATH}")
        overrides = json.loads(OVERRIDES_PATH.read_text())
    
    return all_sources, overrides

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
        raw_spec_typed: dict[str, Any] = raw_spec
        raw_op_count = count_openapi_operations(raw_spec_typed)
        notes.append(f"Found {raw_op_count} operations in raw spec.")

        notes.append("Normalizing and validating spec...")
        normalized_spec = normalize_spec(raw_spec_path)

        notes.append("Extracting lightweight 'utilize' metadata...")
        processed_data: dict[str, Any] = extract_operations_and_components(service_name, cast(dict[str, Any], normalized_spec))
        processed_data['servers'] = servers
        processed_data['format_version'] = FORMAT_VERSION
        op_count = len(processed_data['operations'])
        param_count = len(processed_data['components']['parameters'])
        notes.append(f"Extracted {op_count} operations and {param_count} reusable parameters.")

        coverage = f"{op_count / raw_op_count:.1%}" if raw_op_count > 0 else "N/A"

        return {
            "status": "success", "api_hash": api_hash, "servers": servers,
            "auth_info": auth_info, "processed_op_count": op_count,
            "reusable_param_count": param_count, "coverage": coverage,
            "processed_data": processed_data, "notes": notes
        }
    except Exception as e:
        error_message = f"ERROR at step '{notes[-1] if notes else 'initialization'}': {e}"
        logging.error(f"Failed to process service {service_name}: {error_message}")
        return {"status": "failure", "notes": notes + [error_message]}

def write_metadata(service_name: str, result: dict[str, Any], service_data_dir: Path, overrides: dict[str, Any]):
    """Writes the metadata.yml file for a service."""
    metadata_yml_path = service_data_dir / "metadata.yml"
    first_accessed_time = datetime.now(timezone.utc).isoformat()
    if metadata_yml_path.exists():
        try:
            existing_metadata = yaml.safe_load(metadata_yml_path.read_text())
            first_accessed_time = existing_metadata.get("first_accessed", first_accessed_time)
        except (IOError, yaml.YAMLError):
            pass

    final_auth_info = result["auth_info"].copy()
    if service_name in overrides and "auth" in overrides[service_name]:
        final_auth_info.update(overrides[service_name]["auth"])

    rank = get_rank(service_name)
    metadata_content = {
        "format_version": FORMAT_VERSION, "first_accessed": first_accessed_time,
        "updated_at": datetime.now(timezone.utc).isoformat(), "api_reference": result["url"],
        "status": result["status"], "api_hash": result["api_hash"],
        "operation_count": result["processed_op_count"],
        "reusable_parameter_count": result["reusable_param_count"],
        "coverage": result["coverage"], "auth_types": final_auth_info["auth_types"],
        "primary_auth": final_auth_info["primary_auth"], "popularity_rank": rank,
    }
    metadata_yml_path.write_text(yaml.dump(metadata_content, indent=2, sort_keys=False), encoding="utf-8")

def handle_compression(utilize_path: Path, rank: int, args: argparse.Namespace):
    """Handles the compression of the utilize.json file based on arguments."""
    should_compress = False
    if args.no_compress:
        should_compress = False
    elif args.rank is not None:
        if rank >= args.rank:
            should_compress = True
    else:
        should_compress = True

    if should_compress:
        logging.info(f"Compressing {utilize_path.stem} data (rank {rank}).")
        compress_metadata(utilize_path)
        if utilize_path.exists():
            utilize_path.unlink()

def generate_auth_notice(services_requiring_fix: list[str], services_with_override: list[str]):
    """Generates the AUTH_NOTICE.md file if needed."""
    notice_content = "# Authentication Override Notice\n\nThis notice provides a summary of authentication configurations for the processed services.\n"

    if not services_requiring_fix and not services_with_override:
        if AUTH_NOTICE_PATH.exists():
            notice_content += "\n---\n\n### Active Overrides\n\nAll services were successfully discovered and their OpenAPI specifications fully resolved. Authentication overrides from `src/mapigen/registry/overrides.json` were applied where relevant. No manual action is required.\n\n"
            AUTH_NOTICE_PATH.write_text(notice_content)
            logging.info("All services have auth info; removing old notice file.")
        return

    if services_with_override:
        notice_content += "\n---\n\n### Active Overrides\n\nThe following services have incomplete OpenAPI specifications. Manual authentication overrides were successfully found and applied from `src/mapigen/registry/overrides.json`. No action is needed for these services.\n\n"
        for service in sorted(services_with_override):
            notice_content += f"- `{service}`\n"

    if services_requiring_fix:
        notice_content += "\n---\n\n### ACTION REQUIRED: Add Override\n\nThe following services were processed but have no declared authentication methods, and no override was found.\n\nTo ensure the SDK can work with these services, you must add a manual override to `src/mapigen/registry/overrides.json`.\n\n**Services needing an override:**\n\n"
        for service in sorted(services_requiring_fix):
            notice_content += f"- `{service}`\n"
        notice_content += "\n**How to fix:**\n\n1. Consult the service's API documentation to determine the correct authentication method(s).\n2. Add an entry to `src/mapigen/registry/overrides.json`.\n\n"

    AUTH_NOTICE_PATH.write_text(notice_content)
    logging.warning(f"Auth Notice generated at {AUTH_NOTICE_PATH}. Action may be required.")

def main():
    """Main function to orchestrate the data population process."""
    args = setup_arg_parser()
    logging.info("Starting data population process...")
    
    all_sources, overrides = load_configuration()
    if not all_sources:
        logging.warning("No sources found in registry. Exiting.")
        return

    logging.info(f"Found {len(all_sources)} services to process.")
    
    service_registry = {}
    services_requiring_override_fix = []
    services_with_active_override = []

    for service_name, url in all_sources.items():
        service_data_dir = DATA_DIR / service_name
        metadata_yml_path = service_data_dir / "metadata.yml"
        utilize_json_path = service_data_dir / f"{service_name}.utilize.json"
        utilize_lz4_path = service_data_dir / f"{service_name}.utilize.json.lz4"

        is_cached = args.cache and metadata_yml_path.exists() and (utilize_json_path.exists() or utilize_lz4_path.exists())
        
        original_auth_info = {}
        if is_cached:
            logging.info(f"[CACHED] Skipping service processing for: {service_name}")
            metadata = yaml.safe_load(metadata_yml_path.read_text())
            original_auth_info = {"auth_types": metadata.get("auth_types", []), "primary_auth": metadata.get("primary_auth", "none")}
        else:
            if service_data_dir.exists() and not next(service_data_dir.glob(f"{service_name}.openapi.*", ), None):
                shutil.rmtree(service_data_dir)
            service_data_dir.mkdir(parents=True, exist_ok=True)

            logging.info(f"--- Processing: {service_name} ---")
            result = process_service(service_name, url, service_data_dir)
            result["url"] = url

            if result["status"] == "success":
                original_auth_info = result["auth_info"]
                write_metadata(service_name, result, service_data_dir, overrides)
                utilize_path = save_metadata(service_name, result["processed_data"], service_data_dir)
                handle_compression(utilize_path, get_rank(service_name), args)
            
            logging.info(f"Finished processing: {service_name} with status: {result.get('status', 'unknown')}")

        if original_auth_info and not original_auth_info.get("auth_types"):
            if service_name in overrides and "auth" in overrides[service_name]:
                services_with_active_override.append(service_name)
            else:
                services_requiring_override_fix.append(service_name)

        if metadata_yml_path.exists():
            final_auth_info = original_auth_info.copy()
            if service_name in overrides and "auth" in overrides[service_name]:
                final_auth_info.update(overrides[service_name]["auth"])
            
            metadata = yaml.safe_load(metadata_yml_path.read_text())
            service_registry[service_name] = {
                "path": f"data/{service_name}",
                "operation_count": metadata.get("operation_count", 0),
                "auth_types": final_auth_info.get("auth_types", []),
                "primary_auth": final_auth_info.get("primary_auth", "none"),
                "popularity_rank": metadata.get("popularity_rank", 999)
            }

    if service_registry:
        logging.info(f"Writing global service registry to {SERVICES_JSON_PATH}...")
        SERVICES_JSON_PATH.write_text(json.dumps(service_registry, option=json.OPT_INDENT_2).decode("utf-8"))

    generate_auth_notice(services_requiring_override_fix, services_with_active_override)
    logging.info("Data population process finished.")

if __name__ == "__main__":
    main()