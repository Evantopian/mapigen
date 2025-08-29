from __future__ import annotations
import sys
import time
import yaml
from pathlib import Path
import logging
from typing import Any, List, Dict

from tqdm import tqdm

from mapigen.tools.utils import load_spec, count_openapi_operations, resolve_parameter
from mapigen.cache.storage import load_service_from_disk
from mapigen.tools.populate_data import FORMAT_VERSION

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

# Define paths
ROOT_DIR = Path(__file__).resolve().parent.parent.parent.parent
DATA_DIR = ROOT_DIR / "src" / "mapigen" / "data"

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
        
        for param_ref in op_data.get("parameters", []):
            param_details = resolve_parameter(param_ref, data)
            if not param_details:
                errors.append(f"Operation '{op_id}' has a broken or malformed $ref: '{param_ref.get('$ref')}'")
            elif "$ref" not in param_ref:  # It was an inline parameter
                if not all(k in param_details for k in ["name", "in", "type"]):
                    errors.append(f"Inline parameter in '{op_id}' is missing one of [name, in, type].")
    return errors

def generate_report(results: List[Dict[str, Any]], total_duration: float):
    """Generates and prints a performance report."""
    successful_services = [r for r in results if r["status"] == "success"]
    failed_services = [r for r in results if r["status"] == "failure"]

    print("\n--- Validation Report ---")
    print(f"Total execution time: {total_duration:.2f}s")
    print(f"Services validated: {len(results)}")
    print(f"  Success: {len(successful_services)}")
    print(f"  Failures: {len(failed_services)}")

    if results:
        avg_total_time = sum(r['duration'] for r in results) / len(results)
        print(f"Avg time per service: {avg_total_time:.2f}s")
    print("-------------------------")

def main():
    """Main validation function."""
    logging.info("Starting validation of data files...")
    overall_start_time = time.perf_counter()

    service_dirs: list[Path] = [d for d in DATA_DIR.iterdir() if d.is_dir()]
    if not service_dirs:
        logging.warning("No service data found to validate.")
        return

    total_success: int = 0
    total_failure: int = 0
    results: List[Dict[str, Any]] = []

    for service_dir in tqdm(service_dirs, desc="Validating Services"):
        service_name: str = service_dir.name
        service_start_time = time.perf_counter()
        failures: list[str] = []
        
        try:
            # 1. Check for metadata.yml
            metadata_path: Path = service_dir / "metadata.yml"
            if not metadata_path.exists():
                failures.append("Missing metadata.yml file.")
            else:
                metadata: dict[str, Any] = yaml.safe_load(metadata_path.read_text())
                if metadata.get("format_version") != FORMAT_VERSION:
                    failures.append(f"Incorrect format_version in metadata.yml (expected {FORMAT_VERSION}).")

            # 2. Check for processed data and its integrity
            processed_data = load_service_from_disk(service_name)
            integrity_errors: list[str] = validate_operations_and_refs(processed_data, service_name)
            if integrity_errors:
                failures.extend(integrity_errors)

            # 3. Compare operation counts with raw spec
            raw_spec_files: list[Path] = list(service_dir.glob(f"{service_name}.openapi.*{''}"))
            if not raw_spec_files:
                logging.warning(f"[{service_name}] No raw OpenAPI spec file found. Skipping op count comparison.")
            else:
                raw_spec: dict[str, Any] = load_spec(raw_spec_files[0])
                raw_op_count = count_openapi_operations(raw_spec)
                processed_op_count: int = len(processed_data.get("operations", {}))
                if raw_op_count != processed_op_count:
                    failures.append(f"Op count mismatch: Raw spec {raw_op_count}, processed {processed_op_count}.")

            if failures:
                raise ValueError(", ".join(failures))

            results.append({"service_name": service_name, "status": "success", "duration": time.perf_counter() - service_start_time})
            total_success += 1

        except Exception as e:
            logging.error(f"Validation failed for {service_name}: {e}")
            results.append({"service_name": service_name, "status": "failure", "duration": time.perf_counter() - service_start_time})
            total_failure += 1

    total_duration = time.perf_counter() - overall_start_time
    generate_report(results, total_duration)

    if total_failure > 0:
        sys.exit(1)

if __name__ == "__main__":
    main()