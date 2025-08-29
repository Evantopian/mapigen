from __future__ import annotations
import sys
import time
import logging
import traceback
from pathlib import Path
from typing import Any, cast, Mapping, List, Dict

from tqdm import tqdm
from openapi_spec_validator import validate_spec

from mapigen.tools.utils import load_spec, get_params_from_operation
from mapigen.cache.storage import load_service_from_disk

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def generate_report(results: List[Dict[str, Any]], total_duration: float):
    """Generates and prints a performance report."""
    successful_services = [r for r in results if r["status"] == "success"]
    failed_services = [r for r in results if r["status"] == "failure"]

    print("\n--- Deep Validation Report ---")
    print(f"Total execution time: {total_duration:.2f}s")
    print(f"Services validated: {len(results)}")
    print(f"  Success: {len(successful_services)}")
    print(f"  Failures: {len(failed_services)}")

    if results:
        avg_total_time = sum(r['total_duration'] for r in results) / len(results)
        avg_spec_validation_time = sum(r['spec_validation_duration'] for r in results) / len(results)
        avg_deep_check_time = sum(r['deep_check_duration'] for r in results) / len(results)
        print(f"Avg time per service: {avg_total_time:.2f}s")
        print(f"  Avg spec validation time: {avg_spec_validation_time:.2f}s")
        print(f"  Avg deep check time: {avg_deep_check_time:.2f}s")
    print("-----------------------------")

def main():
    """Main deep validation function."""
    logging.info("Starting deep validation of all services...")
    overall_start_time = time.perf_counter()
    
    project_root = Path(__file__).resolve().parent.parent.parent.parent
    data_root = project_root / "src" / "mapigen" / "data"
    service_dirs = [d for d in data_root.iterdir() if d.is_dir()]
    
    if not service_dirs:
        logging.warning("No service data found to validate.")
        return

    overall_status = 0
    results: List[Dict[str, Any]] = []

    for service_dir in tqdm(service_dirs, desc="Deep Validating Services"):
        service_name = service_dir.name
        service_start_time = time.perf_counter()
        metrics: Dict[str, Any] = {
            "service_name": service_name,
            "status": "success",
            "spec_validation_duration": 0,
            "deep_check_duration": 0,
        }

        try:
            # 1. Raw Spec Validation
            t_spec_val_start = time.perf_counter()
            raw_spec_path = next(service_dir.glob(f"{service_name}.openapi.*"))
            raw_spec: dict[str, Any] = load_spec(raw_spec_path)
            validate_spec(cast(Mapping[Any, Any], raw_spec))
            metrics["spec_validation_duration"] = time.perf_counter() - t_spec_val_start

            # 2. Deep Integrity Checks
            t_deep_check_start = time.perf_counter()
            utilize_data = load_service_from_disk(service_name)
            reusable_components: dict[str, Any] = utilize_data.get("components", {}).get("parameters", {})
            operations: dict[str, Any] = utilize_data.get("operations", {})
            total_errors = 0

            for op_id, op_data_item in operations.items():
                op_data: dict[str, Any] = op_data_item
                original_op_details: dict[str, Any] | None = None
                original_path_params: list[dict[str, Any]] = []
                for methods_item in raw_spec.get("paths", {}).values():
                    methods: dict[str, Any] = methods_item
                    for details_item in methods.values():
                        if isinstance(details_item, dict):
                            details: dict[str, Any] = cast(dict[str, Any], details_item)
                            if details.get("operationId") == op_id:
                                original_op_details = details
                                original_path_params = methods.get("parameters", [])
                                break
                    if original_op_details:
                        break
                
                if not original_op_details:
                    logging.warning(f"[{service_name}] Operation '{op_id}' not in raw spec. Skipping.")
                    continue

                ground_truth_params = get_params_from_operation(original_op_details, original_path_params, raw_spec)
                original_params_map = {f'{p["name"]}:{p["in"]}': p for p in ground_truth_params}

                for param_ref_item in op_data.get("parameters", []):
                    param_ref: dict[str, Any] = param_ref_item
                    if "$ref" not in param_ref:
                        continue
                    
                    fingerprint: str = param_ref["$ref"].split("/")[-1]
                    canonical_param: dict[str, Any] | None = reusable_components.get(fingerprint)

                    if not canonical_param:
                        logging.error(f"[{op_id}] Broken reference for fingerprint '{fingerprint}'.")
                        total_errors += 1
                        continue

                    param_key = f'{canonical_param["name"]}:{canonical_param["in"]}'
                    original_param: dict[str, Any] | None = original_params_map.get(param_key)

                    if not original_param:
                        logging.error(f"[{op_id}] Mismatch for '{param_key}'. Original param not found.")
                        total_errors += 1
                        continue

                    for key, value in canonical_param.items():
                        if key not in original_param or original_param[key] != value:
                            logging.error(f"[{op_id}] Integrity mismatch for '{param_key}' on key '{key}'!")
                            total_errors += 1
            
            metrics["deep_check_duration"] = time.perf_counter() - t_deep_check_start
            if total_errors > 0:
                raise ValueError(f"Found {total_errors} integrity issues.")

        except Exception:
            logging.error(f"Validation failed for {service_name}:")
            traceback.print_exc()
            metrics["status"] = "failure"
            overall_status = 1
        
        metrics["total_duration"] = time.perf_counter() - service_start_time
        results.append(metrics)

    total_duration = time.perf_counter() - overall_start_time
    generate_report(results, total_duration)

    sys.exit(overall_status)

if __name__ == "__main__":
    main()