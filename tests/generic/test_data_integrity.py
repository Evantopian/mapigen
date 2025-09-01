"""Generic, dynamic tests that verify the integrity of all populated service data."""
import pytest
from mapigen.discovery import DiscoveryClient
from mapigen.cache.storage import load_service_from_disk
from mapigen.models import ParameterRef


def get_all_services() -> list[str]:
    """Discovers and returns a list of all available services."""
    try:
        return DiscoveryClient().list_services()
    except FileNotFoundError:
        return []


@pytest.mark.parametrize("service_name", get_all_services())
def test_service_data_integrity(service_name: str):
    """Tests that service data loads and all parameter $refs are resolvable."""
    # 1. Test that the service data can be loaded
    try:
        service_data = load_service_from_disk(service_name)
        assert service_data.service_name == service_name
    except Exception as e:
        pytest.fail(f"Failed to load service data for '{service_name}': {e}")

    # 2. Test that all parameter references in all operations are resolvable
    all_ops = service_data.operations.keys()
    if not all_ops:
        pytest.skip(f"No operations found for service '{service_name}'.")

    for operation_name in all_ops:
        operation = service_data.operations.get(operation_name)
        assert operation is not None, f"Operation '{operation_name}' not found in service '{service_name}'"

        for param in operation.parameters:
            if isinstance(param, ParameterRef):
                assert (
                    param.component_name in service_data.components.parameters
                ), f"Broken parameter reference '{param.ref}' in {service_name}/{operation_name}"