"""Parameter validation using schemas from utilize.json."""
from __future__ import annotations
from typing import Any, Dict, List

import msgspec

from ..cache.storage import load_service_from_disk
from ..client.exceptions import MapiError
from ..models import Parameter, ParameterRef, ServiceData


def _validate_type(value: Any, schema: Dict[str, Any], param_name: str, service_name: str, operation_id: str):
    schema_type = schema.get("type")
    if not schema_type:
        return # No type to validate against

    py_type_map = {
        "string": str,
        "integer": int,
        "number": (int, float),
        "boolean": bool,
        "array": list,
        "object": dict,
    }

    expected_type = py_type_map.get(schema_type)
    if expected_type and not isinstance(value, expected_type):
        raise MapiError(
            f"Invalid type for parameter '{param_name}'. "
            f"Expected {schema_type}, got {type(value).__name__}",
            service=service_name,
            operation=operation_id,
            error_type="validation",
        )
    
    if "enum" in schema and value not in schema["enum"]:
        raise MapiError(
            f"Invalid value for parameter '{param_name}'. "
            f"Value '{value}' is not in the allowed enum values: {schema['enum']}",
            service=service_name,
            operation=operation_id,
            error_type="validation",
        )

    if schema_type == "array":
        items_schema = schema.get("items")
        if items_schema and isinstance(value, list):
            for item in value:
                _validate_type(item, items_schema, f"{param_name}[]", service_name, operation_id)


def build_and_validate_parameters(
    service_name: str,
    operation_id: str,
    parameters: dict[str, Any],
) -> None:
    """
    Validates parameters against the schema defined in utilize.json.
    """
    try:
        service_data: ServiceData = load_service_from_disk(service_name)
        operation = service_data.operations.get(operation_id)
        if not operation:
            raise MapiError(f"Operation '{operation_id}' not found in service '{service_name}'", service=service_name, operation=operation_id, error_type="sdk")

        op_params: Dict[str, Parameter] = {}
        for param_union in operation.parameters:
            param: Parameter
            if isinstance(param_union, ParameterRef):
                if param_union.component_name not in service_data.components.parameters:
                    raise MapiError(f"Broken parameter reference: {param_union.ref}", service=service_name, operation=operation_id, error_type="sdk")
                param = service_data.components.parameters[param_union.component_name]
            else:
                param = param_union
            op_params[param.name] = param

        # Check for required parameters
        for param_name, param_details in op_params.items():
            if param_details.required and param_name not in parameters:
                raise MapiError(f"Missing required parameter: '{param_name}'", service=service_name, operation=operation_id, error_type="validation")

        # Validate provided parameters
        for param_name, value in parameters.items():
            if param_name not in op_params:
                continue
            
            param_details = op_params[param_name]
            
            # Validate type
            _validate_type(value, param_details.schema_, param_name, service_name, operation_id)

    except FileNotFoundError as e:
        raise MapiError(f"Service data for '{service_name}' not found. Please ensure data is populated.", service=service_name, error_type="sdk", original_exception=e) from e
    except msgspec.ValidationError as e:
        # This can happen if utilize.json is corrupt
        raise MapiError(f"Service data for '{service_name}' is invalid. Please regenerate the service data. Error: {e}", service=service_name, error_type="sdk", original_exception=e) from e
