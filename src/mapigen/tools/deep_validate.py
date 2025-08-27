from __future__ import annotations
import json
import sys
from pathlib import Path
import logging
from typing import Any

from mapigen.tools.utils import load_spec, get_params_from_operation, load_metadata

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def main():
    logging.info("Starting deep validation of all services...")
    project_root = Path(__file__).resolve().parent.parent.parent.parent
    data_root = project_root / "src" / "mapigen" / "data"
    service_dirs = [d for d in data_root.iterdir() if d.is_dir()]
    overall_status = 0

    for service_dir in service_dirs:
        service_name = service_dir.name
        logging.info(f"--- Validating service: {service_name} ---")

        try:
            utilize_path_lz4 = service_dir / f"{service_name}.utilize.json.lz4"
            utilize_path_json = service_dir / f"{service_name}.utilize.json"
            utilize_data: dict[str, Any]
            if utilize_path_lz4.exists():
                utilize_data = load_metadata(utilize_path_lz4)
            elif utilize_path_json.exists():
                utilize_data = json.loads(utilize_path_json.read_text())
            else:
                raise FileNotFoundError(f"No utilize file found for {service_name}")

            raw_spec_path = next(service_dir.glob(f"{service_name}.openapi.*"))
            raw_spec: dict[str, Any] = load_spec(raw_spec_path)
        except (FileNotFoundError, StopIteration) as e:
            logging.error(f"Could not find necessary files for validation: {e}")
            overall_status = 1
            continue

        reusable_components: dict[str, Any] = utilize_data.get("components", {}).get("parameters", {})
        operations: dict[str, Any] = utilize_data.get("operations", {})
        total_errors = 0

        for op_id, op_data_item in operations.items():
            op_data: dict[str, Any] = op_data_item
            # Find the original operation details in the raw spec to get its params
            original_op_details: dict[str, Any] | None = None
            original_path_params: list[dict[str, Any]] = []
            for methods_item in raw_spec.get("paths", {}).values():
                methods: dict[str, Any] = methods_item # Explicitly cast
                for details_item in methods.values():
                    details: dict[str, Any] = details_item # Explicitly cast
                    if details.get("operationId") == op_id:
                        original_op_details = details
                        original_path_params = methods.get("parameters", [])
                        break
                if original_op_details:
                    break
            
            if not original_op_details:
                logging.warning(f"Operation '{op_id}' found in utilize.json but not in raw spec. Skipping.")
                continue

            # Generate ground truth for this single operation using the canonical function
            ground_truth_params = get_params_from_operation(original_op_details, original_path_params, raw_spec)
            original_params_map = {f'{p["name"]}:{p["in"]}': p for p in ground_truth_params}

            for param_ref_item in op_data.get("parameters", []):
                param_ref: dict[str, Any] = param_ref_item
                if "$ref" not in param_ref:
                    continue
                
                fingerprint: str = param_ref["$ref"].split("/")[-1]
                canonical_param: dict[str, Any] | None = reusable_components.get(fingerprint)

                if not canonical_param:
                    logging.error(f"[{op_id}] Broken reference! Cannot find component for fingerprint '{fingerprint}'.")
                    total_errors += 1
                    continue

                param_key = f'{canonical_param["name"]}:{canonical_param["in"]}'
                original_param: dict[str, Any] | None = original_params_map.get(param_key)

                if not original_param:
                    logging.error(f"[{op_id}] Mismatch for '{param_key}'. Could not find original parameter to compare against.")
                    total_errors += 1
                    continue

                # Compare the canonical version against the original ground truth
                if canonical_param and original_param: # Add None check
                    for key, value in canonical_param.items():
                        if key not in original_param or original_param[key] != value:
                            logging.error(f"[{op_id}] Integrity mismatch for component '{param_key}' (Fingerprint: {fingerprint}) on key '{key}'!")
                            logging.error(f"  Canonical: {value}")
                            logging.error(f"  Original:  {original_param.get(key)}")
                            total_errors += 1

        if total_errors == 0:
            logging.info(f"SUCCESS: All component references in {service_name} are consistent.")
        else:
            logging.error(f"FAILURE: Found {total_errors} integrity issues for {service_name}.")
            overall_status = 1

    sys.exit(overall_status)

if __name__ == "__main__":
    main()