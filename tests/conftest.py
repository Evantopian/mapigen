"""Global fixtures for the test suite."""
from typing import Any, Dict

import pytest
import msgspec

from mapigen.models import (
    ServiceData,
    ApiInfo,
    ServiceRegistry,
)
from .helpers import result_reporter

@pytest.fixture(scope="session", autouse=True)
def save_report_at_end(request):
    """A session-level fixture to automatically save the report at the end."""
    yield
    # This code runs after the entire test session finishes
    result_reporter.save()

@pytest.fixture(scope="session")
def service_registry_fixture() -> ServiceRegistry:
    """Returns a reusable, typed ServiceRegistry object for testing."""
    return ServiceRegistry(
        version="1.0-test",
        generated_at="2025-01-01T00:00:00Z",
        providers={
            "provider_a": {
                "service_a": ApiInfo(
                    sources=["default"],
                    operation_count=10,
                    popularity_rank=1,
                    auth_types=["bearer_token"],
                    primary_auth="bearer_token",
                )
            },
            "provider_b": {
                "service_b": ApiInfo(
                    sources=["default"],
                    operation_count=20,
                    popularity_rank=2,
                    auth_types=["basic_auth", "api_key"],
                    primary_auth="basic_auth",
                )
            },
        },
    )


@pytest.fixture(scope="session")
def service_data_fixture() -> ServiceData:
    """Returns a reusable, typed ServiceData object for testing."""
    # This is a dictionary representation that will be decoded into the object
    # This makes the fixture more readable and easier to maintain
    data_dict: Dict[str, Any] = {
        "format_version": 3,
        "service_name": "mock_service",
        "servers": [{"url": "https://example.com", "description": "Test Server"}],
        "components": {
            "parameters": {
                "common_param": {
                    "name": "common_param",
                    "in": "query",
                    "schema": {"type": "string"},
                }
            }
        },
        "operations": {
            "test_op": {
                "service": "mock_service",
                "path": "/test/{user_id}",
                "method": "GET",
                "parameters": [
                    {
                        "name": "user_id",
                        "in": "path",
                        "required": True,
                        "schema": {"type": "integer"},
                    },
                    {
                        "name": "limit",
                        "in": "query",
                        "required": False,
                        "schema": {"type": "integer", "default": 10},
                    },
                    {
                        "name": "status",
                        "in": "query",
                        "required": False,
                        "schema": {"type": "string", "enum": ["active", "inactive"]},
                    },
                    {
                        "$ref": "#/$defs/parameters/common_param"
                    }
                ],
            }
        },
    }
    return msgspec.json.decode(msgspec.json.encode(data_dict), type=ServiceData)
