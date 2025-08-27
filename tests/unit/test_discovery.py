"""Unit tests for the discovery service."""
import sys
from pathlib import Path
from unittest.mock import patch, MagicMock

# Add src to path to allow importing mapigen
sys.path.append(str(Path(__file__).resolve().parent.parent.parent / 'src'))

from mapigen.discovery import services

MOCK_REGISTRY = {
    "service_a": {
        "path": "data/service_a",
        "auth_types": ["bearer_token"],
        "primary_auth": "bearer_token",
    },
    "service_b": {
        "path": "data/service_b",
        "auth_types": ["basic_auth", "api_key"],
        "primary_auth": "basic_auth",
    },
}


@patch("mapigen.discovery.services._load_registry", return_value=MOCK_REGISTRY)
def test_list_services(mock_load_registry: MagicMock):
    """Tests that list_services returns the correct keys."""
    result = services.list_services()
    assert result == ["service_a", "service_b"]


@patch("mapigen.discovery.services._load_registry", return_value=MOCK_REGISTRY)
def test_service_exists(mock_load_registry: MagicMock):
    """Tests that service_exists returns correct boolean values."""
    assert services.service_exists("service_a") is True
    assert services.service_exists("service_c") is False


@patch("mapigen.discovery.services._load_registry", return_value=MOCK_REGISTRY)
def test_get_service_info(mock_load_registry: MagicMock):
    """Tests that get_service_info returns the correct dictionary."""
    info = services.get_service_info("service_b")
    assert info == MOCK_REGISTRY["service_b"]


@patch("mapigen.discovery.services._load_registry", return_value=MOCK_REGISTRY)
def test_get_auth_types(mock_load_registry: MagicMock):
    """Tests that get_auth_types returns the correct list."""
    auth_types = services.get_auth_types("service_b")
    assert auth_types == ["basic_auth", "api_key"]


@patch("mapigen.discovery.services._load_registry", return_value=MOCK_REGISTRY)
def test_get_primary_auth(mock_load_registry: MagicMock):
    """Tests that get_primary_auth returns the correct string."""
    primary_auth = services.get_primary_auth("service_a")
    assert primary_auth == "bearer_token"
