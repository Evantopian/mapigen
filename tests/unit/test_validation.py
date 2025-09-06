"""Unit tests for the parameter validation."""
import pytest
import msgspec
from unittest.mock import MagicMock

from mapigen.validation.schemas import build_and_validate_parameters
from mapigen.models import ServiceData
from mapigen.client.exceptions import MapiError


@pytest.fixture
def mock_service_data() -> ServiceData:
    """Creates a mock ServiceData object for testing."""
    data_dict = {
        "format_version": 3,
        "service_name": "mock_api",
        "servers": [{"url": "https://example.com"}],
        "components": {},
        "operations": {
            "test_op": {
                "service": "mock_api",
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
                        "schema": {"type": "integer"},
                    },
                    {
                        "type": "inline",
                        "name": "tags",
                        "in": "query",
                        "required": False,
                        "schema": {"type": "array", "items": {"type": "string"}},
                    },
                ],
            }
        },
    }
    return msgspec.json.decode(msgspec.json.encode(data_dict), type=ServiceData)


@pytest.fixture(autouse=True)
def mock_load_service(monkeypatch, mock_service_data: ServiceData):
    """Mocks load_service_from_disk to return the mock_service_data fixture."""
    mock_load = MagicMock(return_value=mock_service_data)
    monkeypatch.setattr("mapigen.validation.schemas.load_service_from_disk", mock_load)
    return mock_load


def test_validation_success(mock_service_data: ServiceData):
    """Tests that valid parameters pass validation."""
    params = {"user_id": 123, "limit": 50}
    build_and_validate_parameters("mock_provider", "mock_api", "mock_source", "test_op", params)


def test_validation_missing_required(mock_service_data: ServiceData):
    """Tests that a missing required parameter raises a MapiError."""
    params = {"limit": 50}
    with pytest.raises(MapiError, match="Object missing required field `user_id`"):
        build_and_validate_parameters("mock_provider", "mock_api", "mock_source", "test_op", params)


def test_validation_wrong_type(mock_service_data: ServiceData):
    """Tests that a parameter with the wrong type raises a MapiError."""
    params = {"user_id": "not-an-integer"}
    with pytest.raises(MapiError, match="Expected `int`, got `str`"):
        build_and_validate_parameters("mock_provider", "mock_api", "mock_source", "test_op", params)


def test_validation_unexpected_param(mock_service_data: ServiceData):
    """Tests that an unexpected parameter does not raise an error (due to strict=False)."""
    params = {"user_id": 123, "unexpected": "foo"}
    try:
        build_and_validate_parameters("mock_provider", "mock_api", "mock_source", "test_op", params)
    except MapiError as e:
        pytest.fail(f"Unexpected MapiError was raised for unexpected parameter: {e}")


def test_validation_array_type(mock_service_data: ServiceData):
    """Tests that array types are validated correctly."""
    # Valid case
    params_valid = {"user_id": 123, "tags": ["a", "b", "c"]}
    build_and_validate_parameters("mock_provider", "mock_api", "mock_source", "test_op", params_valid)

    # Invalid item in array
    params_invalid = {"user_id": 123, "tags": ["a", "b", 123]}
    with pytest.raises(MapiError, match="Expected `str`, got `int`"):
        build_and_validate_parameters(
            "mock_provider", "mock_api", "mock_source", "test_op", params_invalid
        )