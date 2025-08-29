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


def get_all_operations() -> list[tuple[str, str]]:
    """Discovers and returns a list of (service, operation) tuples."""
    client = DiscoveryClient()
    all_ops = []
    for service in get_all_services():
        try:
            ops = client.list_operations(service)
            for op in ops:
                all_ops.append((service, op))
        except FileNotFoundError:
            continue
    return all_ops


@pytest.mark.parametrize("service_name", get_all_services())
def test_service_data_loads_correctly(service_name: str):
    """Tests that the ServiceData object for each service can be loaded without errors."""
    try:
        service_data = load_service_from_disk(service_name)
        assert service_data.service_name == service_name
    except Exception as e:
        pytest.fail(f"Failed to load service data for '{service_name}': {e}")


@pytest.mark.parametrize("service_name, operation_name", get_all_operations())
def test_operation_parameters_are_resolvable(service_name: str, operation_name: str):
    """Tests that all parameter $refs in an operation can be resolved."""
    service_data = load_service_from_disk(service_name)
    operation = service_data.operations.get(operation_name)
    assert operation is not None, f"Operation '{operation_name}' not found in service '{service_name}'"

    for param in operation.parameters:
        if isinstance(param, ParameterRef):
            assert (
                param.component_name in service_data.components.parameters
            ), f"Broken parameter reference '{param.ref}' in {service_name}/{operation_name}"
