import yaml
import json
import logging
from pathlib import Path
from typing import Dict, Any, List, Set
import lz4.frame

VALID_METHODS = {"get", "put", "post", "delete", "options", "head", "patch", "trace"}

def load_spec(path: Path) -> Dict[str, Any]:
    """Loads a YAML or JSON spec from the given path."""
    try:
        content = path.read_text(encoding="utf-8")
        if path.suffix in (".yml", ".yaml"):
            return yaml.safe_load(content)
        elif path.suffix == ".json":
            return json.loads(content)
        else:
            raise ValueError(f"Unsupported file type: {path.suffix}")
    except Exception as e:
        logging.error(f"Failed to load spec file {path}: {e}")
        raise

def count_openapi_operations(spec: dict) -> int:
    """Counts the number of operations in a raw OpenAPI spec."""
    count = 0
    for path_data in spec.get('paths', {}).values():
        if isinstance(path_data, dict):
            for method, details in path_data.items():
                if method.lower() in VALID_METHODS and isinstance(details, dict) and details.get("operationId"):
                    count += 1
    return count

def _resolve_ref(spec: Dict[str, Any], ref: str) -> Dict[str, Any]:
    """Resolves a $ref pointer in the OpenAPI spec."""
    parts = ref.strip("#/").split("/")
    node = spec
    for part in parts:
        if part not in node:
            logging.warning(f"Could not resolve $ref: '{ref}'. Part '{part}' not found.")
            return {}
        node = node[part]
    return node

def _extract_parameter_details(param_data: Dict[str, Any]) -> Dict[str, Any]:
    """Extracts all relevant details from a parameter definition."""
    details = {}
    schema = param_data.get("schema", param_data)
    # Define a consistent set of keys to check for fingerprinting
    for key in sorted(["description", "deprecated", "required", "default", "enum", "pattern", "minLength", "maxLength", "minimum", "maximum", "format"]):
        if key in param_data:
            details[key] = param_data[key]
        elif key in schema:
            details[key] = schema[key]
            
    details["type"] = schema.get("type", "any")
    if "required" not in details:
        details["required"] = param_data.get("required", False)
    return details

def _unwrap_schema_properties(schema: Dict[str, Any], spec: Dict[str, Any], visited: Set[str]) -> List[Dict[str, Any]]:
    """Recursively unwraps a schema's properties into a flat list of parameters."""
    params = []
    if not isinstance(schema, dict):
        return params

    if "$ref" in schema:
        ref_path = schema["$ref"]
        if ref_path in visited:
            return [] # Avoid circular recursion
        visited.add(ref_path)
        schema = _resolve_ref(spec, ref_path)
        return _unwrap_schema_properties(schema, spec, visited)

    if "allOf" in schema:
        for sub_schema in schema["allOf"]:
            params.extend(_unwrap_schema_properties(sub_schema, spec, visited))

    for name, prop_data in schema.get("properties", {}).items():
        if not isinstance(prop_data, dict):
            continue
        
        if "$ref" in prop_data:
            ref_path = prop_data["$ref"]
            if ref_path in visited:
                continue
            visited.add(ref_path)
            param_details = {"name": name, "in": "body"}
            param_details.update(_extract_parameter_details(prop_data))
            param_details["type"] = "object"
            params.append(param_details)
        else:
            param_details = {"name": name, "in": "body"}
            param_details.update(_extract_parameter_details(prop_data))
            params.append(param_details)
            
    return params

def get_params_from_operation(op_details: Dict[str, Any], path_params: List[Dict[str, Any]], spec: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Gets all parameters for an operation from its `parameters` array and `requestBody`."""
    params = []
    for param_def in path_params + op_details.get("parameters", []):
        if "$ref" in param_def:
            param_def = _resolve_ref(spec, param_def["$ref"])
        if "name" in param_def and "in" in param_def:
            details = {"name": param_def["name"], "in": param_def["in"]}
            details.update(_extract_parameter_details(param_def))
            params.append(details)

    request_body = op_details.get("requestBody", {})
    if "$ref" in request_body:
        request_body = _resolve_ref(spec, request_body["$ref"])
    
    content = request_body.get("content", {})
    for media_type in content.values():
        if "schema" in media_type:
            params.extend(_unwrap_schema_properties(media_type["schema"], spec, set()))
            
    return params

def compress_metadata(json_path: Path) -> Path:
    """
    Read JSON file, compress it into LZ4 frame, and write to disk.
    """
    raw_bytes: bytes = json_path.read_bytes()

    compressed: bytes = lz4.frame.compress(raw_bytes)

    out_path = json_path.with_suffix(json_path.suffix + ".lz4")
    out_path.write_bytes(compressed)
    return out_path


def load_metadata(lz4_path: Path) -> Dict[str, Any]:
    compressed: bytes = lz4_path.read_bytes()
    decompressed: bytes = lz4.frame.decompress(compressed)
    text: str = decompressed.decode("utf-8")
    return json.loads(text)
