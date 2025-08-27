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
from mapigen.tools.utils import count_openapi_operations, load_spec, compress_metadata

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define paths
ROOT_DIR = Path(__file__).resolve().parent.parent.parent.parent
DATA_DIR = ROOT_DIR / "src" / "mapigen" / "data"
REGISTRY_DIR = ROOT_DIR / "src" / "mapigen" / "registry"
CUSTOM_SOURCES_PATH = REGISTRY_DIR / "custom_sources.json"
GITHUB_SOURCES_PATH = REGISTRY_DIR / "github_sources.json"

def process_service(service_name: str, url: str, service_data_dir: Path) -> dict[str, Any]:
    """Fetches and processes a single service spec, returning results and logs."""
    notes: list[str] = []
    try:
        notes.append(f"Fetching spec from {url}...")
        raw_spec_path = fetch_spec(service_name, url, service_data_dir)

        raw_content = raw_spec_path.read_bytes()
        api_hash = hashlib.sha256(raw_content).hexdigest()
        raw_spec = load_spec(raw_spec_path)
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
    parser.add_argument("--cache", action="store_true", help="Skip processing services if metadata already exists.")
    args = parser.parse_args()

    logging.info("Starting data population process...")

    DATA_DIR.mkdir(parents=True, exist_ok=True)

    all_sources: dict[str, str] = {}
    if CUSTOM_SOURCES_PATH.exists():
        all_sources.update(json.loads(CUSTOM_SOURCES_PATH.read_text()))
    if GITHUB_SOURCES_PATH.exists():
        all_sources.update(json.loads(GITHUB_SOURCES_PATH.read_text()))

    if not all_sources:
        logging.warning("No sources found in registry. Exiting.")
        return

    logging.info(f"Found {len(all_sources)} services to process.")

    for service_name, url in all_sources.items():
        service_data_dir: Path = DATA_DIR / service_name
        metadata_yml_path: Path = service_data_dir / "metadata.yml"
        update_yml_path: Path = service_data_dir / "update.yml"

        if args.cache and metadata_yml_path.exists() and not update_yml_path.exists():
            logging.info(f"[CACHED] Skipping service: {service_name}")
            continue

        # Clean and prepare directory
        # Keep the raw spec if it exists
        raw_spec_path: Optional[Path] = next(service_data_dir.glob(f"{service_name}.openapi.*"), None)
        if service_data_dir.exists() and not raw_spec_path:
            shutil.rmtree(service_data_dir)
        service_data_dir.mkdir(parents=True, exist_ok=True)

        logging.info(f"--- Processing: {service_name} ---")
        result: dict[str, Any] = process_service(service_name, url, service_data_dir)

        first_accessed_time: str = datetime.now(timezone.utc).isoformat()
        if metadata_yml_path.exists():
            try:
                existing_metadata: dict[str, Any] = yaml.safe_load(metadata_yml_path.read_text())
                first_accessed_time = existing_metadata.get("first_accessed", first_accessed_time)
            except (IOError, yaml.YAMLError):
                pass

        metadata_content: dict[str, Any] = {
            "format_version": 2,
            "first_accessed": first_accessed_time,
            "updated_at": datetime.now(timezone.utc).isoformat(),
            "api_reference": url,
            "status": result["status"],
        }

        if result["status"] == "success":
            metadata_content.update({
                "api_hash": result["api_hash"],
                "operation_count": result["processed_op_count"],
                "reusable_parameter_count": result["reusable_param_count"],
                "coverage": result["coverage"],
            })
            utilize_path: Path = save_metadata(service_name, result["processed_data"], service_data_dir)
            if not args.no_compress:
                compress_metadata(utilize_path)
                if utilize_path.exists():
                    utilize_path.unlink()
        
        metadata_content["notes"] = result["notes"]

        metadata_yml_path.write_text(yaml.dump(metadata_content, indent=2, sort_keys=False), encoding="utf-8")
        logging.info(f"Finished processing: {service_name} with status: {result['status']}")

        

    logging.info("Data population process finished.")

if __name__ == "__main__":
    main()
