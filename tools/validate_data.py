import json
import sys
from pathlib import Path
import logging
import glob

# Add the src directory to the Python path
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root / "src"))

from mapigen.metadata.utils import load_spec
from mapigen.metadata.loader import load_metadata

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

# Define paths
ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "src" / "mapigen" / "data"

VALID_METHODS = {"get", "put", "post", "delete", "options", "head", "patch", "trace"}

def count_openapi_operations(spec: dict) -> int:
    """Counts the number of operations in a raw OpenAPI spec."""
    count = 0
    for path_data in spec.get('paths', {}).values():
        if isinstance(path_data, dict):
            for method in path_data.keys():
                if method.lower() in VALID_METHODS:
                    count += 1
    return count

def main():
    """Main validation function."""
    logging.info("Starting validation of data files...")
    
    service_dirs = [d for d in DATA_DIR.iterdir() if d.is_dir()]
    if not service_dirs:
        logging.warning("No service data found to validate.")
        return

    success_count = 0
    failure_count = 0

    for service_dir in service_dirs:
        service_name = service_dir.name
        logging.info(f"---")
        logging.info(f"Validating service: {service_name}")

        # Find the raw spec file, which could be .json or .yml
        raw_spec_files = list(service_dir.glob(f"{service_name}.openapi.*"))
        if not raw_spec_files:
            logging.error(f"No raw OpenAPI spec file found for {service_name}. Skipping.")
            failure_count += 1
            continue
        openapi_path = raw_spec_files[0]

        # Path to the compressed utilize file
        utilize_path = service_dir / f"{service_name}.utilize.json.lz4"

        if not openapi_path.exists() or not utilize_path.exists():
            logging.error(f"Missing spec or processed metadata file for {service_name}. Skipping.")
            failure_count += 1
            continue

        try:
            # Load files (load_metadata handles decompression)
            raw_spec = load_spec(openapi_path)
            utilize_data = load_metadata(utilize_path)

            # Count operations
            raw_count = count_openapi_operations(raw_spec)
            utilize_count = len(utilize_data)

            # Compare and report
            if raw_count == utilize_count:
                logging.info(f"SUCCESS: Operation count matches ({raw_count} operations).")
                success_count += 1
            else:
                logging.error(f"FAILURE: Mismatch! Raw spec has {raw_count} operations, but processed data has {utilize_count}.")
                failure_count += 1
        
        except Exception as e:
            logging.error(f"An error occurred while processing {service_name}: {e}", exc_info=True)
            failure_count += 1

    logging.info("===")
    logging.info(f"Validation Complete. Success: {success_count}, Failures: {failure_count}.")
    logging.info("===")

if __name__ == "__main__":
    main()
