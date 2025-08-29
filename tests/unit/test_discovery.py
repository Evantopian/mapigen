"""Unit tests for the discovery service."""
import pytest
from unittest.mock import patch, MagicMock

from mapigen.discovery import services
from mapigen.models import ServiceRegistry, ServiceInfo


@pytest.fixture
def mock_service_registry() -> ServiceRegistry:
    """Creates a mock ServiceRegistry object for testing."""
    return ServiceRegistry(
        version="1.0-test",
        generated_at="2025-01-01T00:00:00Z",
        services={
            "service_a": ServiceInfo(
                operation_count=10,
                popularity_rank=1,
                auth_types=["bearer_token"],
                primary_auth="bearer_token",
            ),
            "service_b": ServiceInfo(
                operation_count=20,
                popularity_rank=2,
                auth_types=["basic_auth", "api_key"],
                primary_auth="basic_auth",
            ),
        },
    )


@patch("mapigen.discovery.services._load_registry")
def test_list_services(mock_load_registry: MagicMock, mock_service_registry: ServiceRegistry):
    """Tests that list_services returns the correct keys."""
    mock_load_registry.return_value = mock_service_registry
    result = services.list_services()
    assert result == ["service_a", "service_b"]


@patch("mapigen.discovery.services._load_registry")
def test_service_exists(mock_load_registry: MagicMock, mock_service_registry: ServiceRegistry):
    """Tests that service_exists returns correct boolean values."""
    mock_load_registry.return_value = mock_service_registry
    assert services.service_exists("service_a") is True
    assert services.service_exists("service_c") is False


@patch("mapigen.discovery.services._load_registry")
def test_get_service_info(mock_load_registry: MagicMock, mock_service_registry: ServiceRegistry):
    """Tests that get_service_info returns the correct ServiceInfo object."""
    mock_load_registry.return_value = mock_service_registry
    info = services.get_service_info("service_b")
    assert info == mock_service_registry.services["service_b"]


@patch("mapigen.discovery.services._load_registry")
def test_get_auth_types(mock_load_registry: MagicMock, mock_service_registry: ServiceRegistry):
    """Tests that get_auth_types returns the correct list."""
    mock_load_registry.return_value = mock_service_registry
    auth_types = services.get_auth_types("service_b")
    assert auth_types == ["basic_auth", "api_key"]


@patch("mapigen.discovery.services._load_registry")
def test_get_primary_auth(mock_load_registry: MagicMock, mock_service_registry: ServiceRegistry):
    """Tests that get_primary_auth returns the correct string."""
    mock_load_registry.return_value = mock_service_registry
    primary_auth = services.get_primary_auth("service_a")
    assert primary_auth == "bearer_token"