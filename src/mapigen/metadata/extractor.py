from __future__ import annotations
import hashlib
from pathlib import Path
from typing import Any, Optional

import msgspec

from mapigen.tools.utils import get_params_from_operation, VALID_METHODS


def get_param_fingerprint(param: dict[str, Any]) -> str:
    """Creates a stable, hashable fingerprint for a parameter dictionary."""
    # Ignore volatile/example fields to ensure stable fingerprinting
    fingerprint_data = {k: v for k, v in param.items() if k not in ("example", "examples")}
    return hashlib.sha256(msgspec.json.encode(fingerprint_data)).hexdigest()


def extract_operations_and_components(service: str, spec: dict[str, Any]) -> dict[str, Any]:
    """
    Reduces an OpenAPI spec into a lightweight structure with reusable components,
    identified by a unique fingerprint of their properties.
    """
    canonical_params: dict[str, dict[str, Any]] = {}
    param_usage_count: dict[str, int] = {}
    op_param_hashes: dict[str, list[str]] = {}

    paths = spec.get("paths", {})
    if not isinstance(paths, dict):
        return {"components": {"parameters": {}}, "operations": {}}

    # Pass 1: Collect parameter fingerprints across operations
    for path, methods_dict in paths.items():
        if not isinstance(methods_dict, dict):
            continue

        path_level_params: list[dict[str, Any]] = methods_dict.get("parameters", [])
        for method, details_dict in methods_dict.items():
            if method.lower() not in VALID_METHODS or not isinstance(details_dict, dict):
                continue

            op_id: Optional[str] = details_dict.get("operationId")
            if not op_id:
                continue

            op_params = get_params_from_operation(details_dict, path_level_params, spec)
            hashes = []

            for param in op_params:
                fingerprint = get_param_fingerprint(param)
                hashes.append(fingerprint)

                if fingerprint not in canonical_params:
                    canonical_params[fingerprint] = param
                    param_usage_count[fingerprint] = 1
                else:
                    param_usage_count[fingerprint] += 1

            op_param_hashes[op_id] = hashes

    # Pass 2: Identify reusable parameters
    reusable_components = {
        fp: canonical_params[fp] for fp, count in param_usage_count.items() if count > 1
    }

    # Pass 3: Construct operations with $refs where possible
    operations: dict[str, dict[str, Any]] = {}
    for path, methods_dict in paths.items():
        if not isinstance(methods_dict, dict):
            continue

        for method, details_dict in methods_dict.items():
            if method.lower() not in VALID_METHODS or not isinstance(details_dict, dict):
                continue

            op_id = details_dict.get("operationId")
            if not op_id:
                continue

            final_params: list[dict[str, Any]] = []
            seen: set[str] = set()

            for fingerprint in op_param_hashes.get(op_id, []):
                if fingerprint in seen:
                    continue
                seen.add(fingerprint)

                if fingerprint in reusable_components:
                    final_params.append({"$ref": f"#/$defs/parameters/{fingerprint}"})
                else:
                    param_details = canonical_params[fingerprint]
                    # Default type if missing
                    if "type" not in param_details:
                        param_details = {**param_details, "type": "object"}
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

    return {"components": {"parameters": reusable_components}, "operations": operations}


def save_metadata(service: str, data: dict[str, Any], out_dir: Path) -> Path:
    """
    Save extracted metadata into a utilize.json file.
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"{service}.utilize.json"
    path.write_bytes(msgspec.json.encode(data))
    return path
