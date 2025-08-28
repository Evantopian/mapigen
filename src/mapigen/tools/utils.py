from __future__ import annotations
import yaml
import orjson as json
import logging
from pathlib import Path
from typing import Any
import lz4.frame # type: ignore

VALID_METHODS = {"get", "put", "post", "delete", "options", "head", "patch", "trace"}

def load_spec(path: Path) -> dict[str, Any]:
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

def count_openapi_operations(spec: dict[str, Any]) -> int:
    """Counts the number of operations in a raw OpenAPI spec."""
    count = 0
    for path_item in spec.get('paths', {}).values():
        path_data: dict[str, Any] = path_item # Explicitly cast
        for method_name, operation_details in path_data.items():
            method: str = method_name # Explicitly cast
            details: dict[str, Any] = operation_details # Explicitly cast
            if method.lower() in VALID_METHODS and details.get("operationId"):
                count += 1
    return count

def _resolve_ref(spec: dict[str, Any], ref: str) -> dict[str, Any]:
    """Resolves a $ref pointer in the OpenAPI spec."""
    parts = ref.strip("#/").split("/")
    node: dict[str, Any] = spec
    for part in parts:
        if part not in node:
            logging.warning(f"Could not resolve $ref: '{ref}'. Part '{part}' not found.")
            return {}
        node = node[part]
    return node

def _extract_parameter_details(param_data: dict[str, Any]) -> dict[str, Any]:
    """Extracts all relevant details from a parameter definition."""
    details: dict[str, Any] = {}
    schema: dict[str, Any] = param_data.get("schema", param_data)
    # Define a consistent set of keys to check for fingerprinting
    for key in sorted(["description", "deprecated", "required", "default", "enum", "pattern", "minLength", "maxLength", "minimum", "maximum", "format"]):
        if key in param_data:
            details[key] = param_data[key]
        elif key in schema:
            details[key] = schema[key]
    
    # Only add the type if it's explicitly defined and valid.
    # The absence of a type key means 'any type' in JSON Schema.
    param_type = schema.get("type")
    if param_type:
        details["type"] = param_type

    if "required" not in details:
        details["required"] = param_data.get("required", False)
    return details

def _unwrap_schema_properties(schema: dict[str, Any], spec: dict[str, Any], visited: set[str]) -> list[dict[str, Any]]:
    """Recursively unwraps a schema's properties into a flat list of parameters."""
    params: list[dict[str, Any]] = []

    if "$ref" in schema:
        ref_path: str = schema["$ref"] # Explicitly cast
        if ref_path in visited:
            return [] # Avoid circular recursion
        visited.add(ref_path)
        schema = _resolve_ref(spec, ref_path)
        return _unwrap_schema_properties(schema, spec, visited)

    if "allOf" in schema:
        for sub_schema in schema["allOf"]:
            params.extend(_unwrap_schema_properties(sub_schema, spec, visited))

    for name, prop_data_item in schema.get("properties", {}).items():
        prop_data: dict[str, Any] = prop_data_item # Explicitly cast
        
        if "$ref" in prop_data:
            ref_path: str = prop_data["$ref"] # Explicitly cast
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

def get_params_from_operation(op_details: dict[str, Any], path_params: list[dict[str, Any]], spec: dict[str, Any]) -> list[dict[str, Any]]:
    """Gets all parameters for an operation from its `parameters` array and `requestBody`."""
    params: list[dict[str, Any]] = []
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

    compressed: bytes = lz4.frame.compress(raw_bytes) # type: ignore

    out_path = json_path.with_suffix(json_path.suffix + ".lz4")
    out_path.write_bytes(compressed) # type: ignore
    return out_path



def extract_auth_info(spec: dict[str, Any]) -> dict[str, Any]:
    """
    Extracts authentication information from the OpenAPI spec's security schemes.
    """
    auth_types: list[str] = []
    primary_auth: str = "none"
    
    security_schemes: dict[str, Any] = spec.get("components", {}).get("securitySchemes", {})
    
    for _, scheme_details in security_schemes.items():
        auth_type = scheme_details.get("type")
        if auth_type == "http":
            scheme = scheme_details.get("scheme", "").lower()
            if scheme == "bearer":
                auth_types.append("bearer_token")
            elif scheme == "basic":
                auth_types.append("basic_auth")
        elif auth_type == "apiKey":
            auth_types.append("api_key")
        elif auth_type == "oauth2":
            auth_types.append("oauth2")

    if auth_types:
        primary_auth = auth_types[0]

    return {"auth_types": auth_types, "primary_auth": primary_auth}

def resolve_parameter(param_ref: dict[str, Any], service_data: dict[str, Any]) -> dict[str, Any]:
    """Resolves a parameter reference to its full definition."""
    if "$ref" in param_ref:
        ref_path = param_ref["$ref"]
        if not ref_path.startswith("#/$defs/parameters/"):
            # In a real-world scenario, might raise an error
            return {}
        component_name = ref_path.split("/")[-1]
        return service_data.get("components", {}).get("parameters", {}).get(component_name, {})
    # If there's no $ref, it's an inline parameter object already
    return param_ref