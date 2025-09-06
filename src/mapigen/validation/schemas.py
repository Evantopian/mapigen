from __future__ import annotations
from typing import Any, Dict, List, Optional, Union

import msgspec

from mapigen.models import Parameter, ParameterRef
from mapigen.cache.storage import load_service_from_disk
from mapigen.client.exceptions import MapiError


def _get_python_type(openapi_schema: dict[str, Any]) -> Any:
    """Converts an OpenAPI schema type to a Python type hint."""
    type_map = {
        "integer": int,
        "string": str,
        "boolean": bool,
        "number": float,
    }
    openapi_type = openapi_schema.get("type")
    if not isinstance(openapi_type, str):
        return Any

    if openapi_type == "array":
        items_schema = openapi_schema.get("items", {})
        item_type = _get_python_type(items_schema)
        return List[item_type]
    
    return type_map.get(openapi_type, Any)

def build_and_validate_parameters(provider: str, api: str, source: str, operation: str, kwargs: Any):
    """Builds a dynamic msgspec.Struct for an operation and validates kwargs against it."""
    service_name = f"{provider}/{api}/{source}"
    try:
        service_data = load_service_from_disk(provider, api, source)
    except FileNotFoundError:
        raise MapiError(f"Service '{service_name}' not found for validation.", service=service_name, error_type="sdk")

    op_details = service_data.operations.get(operation)
    if not op_details:
        raise MapiError(f"Operation '{operation}' not found in service '{service_name}'", service=service_name, error_type="sdk")

    struct_fields = []
    for param_union in op_details.parameters:
        param_details: Parameter
        if isinstance(param_union, ParameterRef):
            param_details = service_data.components.parameters[param_union.component_name]
        else:
            param_details = param_union

        if not param_details.name.isidentifier():
            continue

        param_type = _get_python_type(param_details.schema_)

        if param_details.required:
            struct_fields.append((param_details.name, param_type))
        else:
            # Use None as the default for optional fields
            struct_fields.append((param_details.name, Optional[param_type], None))

    if not struct_fields:
        return # No parameters to validate

    ParamStruct = msgspec.defstruct(f"{operation}_params", struct_fields, gc=False)

    try:
        msgspec.convert(kwargs, ParamStruct, strict=False)
    except msgspec.ValidationError as e:
        raise MapiError(str(e), service=service_name, operation=operation, error_type="validation", original_exception=e) from e