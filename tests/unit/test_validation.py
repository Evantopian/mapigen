"""Unit tests for the parameter validation."""
import sys
from pathlib import Path

import pytest
from jsonschema.exceptions import ValidationError

# Add src to path to allow importing mapigen
sys.path.append(str(Path(__file__).resolve().parent.parent.parent / 'src'))

from mapigen.validation.schemas import build_and_validate_parameters

MOCK_SERVICE_DATA = {
    "operations": {
        "test_op": {
            "parameters": [
                {
                    "name": "user_id",
                    "in": "path",
                    "required": True,
                    "type": "integer",
                },
                {
                    "name": "limit",
                    "in": "query",
                    "required": False,
                    "type": "integer",
                    "default": 10,
                },
                {
                    "name": "status",
                    "in": "query",
                    "required": False,
                    "type": "string",
                    "enum": ["active", "inactive"],
                },
            ]
        }
    }
}


def test_validation_success():
    """Tests that valid parameters pass validation."""
    params = {"user_id": 123, "limit": 50, "status": "active"}
    build_and_validate_parameters(MOCK_SERVICE_DATA, "test_op", params)
    # No exception means success


def test_validation_missing_required():
    """Tests that a missing required parameter raises a ValidationError."""
    params = {"limit": 50}
    with pytest.raises(ValidationError, match="'user_id' is a required property"):
        build_and_validate_parameters(MOCK_SERVICE_DATA, "test_op", params)


def test_validation_wrong_type():
    """Tests that a parameter with the wrong type raises a ValidationError."""
    params = {"user_id": "not-an-integer"}
    with pytest.raises(ValidationError, match="'not-an-integer' is not of type 'integer'"):
        build_and_validate_parameters(MOCK_SERVICE_DATA, "test_op", params)


def test_validation_unexpected_param():
    """Tests that an unexpected parameter raises a ValidationError."""
    params = {"user_id": 123, "unexpected": "foo"}
    with pytest.raises(ValidationError, match="Additional properties are not allowed"):
        build_and_validate_parameters(MOCK_SERVICE_DATA, "test_op", params)


def test_validation_enum_mismatch():
    """Tests that a parameter outside the enum raises a ValidationError."""
    params = {"user_id": 123, "status": "invalid-status"}
    with pytest.raises(ValidationError, match="'invalid-status' is not one of"):
        build_and_validate_parameters(MOCK_SERVICE_DATA, "test_op", params)
