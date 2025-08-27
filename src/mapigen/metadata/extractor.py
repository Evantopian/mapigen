import json
import hashlib
from pathlib import Path
from typing import Any, Dict, List

from mapigen.tools.utils import get_params_from_operation, VALID_METHODS

def get_param_fingerprint(param: Dict[str, Any]) -> str:
    """Creates a stable, hashable fingerprint for a parameter dictionary."""
    fingerprint_data = {
        k: v for k, v in param.items() 
        if k not in ['example', 'examples']
    }
    return hashlib.sha256(json.dumps(fingerprint_data, sort_keys=True).encode()).hexdigest()

def extract_operations_and_components(service: str, spec: Dict[str, Any]) -> Dict[str, Any]:
    """
    Reduces an OpenAPI spec into a lightweight structure with genuinely reusable components,
    identified by a unique fingerprint of their properties.
    """
    canonical_params: Dict[str, Dict[str, Any]] = {}
    param_usage_count: Dict[str, int] = {}
    op_param_hashes: Dict[str, List[str]] = {}

    # 1. First pass: Discover all parameters, fingerprint them, and track usage
    for path, methods in spec.get("paths", {}).items():
        if not isinstance(methods, dict):
            continue
        path_level_params = methods.get("parameters", [])

        for method, details in methods.items():
            if method.lower() not in VALID_METHODS or not isinstance(details, dict):
                continue
            op_id = details.get("operationId")
            if not op_id:
                continue

            op_param_hashes[op_id] = []
            op_params = get_params_from_operation(details, path_level_params, spec)
            
            for param in op_params:
                fingerprint = get_param_fingerprint(param)
                op_param_hashes[op_id].append(fingerprint)

                if fingerprint not in canonical_params:
                    canonical_params[fingerprint] = param
                    param_usage_count[fingerprint] = 0
                param_usage_count[fingerprint] += 1

    # 2. Identify genuinely reusable components, keyed by their unique fingerprint
    reusable_components = {}
    for fingerprint, count in param_usage_count.items():
        if count > 1:
            reusable_components[fingerprint] = canonical_params[fingerprint]

    # 3. Build the final operations structure with appropriate $refs
    operations = {}
    for path, methods in spec.get("paths", {}).items():
        if not isinstance(methods, dict):
            continue
        for method, details in methods.items():
            if method.lower() not in VALID_METHODS or not isinstance(details, dict):
                continue
            op_id = details.get("operationId")
            if not op_id:
                continue

            final_params = []
            processed_fingerprints_in_op = set()

            for fingerprint in op_param_hashes.get(op_id, []):
                if fingerprint in processed_fingerprints_in_op:
                    continue
                processed_fingerprints_in_op.add(fingerprint)

                if fingerprint in reusable_components:
                    final_params.append({"$ref": f"#/$defs/parameters/{fingerprint}"})
                else:
                    final_params.append(canonical_params[fingerprint])
            
            operations[op_id] = {
                "service": service,
                "path": path,
                "method": method.upper(),
                "summary": details.get("summary", ""),
                "description": details.get("description", ""),
                "deprecated": details.get("deprecated", False),
                "parameters": final_params,
            }

    return {
        "components": {"parameters": reusable_components},
        "operations": operations
    }

def save_metadata(service: str, data: dict, out_dir: Path) -> Path:
    """
    Save extracted metadata into a utilize.json file.
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"{service}.utilize.json"
    path.write_text(json.dumps(data, indent=2))
    return path