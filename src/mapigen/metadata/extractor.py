from __future__ import annotations
import orjson as json
import hashlib
from pathlib import Path
from typing import Any, Optional, cast

from mapigen.tools.utils import get_params_from_operation, VALID_METHODS

def get_param_fingerprint(param: dict[str, Any]) -> str:
    """Creates a stable, hashable fingerprint for a parameter dictionary."""
    fingerprint_data = {
        k: v for k, v in param.items() 
        if k not in ['example', 'examples']
    }
    return hashlib.sha256(json.dumps(fingerprint_data)).hexdigest()

def extract_operations_and_components(service: str, spec: dict[str, Any]) -> dict[str, Any]:
    """
    Reduces an OpenAPI spec into a lightweight structure with genuinely reusable components,
    identified by a unique fingerprint of their properties.
    """
    canonical_params: dict[str, dict[str, Any]] = {}
    param_usage_count: dict[str, int] = {}
    op_param_hashes: dict[str, list[str]] = {}

    # 1. First pass: Discover all parameters, fingerprint them, and track usage
    for path, methods_dict in spec.get("paths", {}).items():
        if not isinstance(methods_dict, dict):
            continue
        methods_dict = cast(dict[str, Any], methods_dict)
        path_level_params: list[dict[str, Any]] = methods_dict.get("parameters", [])

        for method, details_dict in methods_dict.items():
            method: str
            details_dict: dict[str, Any]
            if method.lower() not in VALID_METHODS:
                continue
            op_id: Optional[str] = details_dict.get("operationId")
            if not op_id:
                continue

            op_param_hashes[op_id] = []
            op_params: list[dict[str, Any]] = get_params_from_operation(details_dict, path_level_params, spec)
            
            for param in op_params:
                fingerprint = get_param_fingerprint(param)
                op_param_hashes[op_id].append(fingerprint)

                if fingerprint not in canonical_params:
                    canonical_params[fingerprint] = param
                    param_usage_count[fingerprint] = 0
                param_usage_count[fingerprint] += 1

    # 2. Identify genuinely reusable components, keyed by their unique fingerprint
    reusable_components: dict[str, dict[str, Any]] = {}
    for fingerprint, count in param_usage_count.items():
        if count > 1:
            reusable_components[fingerprint] = canonical_params[fingerprint]

    # 3. Build the final operations structure with appropriate $refs
    operations: dict[str, dict[str, Any]] = {}
    for path, methods_dict in spec.get("paths", {}).items():
        if not isinstance(methods_dict, dict):
            continue
        methods_dict = cast(dict[str, Any], methods_dict)
        for method, details_dict in methods_dict.items():
            method: str
            details_dict: dict[str, Any]
            if method.lower() not in VALID_METHODS:
                continue
            op_id = details_dict.get("operationId")
            if not op_id:
                continue

            final_params: list[dict[str, Any]] = []
            processed_fingerprints_in_op: set[str] = set()

            for fingerprint in op_param_hashes.get(op_id, []):
                if fingerprint in processed_fingerprints_in_op:
                    continue
                processed_fingerprints_in_op.add(fingerprint)

                if fingerprint in reusable_components:
                    final_params.append({"$ref": f"#/$defs/parameters/{fingerprint}"})
                else:
                    param_details = canonical_params[fingerprint]
                    if 'type' not in param_details:
                        param_details['type'] = 'object' # Defaulting to object, can be refined
                    final_params.append(param_details)
            
            operations[op_id] = {
                "service": service,
                "path": path,
                "method": method.upper(),
                "summary": details_dict.get("summary", ""),
                "description": details_dict.get("description", ""),
                "deprecated": details_dict.get("deprecated", False),
                "parameters": final_params,
            }

    return {
        "components": {"parameters": reusable_components},
        "operations": operations
    }

def save_metadata(service: str, data: dict[str, Any], out_dir: Path) -> Path:
    """
    Save extracted metadata into a utilize.json file.
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"{service}.utilize.json"
    path.write_text(json.dumps(data, option=json.OPT_INDENT_2).decode("utf-8"))
    return path