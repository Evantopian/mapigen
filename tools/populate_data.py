import json
import sys
import argparse
import yaml
import shutil
import hashlib
from pathlib import Path
import logging
from datetime import datetime, timezone

# Add the src directory to the Python path
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root / "src"))

from mapigen.metadata.fetcher import fetch_spec
from mapigen.metadata.converter import normalize_spec
from mapigen.metadata.extractor import extract_operations_and_components, save_metadata
from mapigen.metadata.loader import compress_metadata

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define paths
ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "src" / "mapigen" / "data"
REGISTRY_DIR = ROOT_DIR / "src" / "mapigen" / "registry"
CUSTOM_SOURCES_PATH = REGISTRY_DIR / "custom_sources.json"
GITHUB_SOURCES_PATH = REGISTRY_DIR / "github_sources.json"

def process_service(service_name, url, service_data_dir, keep_raw_specs, no_compress):
    """
    Fetches, normalizes, and extracts metadata for a single service.
    """
    raw_spec_path = None
    utilize_path = None
    try:
        # Clean the specific service directory before processing
        logging.info(f"Cleaning service directory: {service_data_dir}")
        if service_data_dir.exists():
            shutil.rmtree(service_data_dir)
        service_data_dir.mkdir(parents=True)

        logging.info(f"Processing service: {service_name}")

        # 1. Fetch spec
        logging.info(f"Fetching spec from {url}...")
        raw_spec_path = fetch_spec(service_name, url, service_data_dir)
        logging.info(f"Spec saved to {raw_spec_path}")

        # 2. Calculate hash of the raw spec
        raw_content = raw_spec_path.read_bytes()
        api_hash = hashlib.sha256(raw_content).hexdigest()

        # 3. Normalize and validate spec
        logging.info("Normalizing and validating spec...")
        normalized_spec = normalize_spec(raw_spec_path)
        logging.info("Spec validation successful.")

        # 4. Extract lightweight metadata
        logging.info("Extracting lightweight 'utilize' metadata...")
        processed_data = extract_operations_and_components(service_name, normalized_spec)
        op_count = len(processed_data['operations'])
        param_count = len(processed_data['components']['parameters'])
        logging.info(f"Extracted {op_count} operations and {param_count} reusable parameters.")

        # 5. Create metadata.yml
        now_utc = datetime.now(timezone.utc).isoformat()
        metadata_content = {
            "format_version": 2,
            "first_accessed": now_utc,
            "api_reference": url,
            "api_hash": api_hash,
            "operation_count": op_count,
            "reusable_parameter_count": param_count,
            "notes": ""
        }
        metadata_yml_path = service_data_dir / "metadata.yml"
        metadata_yml_path.write_text(yaml.dump(metadata_content, indent=2), encoding="utf-8")
        logging.info(f"Saved service metadata to {metadata_yml_path}")

        # 6. Save extracted metadata
        utilize_path = save_metadata(service_name, processed_data, service_data_dir)
        logging.info(f"Saved 'utilize' metadata to {utilize_path}")

        # 7. Compress metadata (optional)
        if not no_compress:
            logging.info(f"Compressing metadata file: {utilize_path}")
            compress_metadata(utilize_path)
            logging.info(f"Compressed metadata and deleted intermediate file.")
            if utilize_path.exists():
                utilize_path.unlink()

    except Exception as e:
        logging.error(f"Failed to process service {service_name}: {e}", exc_info=True)
    finally:
        # 8. Clean up raw spec file (optional)
        if not keep_raw_specs and raw_spec_path and raw_spec_path.exists():
            logging.info(f"Deleting raw spec file: {raw_spec_path}")
            raw_spec_path.unlink()

def main():
    """
    Main function to orchestrate the data population process.
    """
    parser = argparse.ArgumentParser(description="Fetch and process API specifications.")
    parser.add_argument(
        "--keep-raw-specs",
        action="store_true",
        help="If set, the original downloaded OpenAPI spec files will not be deleted after processing."
    )
    parser.add_argument(
        "--no-compress",
        action="store_true",
        help="If set, the final utilize.json file will not be compressed."
    )
    args = parser.parse_args()

    logging.info("Starting data population process...")
    if args.keep_raw_specs:
        logging.info("Raw specification files will be kept.")
    if args.no_compress:
        logging.info("Compression is disabled.")

    # Ensure the root data directory exists
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    # Load sources
    all_sources = {}
    if CUSTOM_SOURCES_PATH.exists():
        all_sources.update(json.loads(CUSTOM_SOURCES_PATH.read_text()))
    if GITHUB_SOURCES_PATH.exists():
        all_sources.update(json.loads(GITHUB_SOURCES_PATH.read_text()))

    if not all_sources:
        logging.warning("No sources found in registry. Exiting.")
        return

    logging.info(f"Found {len(all_sources)} services to process.")

    for service_name, url in all_sources.items():
        service_data_dir = DATA_DIR / service_name
        process_service(service_name, url, service_data_dir, args.keep_raw_specs, args.no_compress)

    logging.info("Data population process finished.")

if __name__ == "__main__":
    main()
