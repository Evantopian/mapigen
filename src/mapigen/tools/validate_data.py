from __future__ import annotations
import sys
import time
from pathlib import Path
import logging
from typing import Any, List, Dict

import msgspec
from tqdm import tqdm

from mapigen.models import ServiceData, Parameter, ParameterRef
from mapigen.tools.utils import load_spec, count_openapi_operations
from mapigen.cache.storage import load_service_from_disk
from mapigen.tools.populate_data import FORMAT_VERSION

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

# Define paths
ROOT_DIR = Path(__file__).resolve().parent.parent.parent.parent
DATA_DIR = ROOT_DIR / "src" / "mapigen" / "data"

def validate_operations_and_refs(data: ServiceData, service_key: str) -> list[str]:
    """Validates the integrity of operations and their parameter references."""
    errors: list[str] = []
    operations = data.operations
    components = data.components.parameters

    if not operations:
        errors.append(f"[{service_key}] No 'operations' block found.")
    if not components:
        logging.warning(f"[{service_key}] No reusable 'components' found. This may be expected.")

    for op_id, op_data in operations.items():
        if not all([op_data.service, op_data.path, op_data.method, op_data.parameters is not None]):
            errors.append(f"[{service_key}] Operation '{op_id}' is missing one of [service, path, method, parameters].")
        
        for param in op_data.parameters:
            if isinstance(param, ParameterRef):
                if param.component_name not in components:
                    errors.append(f"[{service_key}] Operation '{op_id}' has a broken $ref: '{param.ref}'")
            elif isinstance(param, Parameter):
                if not all([param.name, param.in_, param.schema_]):
                    errors.append(f"[{service_key}] Inline parameter in '{op_id}' is missing one of [name, in, schema].")
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

    processed_files = list(DATA_DIR.glob("**/*.utilize.json.zst"))
    if not processed_files:
        logging.warning("No processed data found to validate.")
        return

    total_success, total_failure = 0, 0
    results: List[Dict[str, Any]] = []

    for processed_path in tqdm(processed_files, desc="Validating Services"):
        service_start_time = time.perf_counter()
        failures: list[str] = []
        api_name = processed_path.parent.name
        source_name = processed_path.parent.parent.name
        provider_name = processed_path.parent.parent.parent.name
        service_key = f"{provider_name}:{api_name}:{source_name}"

        try:
            metadata_path = processed_path.parent / "metadata.yml"
            if not metadata_path.exists():
                failures.append("Missing metadata.yml file.")
            else:
                metadata = msgspec.yaml.decode(metadata_path.read_text())
                if metadata.get("format_version") != FORMAT_VERSION:
                    failures.append(f"Incorrect format_version in metadata.yml (expected {FORMAT_VERSION}).")

            processed_data = load_service_from_disk(processed_path)
            integrity_errors = validate_operations_and_refs(processed_data, service_key)
            failures.extend(integrity_errors)

            raw_spec_path = processed_path.parent / f"{api_name}.openapi.json.zst"
            if not raw_spec_path.exists():
                raw_spec_path = raw_spec_path.with_suffix(".json")
            
            if not raw_spec_path.exists():
                logging.warning(f"[{service_key}] No raw OpenAPI spec file found. Skipping op count comparison.")
            else:
                raw_spec = load_spec(raw_spec_path)
                raw_op_count = count_openapi_operations(raw_spec)
                processed_op_count = len(processed_data.operations)
                if raw_op_count != processed_op_count:
                    failures.append(f"Op count mismatch: Raw spec {raw_op_count}, processed {processed_op_count}.")

            if failures:
                raise ValueError(", ".join(failures))

            results.append({"service_key": service_key, "status": "success", "duration": time.perf_counter() - service_start_time})
            total_success += 1

        except Exception as e:
            logging.error(f"Validation failed for {service_key}: {e}")
            results.append({"service_key": service_key, "status": "failure", "duration": time.perf_counter() - service_start_time})
            total_failure += 1

    total_duration = time.perf_counter() - overall_start_time
    generate_report(results, total_duration)

    if total_failure > 0:
        sys.exit(1)

if __name__ == "__main__":
    main()
