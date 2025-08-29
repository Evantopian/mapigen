from __future__ import annotations
import hashlib
from pathlib import Path
from typing import Any, Optional, Dict
import keyword

import msgspec

from mapigen.tools.utils import get_params_from_operation, VALID_METHODS


def get_param_fingerprint(param: dict[str, Any]) -> str:
    """Creates a stable, hashable fingerprint for a parameter dictionary."""
    # Ignore volatile/example fields to ensure stable fingerprinting
    fingerprint_data = {k: v for k, v in param.items() if k not in ("example", "examples")}
    return hashlib.sha256(msgspec.json.encode(fingerprint_data)).hexdigest()

def map_type(param_schema: dict[str, Any]) -> str:
    """Maps an OpenAPI schema type to a Python type hint."""
    param_type = param_schema.get("type")
    if param_type == "string":
        return "str"
    elif param_type == "integer":
        return "int"
    elif param_type == "number":
        return "float"
    elif param_type == "boolean":
        return "bool"
    elif param_type == "array":
        items_schema = param_schema.get("items", {})
        items_type = map_type(items_schema)
        return f"List[{items_type}]"
    elif param_type == "object":
        return "Dict[str, Any]"
    else:
        return "Any"

def generate_struct_definitions(operations: Dict[str, Any], components: Dict[str, Any]) -> str:
    """Generates msgspec.Struct definitions for all operations."""
    structs = ["import msgspec", "from typing import Optional, List, Any, Dict", ""]
    for op_id, op_data in operations.items():
        struct_name = f"{op_id.replace('/', '_').replace('-', '_')}_params"
        structs.append(f"class {struct_name}(msgspec.Struct):")
        
        has_params = False
        param_names = set()
        for param_union in op_data.get("parameters", []):
            has_params = True
            if param_union["type"] == "ref":
                ref_name = param_union["$ref"].split("/")[-1]
                param = components["parameters"][ref_name]
            else:
                param = param_union

            param_name = param["name"].replace("-", "_").replace("[", "_").replace("]", "")
            if keyword.iskeyword(param_name):
                param_name = f"{param_name}_"
            
            if param_name in param_names:
                param_name = f"{param_name}_"
            param_names.add(param_name)

            param_type = map_type(param.get("schema", {}))
            
            if not param.get("required", False):
                param_type = f"Optional[{param_type}] = None"
            
            structs.append(f"    {param_name}: {param_type}")
        
        if not has_params:
            structs.append("    pass")
        
        structs.append("")
        
    return "\n".join(structs)

def extract_operations_and_components(service: str, spec: dict[str, Any]) -> dict[str, Any]:
    """
    Reduces an OpenAPI spec into a lightweight structure with all unique parameters
    as components, identified by a unique fingerprint of their properties.
    """
    canonical_params: dict[str, dict[str, Any]] = {}
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
                param_dict = msgspec.to_builtins(param)
                fingerprint = get_param_fingerprint(param_dict)
                hashes.append(fingerprint)

                if fingerprint not in canonical_params:
                    canonical_params[fingerprint] = param_dict

            op_param_hashes[op_id] = hashes

    # Pass 2: Construct operations with $refs to all unique parameters
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

    schemas = spec.get("components", {}).get("schemas", {})
    
    # Add 'type' field to all parameters for decoding
    all_params_with_type = {}
    for fp, param in canonical_params.items():
        p = param.copy()
        p["type"] = "inline"
        all_params_with_type[fp] = p

    struct_definitions = generate_struct_definitions(operations, {"parameters": all_params_with_type, "schemas": schemas})

    return {
        "components": {"parameters": all_params_with_type, "schemas": schemas},
        "operations": operations,
        "struct_definitions": struct_definitions
    }


def save_metadata(service: str, data: dict[str, Any], out_dir: Path) -> Path:
    """
    Save extracted metadata into a utilize.json file.
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"{service}.utilize.json"
    path.write_bytes(msgspec.json.encode(data))
    return path