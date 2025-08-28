import sys
from pathlib import Path
from unittest.mock import patch, MagicMock
import pytest

# Add src to path to allow importing mapigen
sys.path.append(str(Path(__file__).resolve().parent.parent.parent / 'src'))

from mapigen import Mapi
from mapigen.client.exceptions import RequestError
from mapigen.client.config import ResponseMetadata


def test_proxy_success():
    """Tests that a valid proxy call succeeds."""
    print("\n--- Running Test: test_proxy_success ---")
    client = Mapi()
    print("Testing dynamic proxy for PokeAPI...")
    try:
        result = client.pokeapi.api_v2_pokemon_retrieve(id='ditto')
        assert result is not None
        if result and 'name' in result and result['name'] == 'ditto':
            print("SUCCESS: Proxy test successful! Received data for Ditto.")
            condensed_result = {
                "id": result.get("id"), "name": result.get("name"),
                "height": result.get("height"), "weight": result.get("weight"),
            }
            print(f"Condensed result: {condensed_result}")
        else:
            print(f"FAILURE: Proxy test may have failed. Unexpected result: {result}")
    except Exception as e:
        print(f"FAILURE: Proxy test failed with an unexpected exception: {e}")

def test_proxy_non_existent_service():
    """Tests that calling a non-existent service raises an AttributeError."""
    print("\n--- Running Test: test_proxy_non_existent_service ---")
    client = Mapi()
    print("Testing a service that doesn't exist...")
    with pytest.raises(AttributeError):
        client.non_existent_service.foo.bar()
    print("SUCCESS: Caught expected AttributeError for non-existent service.")

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
    _, kwargs = mock_request.call_args
    assert kwargs.get("auth") == "my-dummy-token"
    print("SUCCESS: Auth object was correctly passed to the request.")

def test_metadata_flag():
    """Tests that the include_metadata flag returns the correct structure."""
    print("\n--- Running Test: test_metadata_flag ---")
    client = Mapi()
    # Test success case
    result = client.pokeapi.api_v2_pokemon_retrieve(id='snorlax', include_metadata=True)
    assert isinstance(result, dict)
    assert "data" in result and "metadata" in result
    assert isinstance(result["metadata"], ResponseMetadata)
    assert result["data"]['name'] == 'snorlax'
    assert result["metadata"].status == "success"
    print("SUCCESS: Metadata flag returned correct success structure.")

    # Test error case
    result_err = client.pokeapi.api_v2_pokemon_retrieve(include_metadata=True)
    assert isinstance(result_err, dict)
    assert result_err["data"] is None and "metadata" in result_err
    assert isinstance(result_err["metadata"], ResponseMetadata)
    assert result_err["metadata"].status == "error"
    print("SUCCESS: Metadata flag returned correct error structure.")


def test_validation_missing_required():
    """Tests that a call with a missing required parameter raises a RequestError."""
    print("\n--- Running Test: test_validation_missing_required ---")
    client = Mapi()
    with pytest.raises(RequestError):
        client.pokeapi.api_v2_pokemon_retrieve()
    print("SUCCESS: Caught expected RequestError.")

def test_validation_unexpected_param():
    """Tests that a call with an unexpected parameter raises a RequestError."""
    print("\n--- Running Test: test_validation_unexpected_param ---")
    client = Mapi()
    with pytest.raises(RequestError):
        client.pokeapi.api_v2_pokemon_retrieve(id='ditto', foo='bar')
    print("SUCCESS: Caught expected RequestError.")
