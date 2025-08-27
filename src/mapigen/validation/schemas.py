"""Parameter validation using JSON Schema."""
from __future__ import annotations
from typing import Any

from jsonschema import validate



def build_and_validate_parameters(
    service_data: dict[str, Any],
    operation_id: str,
    parameters: dict[str, Any],
) -> None:
    """
    Builds a JSON schema from an operation's parameter definitions and validates
    the provided parameters against it.

    Args:
        service_data: The full 'utilize.json' data for the service.
        operation_id: The ID of the operation to validate against.
        parameters: The user-provided parameters for the API call.

    Raises:
        ValueError: If the operation is not found.
        ValidationError: If the provided parameters are invalid.
    """
    op_details = service_data.get("operations", {}).get(operation_id)
    if not op_details:
        raise ValueError(f"Operation '{operation_id}' not found in service data.")

    schema_properties: dict[str, Any] = {}
    required_params: list[str] = []

    for param_ref in op_details.get("parameters", []):
        param_details: dict[str, Any]
        if "$ref" in param_ref:
            ref_path: str = param_ref["$ref"]
            component_name: str = ref_path.split("/")[-1]
            param_details = (
                service_data.get("components", {})
                .get("parameters", {})
                .get(component_name, {})
            )
        else:
            param_details = param_ref

        param_name = param_details.get("name")
        if not param_name:
            continue

        # We can extract the schema-related keywords.
        param_schema = {}
        for key, value in param_details.items():
            if key in ["name", "in", "required"]:
                continue
            # 'any' is not a valid JSON Schema type. Omitting the type keyword
            # allows any type, which is the desired behavior.
            if key == 'type' and value == 'any':
                continue
            param_schema[key] = value
        
        schema_properties[param_name] = param_schema

        if param_details.get("required", False):
            required_params.append(param_name)

    # The final schema to validate against
    final_schema = {
        "type": "object",
        "properties": schema_properties,
        "required": required_params,
        "additionalProperties": False,
    }

    validate(instance=parameters, schema=final_schema)
