from __future__ import annotations
import hashlib
import collections
from pathlib import Path
from typing import Any

import msgspec

from mapigen.tools.utils import get_params_from_operation, VALID_METHODS


def get_param_fingerprint(param: dict[str, Any]) -> str:
    """Creates a stable, hashable fingerprint for a parameter dictionary."""
    # Ignore volatile/example fields to ensure stable fingerprinting
    fingerprint_data = {k: v for k, v in param.items() if k not in ("example", "examples")}
    return hashlib.sha256(msgspec.json.encode(fingerprint_data)).hexdigest()


def extract_operations_and_components(service: str, spec: dict[str, Any]) -> dict[str, Any]:
    """
    Reduces an OpenAPI spec into a lightweight structure with all unique parameters
    as components, identified by a unique fingerprint of their properties.
    """
    paths = spec.get("paths", {})
    if not isinstance(paths, dict):
        return {"components": {"parameters": {}}, "operations": {}}

    canonical_params: dict[str, dict[str, Any]] = {}
    operations: dict[str, dict[str, Any]] = {}
    fingerprint_counts = collections.Counter()

    # Single pass: Process all operations and collect parameter data
    for path, methods_dict in paths.items():
        if not isinstance(methods_dict, dict):
            continue

        path_level_params = methods_dict.get("parameters", [])
        
        for method, details_dict in methods_dict.items():
            if method.lower() not in VALID_METHODS or not isinstance(details_dict, dict):
                continue

            op_id = details_dict.get("operationId")
            if not op_id:
                continue

            op_params = get_params_from_operation(details_dict, path_level_params, spec)
            final_params = []
            seen_fingerprints = set()

            for param in op_params:
                param_dict = msgspec.to_builtins(param)
                fingerprint = get_param_fingerprint(param_dict)
                
                if fingerprint in seen_fingerprints:
                    continue
                seen_fingerprints.add(fingerprint)

                fingerprint_counts[fingerprint] += 1
                if fingerprint not in canonical_params:
                    canonical_params[fingerprint] = param_dict

                final_params.append({
                    "type": "ref",
                    "$ref": f"#/components/parameters/{fingerprint}"
                })

            operations[op_id] = {
                "service": service,
                "path": path,
                "method": method.upper(),
                "summary": details_dict.get("summary", ""),
                "description": details_dict.get("description", ""),
                "deprecated": details_dict.get("deprecated", False),
                "parameters": final_params,
            }
    reusable_parameter_count = sum(1 for count in fingerprint_counts.values() if count > 1)

    all_params_with_type = {
        fp: {**param, "type": "inline"}
        for fp, param in canonical_params.items()
    }

    schemas = spec.get("components", {}).get("schemas", {})

    return {
        "components": {"parameters": all_params_with_type, "schemas": schemas},
        "operations": operations,
        "reusable_param_count": reusable_parameter_count,
    }


def save_metadata(service: str, data: dict[str, Any], out_dir: Path) -> Path:
    """
    Save extracted metadata into a utilize.json file.
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"{service}.utilize.json"
    path.write_bytes(msgspec.json.encode(data))
    return path