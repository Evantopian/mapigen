import argparse
import sys
import time
import logging
import traceback
from pathlib import Path
from typing import Any, cast, Mapping, List, Dict

import msgspec
from tqdm import tqdm
from openapi_spec_validator import validate_spec

from mapigen.models import Operation, Parameter, ParameterRef
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
    parser = argparse.ArgumentParser(description="Deep validate service data.")
    parser.add_argument("service_key", nargs='?', help="Optional: The specific service key (e.g., provider:api:source) to validate.")
    args = parser.parse_args()

    logging.info("Starting deep validation...")
    overall_start_time = time.perf_counter()
    
    data_root = Path(__file__).resolve().parent.parent.parent.parent / "src" / "mapigen" / "data"
    
    if args.service_key:
        try:
            provider, api, source = args.service_key.split(":")
            processed_files = [data_root / provider / source / api / f"{api}.utilize.json.zst"]
            if not processed_files[0].exists():
                logging.error(f"Service '{args.service_key}' not found at {processed_files[0]}.")
                sys.exit(1)
        except ValueError:
            logging.error(f"Invalid service key format: '{args.service_key}'. Expected 'provider:api:source'.")
            sys.exit(1)
    else:
        processed_files = list(data_root.glob("**/*.utilize.json.zst"))
    
    if not processed_files:
        logging.warning("No processed data found to validate.")
        return

    overall_status = 0
    results: List[Dict[str, Any]] = []

    for processed_path in tqdm(processed_files, desc="Deep Validating Services"):
        api_name = processed_path.parent.name
        source_name = processed_path.parent.parent.name
        provider_name = processed_path.parent.parent.parent.name
        service_key = f"{provider_name}:{api_name}:{source_name}"

        service_start_time = time.perf_counter()
        metrics: Dict[str, Any] = {
            "service_key": service_key,
            "status": "success",
            "spec_validation_duration": 0,
            "deep_check_duration": 0,
        }

        try:
            # 1. Raw Spec Validation
            t_spec_val_start = time.perf_counter()
            raw_spec_path = processed_path.parent / f"{api_name}.openapi.json.zst"
            raw_spec: dict[str, Any] = load_spec(raw_spec_path)
            validate_spec(cast(Mapping[Any, Any], raw_spec))
            metrics["spec_validation_duration"] = time.perf_counter() - t_spec_val_start

            # 2. Deep Integrity Checks
            t_deep_check_start = time.perf_counter()
            utilize_data = load_service_from_disk(processed_path)
            reusable_components: dict[str, Parameter] = utilize_data.components.parameters
            operations: dict[str, Operation] = utilize_data.operations
            total_errors = 0

            for op_id, op_data in operations.items():
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
                    logging.warning(f"[{service_key}] Operation '{op_id}' not in raw spec. Skipping.")
                    continue

                ground_truth_params = get_params_from_operation(original_op_details, original_path_params, raw_spec)
                original_params_map = {f'{p.name}:{p.in_}': p for p in ground_truth_params}

                for param in op_data.parameters:
                    if not isinstance(param, ParameterRef):
                        continue
                    
                    component_name: str = param.component_name
                    canonical_param: Parameter | None = reusable_components.get(component_name)

                    if not canonical_param:
                        logging.error(f"[{op_id}] Broken reference for component '{component_name}'.")
                        total_errors += 1
                        continue

                    param_key = f'{canonical_param.name}:{canonical_param.in_}'
                    original_param: Parameter | None = original_params_map.get(param_key)

                    if not original_param:
                        logging.error(f"[{op_id}] Mismatch for '{param_key}'. Original param not found.")
                        total_errors += 1
                        continue

                    canonical_param_dict = msgspec.to_builtins(canonical_param)
                    original_param_dict = msgspec.to_builtins(original_param)

                    for key, value in canonical_param_dict.items():
                        if key not in original_param_dict or original_param_dict[key] != value:
                            logging.error(f"[{op_id}] Integrity mismatch for '{param_key}' on key '{key}'!")
                            total_errors += 1
            
            metrics["deep_check_duration"] = time.perf_counter() - t_deep_check_start
            if total_errors > 0:
                raise ValueError(f"Found {total_errors} integrity issues.")

        except Exception:
            logging.error(f"Validation failed for {service_key}:")
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