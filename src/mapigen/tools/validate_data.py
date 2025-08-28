from __future__ import annotations
import sys
import yaml
from pathlib import Path
import logging
from typing import Any, Optional

from mapigen.tools.utils import load_spec, count_openapi_operations
from mapigen.cache.storage import load_service_from_disk
from mapigen.tools.populate_data import FORMAT_VERSION    
# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

# Define paths
ROOT_DIR = Path(__file__).resolve().parent.parent.parent.parent
DATA_DIR = ROOT_DIR / "src" / "mapigen" / "data"

VALID_METHODS = {"get", "put", "post", "delete", "options", "head", "patch", "trace"}



def validate_operations_and_refs(data: dict[str, Any], service_name: str) -> list[str]:
    """Validates the integrity of operations and their parameter references."""
    errors: list[str] = []
    operations = data.get("operations", {})
    components = data.get("components", {}).get("parameters", {})

    if not operations:
        errors.append("No 'operations' block found.")
    if not components:
        logging.warning(f"[{service_name}] No reusable 'components' found. This may be expected.")

    for op_id, op_data in operations.items():
        if not all(k in op_data for k in ["service", "path", "method", "parameters"]):
            errors.append(f"Operation '{op_id}' is missing one of [service, path, method, parameters].")
        
        for param in op_data.get("parameters", []):
            if "$ref" in param:
                ref_path = param["$ref"]
                if not ref_path.startswith("#/$defs/parameters/"):
                    errors.append(f"Operation '{op_id}' has a malformed $ref: '{ref_path}'.")
                else:
                    component_name = ref_path.split("/")[-1]
                    if component_name not in components:
                        errors.append(f"Operation '{op_id}' has a broken $ref: '{ref_path}'.")
            elif not all(k in param for k in ["name", "in", "type"]):
                errors.append(f"Inline parameter in '{op_id}' is missing one of [name, in, type].")
    return errors

def main():
    """Main validation function."""
    logging.info("Starting validation of data files...")

    service_dirs: list[Path] = [d for d in DATA_DIR.iterdir() if d.is_dir()]
    if not service_dirs:
        logging.warning("No service data found to validate.")
        return

    total_success: int = 0
    total_failure: int = 0

    for service_dir in service_dirs:
        service_name: str = service_dir.name
        logging.info("---")
        logging.info(f"Validating service: {service_name}")
        
        failures: list[str] = []
        processed_data: Optional[dict[str, Any]] = None

        # Check for metadata.yml
        metadata_path: Path = service_dir / "metadata.yml"
        if not metadata_path.exists():
            failures.append("Missing metadata.yml file.")
        else:
            metadata: dict[str, Any] = yaml.safe_load(metadata_path.read_text())
            if metadata.get("format_version") != FORMAT_VERSION:
                failures.append(f"Incorrect format_version in metadata.yml (expected {FORMAT_VERSION}).")

        try:
            processed_data = load_service_from_disk(service_name)
        except FileNotFoundError:
            failures.append("Missing processed utilize file (.json or .json.lz4).")

        # Find raw spec file for comparison
        raw_spec_files: list[Path] = list(service_dir.glob(f"{service_name}.openapi.*"))
        if not raw_spec_files:
            logging.warning("No raw OpenAPI spec file found. Skipping operation count comparison.")
            raw_op_count: int = -1 # Sentinel value
        else:
            raw_spec: dict[str, Any] = load_spec(raw_spec_files[0])
            raw_spec_typed: dict[str, Any] = raw_spec # Explicitly cast
            raw_op_count = count_openapi_operations(raw_spec_typed)

        if processed_data:
            # 1. Validate data integrity and references
            integrity_errors: list[str] = validate_operations_and_refs(processed_data, service_name)
            if integrity_errors:
                failures.extend(integrity_errors)
            else:
                logging.info("Data integrity and reference checks passed.")

            # 2. Compare operation counts
            processed_op_count: int = len(processed_data.get("operations", {}))
            if raw_op_count != -1 and raw_op_count != processed_op_count:
                failures.append(f"Operation count mismatch: Raw spec has {raw_op_count}, processed has {processed_op_count}.")
            elif raw_op_count != -1:
                logging.info(f"Operation count matches ({processed_op_count} operations).")

        if failures:
            for f in failures:
                logging.error(f"FAILURE: {f}")
            total_failure += 1
        else:
            logging.info(f"SUCCESS: All checks passed for {service_name}.")
            total_success += 1

    logging.info("===")
    logging.info(f"Validation Complete. Success: {total_success}, Failures: {total_failure}.")
    logging.info("===")

    if total_failure > 0:
        sys.exit(1)

if __name__ == "__main__":
    main()
