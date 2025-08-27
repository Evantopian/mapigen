import json
from pathlib import Path
import logging
from typing import Any, Dict, List, Set

VALID_METHODS = {"get", "put", "post", "delete", "options", "head", "patch", "trace"}

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
    for key in ["description", "deprecated", "required", "default", "enum", "pattern", "minLength", "maxLength", "minimum", "maximum", "format"]:
        if key in param_data:
            details[key] = param_data[key]
        if key in schema:
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
        # Continue unwrapping from the resolved schema
        return _unwrap_schema_properties(schema, spec, visited)

    # AllOf is used for composition
    if "allOf" in schema:
        for sub_schema in schema["allOf"]:
            params.extend(_unwrap_schema_properties(sub_schema, spec, visited))

    # Properties of the current schema level
    for name, prop_data in schema.get("properties", {}).items():
        if not isinstance(prop_data, dict):
            continue
        
        # If a property is itself a reference, unwrap it
        if "$ref" in prop_data:
            ref_path = prop_data["$ref"]
            if ref_path in visited:
                continue
            visited.add(ref_path)
            resolved_prop_schema = _resolve_ref(spec, ref_path)
            # We assume the unwrapped properties of a nested object should be treated as a single JSON object parameter
            # This could be enhanced later if needed.
            param_details = {"name": name, "in": "body"}
            param_details.update(_extract_parameter_details(prop_data))
            param_details["type"] = "object" # The nested item is an object
            params.append(param_details)
        else:
            param_details = {"name": name, "in": "body"}
            param_details.update(_extract_parameter_details(prop_data))
            params.append(param_details)
            
    return params

def get_params_from_operation(op_details: Dict[str, Any], path_params: List[Dict[str, Any]], spec: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Gets all parameters for an operation from its `parameters` array and `requestBody`."""
    params = []
    # 1. From the `parameters` array
    for param_def in path_params + op_details.get("parameters", []):
        if "$ref" in param_def:
            param_def = _resolve_ref(spec, param_def["$ref"])
        if "name" in param_def and "in" in param_def:
            details = {"name": param_def["name"], "in": param_def["in"]}
            details.update(_extract_parameter_details(param_def))
            params.append(details)

    # 2. From the `requestBody`
    request_body = op_details.get("requestBody", {})
    if "$ref" in request_body:
        request_body = _resolve_ref(spec, request_body["$ref"])
    
    content = request_body.get("content", {})
    for media_type in content.values():
        if "schema" in media_type:
            params.extend(_unwrap_schema_properties(media_type["schema"], spec, set()))
            
    return params

def extract_operations_and_components(service: str, spec: Dict[str, Any]) -> Dict[str, Any]:
    """
    Reduces an OpenAPI spec into a lightweight structure with operations and reusable components.
    This version unwraps requestBody schemas to find all possible parameters.
    """
    all_params_map: Dict[str, List[Dict]] = {}
    operations_with_param_keys: Dict[str, List[str]] = {}

    # 1. First pass: Discover all parameters for every operation
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

            op_params = get_params_from_operation(details, path_level_params, spec)
            operations_with_param_keys[op_id] = []
            for param in op_params:
                param_key = f'{param["name"]}:{param["in"]}'
                operations_with_param_keys[op_id].append(param_key)
                if param_key not in all_params_map:
                    all_params_map[param_key] = []
                all_params_map[param_key].append(param)

    # 2. Second pass: Identify and create reusable components
    reusable_components = {}
    for key, param_list in all_params_map.items():
        # A simple heuristic for reusability: if a param name/location pair appears more than once.
        if len(param_list) > 1:
            # In a real scenario, you might average or merge details.
            # For now, we just take the first definition as canonical.
            reusable_components[key] = param_list[0]

    # 3. Third pass: Build the final operations structure with $refs
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
            for param_key in operations_with_param_keys.get(op_id, []):
                if param_key in reusable_components:
                    final_params.append({"$ref": f"#/$defs/parameters/{param_key}"})
                else:
                    # It appeared only once, so embed it directly.
                    final_params.append(all_params_map[param_key][0])
            
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
