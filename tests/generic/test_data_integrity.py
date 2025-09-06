"""Generic, dynamic tests that verify the integrity of all populated service data."""
import pytest
from mapigen.discovery import DiscoveryClient
from mapigen.cache.storage import load_service_from_disk
from mapigen.models import ParameterRef

def get_all_service_identifiers() -> list[tuple[str, str, str]]:
    """Discovers and returns a list of all available (provider, api, source) tuples."""
    client = DiscoveryClient()
    identifiers = []
    try:
        providers = client.list_providers()
        for provider in providers:
            apis = client.list_apis(provider)
            for api in apis:
                api_info = client.get_api_info(provider, api)
                for source in api_info.sources:
                    identifiers.append((provider, api, source))
    except FileNotFoundError:
        pass  # If registry doesn't exist, tests will be skipped
    return identifiers


@pytest.mark.parametrize("provider,api,source", get_all_service_identifiers())
def test_service_data_integrity(provider: str, api: str, source: str):
    """Tests that service data loads and all parameter $refs are resolvable."""
    # 1. Test that the service data can be loaded
    try:
        service_data = load_service_from_disk(provider, api, source)
        assert service_data.service_name == api
    except Exception as e:
        pytest.fail(f"Failed to load service data for '{provider}/{api}/{source}': {e}")

    # 2. Test that all parameter references in all operations are resolvable
    all_ops = service_data.operations.keys()
    if not all_ops:
        pytest.skip(f"No operations found for service '{api}'.")

    for operation_name in all_ops:
        operation = service_data.operations.get(operation_name)
        assert operation is not None, f"Operation '{operation_name}' not found in service '{api}'"

        for param in operation.parameters:
            if isinstance(param, ParameterRef):
                assert (
                    param.component_name in service_data.components.parameters
                ), f"Broken parameter reference '{param.ref}' in {api}/{operation_name}"
