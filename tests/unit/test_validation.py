"""Unit tests for the parameter validation."""
import pytest
import msgspec
from unittest.mock import MagicMock
from typing import Optional, Literal

from mapigen.validation.schemas import build_and_validate_parameters
from mapigen.models import ServiceData
from mapigen.client.exceptions import MapiError


class MockOpParams(msgspec.Struct, forbid_unknown_fields=True):
    user_id: int
    limit: Optional[int] = None
    status: Optional[Literal["active", "inactive"]] = None

@pytest.fixture
def mock_service_data() -> ServiceData:
    """Creates a mock ServiceData object for testing."""
    data_dict = {
        "format_version": 3,
        "service_name": "mock_service",
        "servers": [{"url": "https://example.com"}],
        "components": {},
        "operations": {
            "test_op": {
                "service": "mock_service",
                "path": "/test/{user_id}",
                "method": "GET",
                "parameters": [
                    {
                        "type": "inline",
                        "name": "user_id",
                        "in": "path",
                        "required": True,
                        "schema": {"type": "integer"},
                    },
                    {
                        "type": "inline",
                        "name": "limit",
                        "in": "query",
                        "required": False,
                        "schema": {"type": "integer", "default": 10},
                    },
                    {
                        "type": "inline",
                        "name": "status",
                        "in": "query",
                        "required": False,
                        "schema": {"type": "string", "enum": ["active", "inactive"]},
                    },
                ]
            }
        }
    }
    return msgspec.json.decode(msgspec.json.encode(data_dict), type=ServiceData)


@pytest.fixture
def mock_schema_module(monkeypatch):
    """Mocks the schema module import."""
    mock_module = MagicMock()
    
    monkeypatch.setattr(
        "mapigen.validation.schemas._import_schema_module",
        lambda service_name: mock_module
    )
    
    monkeypatch.setattr(
        mock_module,
        "test_op_params",
        MockOpParams
    )
    
    return mock_module


def test_validation_success(mock_service_data: ServiceData, mock_schema_module):
    """Tests that valid parameters pass validation."""
    params = {"user_id": 123, "limit": 50, "status": "active"}
    build_and_validate_parameters(mock_service_data.service_name, "test_op", params)
    # No exception means success


def test_validation_missing_required(mock_service_data: ServiceData, mock_schema_module):
    """Tests that a missing required parameter raises a MapiError."""
    params = {"limit": 50}
    with pytest.raises(MapiError):
        build_and_validate_parameters(mock_service_data.service_name, "test_op", params)


def test_validation_wrong_type(mock_service_data: ServiceData, mock_schema_module):
    """Tests that a parameter with the wrong type raises a MapiError."""
    params = {"user_id": "not-an-integer"}
    with pytest.raises(MapiError):
        build_and_validate_parameters(mock_service_data.service_name, "test_op", params)


def test_validation_unexpected_param(mock_service_data: ServiceData, mock_schema_module):
    """Tests that an unexpected parameter raises a MapiError."""
    params = {"user_id": 123, "unexpected": "foo"}
    with pytest.raises(MapiError):
        build_and_validate_parameters(mock_service_data.service_name, "test_op", params)


def test_validation_enum_mismatch(mock_service_data: ServiceData, mock_schema_module):
    """Tests that a parameter outside the enum raises a MapiError."""
    params = {"user_id": 123, "status": "invalid-status"}
    with pytest.raises(MapiError):
        build_and_validate_parameters(mock_service_data.service_name, "test_op", params)