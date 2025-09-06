"""Unit tests for the discovery service."""
import pytest
from unittest.mock import patch, MagicMock

from mapigen.discovery import services
from mapigen.models import ServiceRegistry, ApiInfo


@pytest.fixture
def mock_service_registry() -> ServiceRegistry:
    """Creates a mock ServiceRegistry object for testing."""
    return ServiceRegistry(
        version="1.0-test",
        generated_at="2025-01-01T00:00:00Z",
        providers={
            "provider_a": {
                "api_x": ApiInfo(
                    sources=["github"],
                    operation_count=10,
                    popularity_rank=1,
                    auth_types=["bearer_token"],
                    primary_auth="bearer_token",
                )
            },
            "provider_b": {
                "api_y": ApiInfo(
                    sources=["custom"],
                    operation_count=20,
                    popularity_rank=2,
                    auth_types=["basic_auth", "api_key"],
                    primary_auth="basic_auth",
                ),
                "api_z": ApiInfo(
                    sources=["github", "custom"],
                    operation_count=30,
                    popularity_rank=3,
                    auth_types=["oauth2"],
                    primary_auth="oauth2",
                ),
            },
        },
    )


@patch("mapigen.discovery.services._load_registry")
def test_list_providers(mock_load_registry: MagicMock, mock_service_registry: ServiceRegistry):
    """Tests that list_providers returns the correct keys."""
    mock_load_registry.return_value = mock_service_registry
    result = services.list_providers()
    assert result == ["provider_a", "provider_b"]


@patch("mapigen.discovery.services._load_registry")
def test_list_apis(mock_load_registry: MagicMock, mock_service_registry: ServiceRegistry):
    """Tests that list_apis returns correct keys for a provider."""
    mock_load_registry.return_value = mock_service_registry
    assert services.list_apis("provider_b") == ["api_y", "api_z"]
    assert services.list_apis("provider_c") == []


@patch("mapigen.discovery.services._load_registry")
def test_get_api_info(mock_load_registry: MagicMock, mock_service_registry: ServiceRegistry):
    """Tests that get_api_info returns the correct ApiInfo object."""
    mock_load_registry.return_value = mock_service_registry
    info = services.get_api_info("provider_b", "api_y")
    assert info == mock_service_registry.providers["provider_b"]["api_y"]
