import json
from pathlib import Path
import logging

VALID_METHODS = {"get", "put", "post", "delete", "options", "head", "patch", "trace"}

def _resolve_ref(spec: dict, ref: str) -> dict:
    """Resolves a $ref pointer in the OpenAPI spec."""
    parts = ref.strip("#/").split("/")
    node = spec
    for part in parts:
        node = node.get(part, {})
    return node

def _sanitize_parameter(param: dict, op_id: str, spec: dict) -> dict | None:
    """
    Validates a parameter object, resolving $refs if necessary.
    Returns a sanitized parameter dict or None if it's invalid.
    """
    if not isinstance(param, dict):
        logging.warning(f"Parameter in {op_id} is not a dictionary, skipping.")
        return None

    if "$ref" in param:
        ref_path = param["$ref"]
        logging.info(f"Resolving referenced parameter in {op_id}: {ref_path}")
        resolved_param = _resolve_ref(spec, ref_path)
        return _sanitize_parameter(resolved_param, f"{op_id} (from ref {ref_path})", spec)

    if "name" not in param or not param["name"]:
        logging.error(f"Parameter in {op_id} has no name, cannot be fixed. Skipping.")
        return None

    if "in" not in param:
        logging.warning(f"Parameter '{param.get('name')}' in {op_id} has no 'in' location. Skipping.")
        return None

    schema = param.get("schema", {})
    param_type = schema.get("type", "any")

    return {
        "name": param["name"],
        "in": param["in"],
        "required": param.get("required", False),
        "type": param_type,
    }

def extract_operations(service: str, spec: dict) -> dict:
    """
    Reduce OpenAPI spec into lightweight operation metadata.
    """
    operations = {}
    for path, methods in spec.get("paths", {}).items():
        path_level_params = methods.get("parameters", [])

        for method, details in methods.items():
            if method.lower() not in VALID_METHODS:
                continue

            if not isinstance(details, dict):
                logging.warning(f"Skipping invalid details for {method.upper()} {path} in {service}")
                continue

            op_id = details.get("operationId") or f"{service}_{method}_{path}"
            
            operation_level_params = details.get("parameters", [])
            all_params = path_level_params + operation_level_params

            sanitized_parameters = []
            for p in all_params:
                sanitized_param = _sanitize_parameter(p, op_id, spec)
                if sanitized_param:
                    sanitized_parameters.append(sanitized_param)

            operations[op_id] = {
                "service": service,
                "path": path,
                "method": method.upper(),
                "parameters": sanitized_parameters,
            }
    return operations

def save_metadata(service: str, operations: dict, out_dir: Path) -> Path:
    """
    Save extracted metadata into a utilize.json file.
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"{service}.utilize.json"
    path.write_text(json.dumps(operations, indent=2))
    return path
