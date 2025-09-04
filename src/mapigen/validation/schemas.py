from __future__ import annotations
import logging
from typing import Any, Dict, List

import msgspec

from ..client.exceptions import MapiError
from ..models import Parameter, ParameterRef
from ..cache.storage import load_service_from_disk
from ..discovery import DiscoveryClient

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

class SchemaValidator:
    """
    A class to validate parameters against their schemas.
    """
    def __init__(self, service_data):
        self.service_data = service_data

    def validate(self, operation_name: str, parameters: Dict[str, Any]):
        """
        Validates the provided parameters against the schema for the given operation.
        """
        operation = self.service_data.operations.get(operation_name)
        if not operation:
            raise MapiError(f"Operation '{operation_name}' not found.", error_type="validation")

        # Collect all parameters for the operation
        op_params: List[Parameter] = []
        for param_union in operation.parameters:
            if isinstance(param_union, ParameterRef):
                param_details = self.service_data.components.parameters.get(param_union.component_name)
                if not param_details:
                    raise MapiError(f"Could not resolve parameter reference: {param_union.ref}", error_type="validation")
                op_params.append(param_details)
            else:
                op_params.append(param_union)

        # Check for missing required parameters
        for param in op_params:
            if param.required and param.name not in parameters:
                raise MapiError(f"Missing required parameter: '{param.name}'", error_type="validation")

        # Validate provided parameters against their schemas
        for param_name, value in parameters.items():
            param_spec = next((p for p in op_params if p.name == param_name), None)
            if not param_spec:
                # Allow extra parameters for now, but log a warning
                logging.warning(f"Extra parameter provided for operation '{operation_name}': '{param_name}'")
                continue

            # This is a simplified validation. A more robust implementation
            # would use a library like jsonschema to validate against param_spec.schema_
            expected_type = param_spec.schema_.get("type")
            if expected_type == "string" and not isinstance(value, str):
                raise MapiError(f"Invalid type for parameter '{param_name}'. Expected string, got {type(value).__name__}.", error_type="validation")
            elif expected_type == "integer" and not isinstance(value, int):
                raise MapiError(f"Invalid type for parameter '{param_name}'. Expected integer, got {type(value).__name__}.", error_type="validation")
            # Add more type checks as needed...

def build_and_validate_parameters(service_key: str, operation_name: str, parameters: Dict[str, Any]):
    """
    Builds a validator for the service and validates the parameters for an operation.
    """
    try:
        discovery = DiscoveryClient()
        provider, api, source = discovery.parse_service_key(service_key)
        service_path = discovery.get_service_path(provider, source, api)
        service_data = load_service_from_disk(service_path)
        validator = SchemaValidator(service_data)
        validator.validate(operation_name, parameters)
    except (FileNotFoundError, msgspec.ValidationError) as e:
        raise MapiError(f"Could not load service data for '{service_key}'.", error_type="sdk", original_exception=e) from e
