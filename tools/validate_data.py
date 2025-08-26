import json
import sys
from pathlib import Path
import logging

# Add the src directory to the Python path
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root / "src"))

from mapigen.metadata.utils import load_spec

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

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

        openapi_path = service_dir / f"{service_name}.openapi.json"
        utilize_path = service_dir / f"{service_name}.utilize.json"

        if not openapi_path.exists() or not utilize_path.exists():
            logging.error(f"Missing openapi.json or utilize.json for {service_name}. Skipping.")
            failure_count += 1
            continue

        try:
            # Load files
            raw_spec = load_spec(openapi_path)
            utilize_data = json.loads(utilize_path.read_text())

            raw_count = count_openapi_operations(raw_spec)
            utilize_count = len(utilize_data)

            if raw_count == utilize_count:
                logging.info(f"SUCCESS: Operation count matches ({raw_count} operations).")
                success_count += 1
            else:
                logging.error(f"FAILURE: Mismatch! openapi.json has {raw_count} operations, but utilize.json has {utilize_count}.")
                failure_count += 1
        
        except Exception as e:
            logging.error(f"An error occurred while processing {service_name}: {e}")
            failure_count += 1

    logging.info("===")
    logging.info(f"Validation Complete. Success: {success_count}, Failures: {failure_count}.")
    logging.info("===")

if __name__ == "__main__":
    main()
