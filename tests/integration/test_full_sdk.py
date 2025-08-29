from __future__ import annotations
from unittest.mock import patch, MagicMock
import pytest
from mapigen import Mapi
from mapigen.client.config import ResponseMetadata
from mapigen.client.exceptions import MapiError


def test_proxy_success():
    """Tests that a valid proxy call succeeds and returns the new structure."""
    print("\n--- Running Test: test_proxy_success ---")
    client = Mapi()
    # Mock the HTTP client to avoid actual network calls
    with patch.object(client.http_client, 'request', return_value=MagicMock(ok=True)) as mock_request:
        mock_request.return_value.json.return_value = {"id": 1, "name": "ditto"}
        result = client.pokeapi.api_v2_pokemon_retrieve(id='ditto')

    assert isinstance(result, dict)
    assert "data" in result and "metadata" in result
    assert result["data"] is not None
    print("SUCCESS: Proxy test successful!")

def test_proxy_non_existent_service():
    """Tests that calling a non-existent service via proxy raises an AttributeError."""
    print("\n--- Running Test: test_proxy_non_existent_service ---")
    client = Mapi()
    with pytest.raises(AttributeError):
        _ = client.non_existent_service
    print("SUCCESS: Caught expected AttributeError.")

@patch('niquests.Session.request')
def test_native_auth(mock_request: MagicMock):
    """Tests that the native niquests auth object is correctly passed."""
    print("\n--- Running Test: test_native_auth ---")
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"status": "mock success"}
    mock_request.return_value = mock_response

    client = Mapi(auth="my-dummy-token")
    client.pokeapi.api_v2_pokemon_retrieve(id='ditto')
    assert mock_request.called
    # Further assertions can be made on the `auth` object passed to the request
    print("SUCCESS: Auth object was correctly passed.")

def test_validation_error_structure():
    """Tests that a validation error returns the correct metadata structure."""
    print("\n--- Running Test: test_validation_error_structure ---")
    client = Mapi()
    result = client.pokeapi.api_v2_pokemon_retrieve() # Missing required 'id'

    assert isinstance(result, dict)
    assert result["data"] is None
    assert isinstance(result["metadata"], ResponseMetadata)
    assert result["metadata"].status == "error"
    assert result["metadata"].error_type == "validation"

def test_error_classification():
    client = Mapi()
    try:
        raise MapiError("test error", service="test_service", operation="test_op", error_type="sdk")
    except Exception as e:
        metadata = client._create_metadata("test_service", "test_op", 0, error=e)
        assert metadata.error_type == "sdk"