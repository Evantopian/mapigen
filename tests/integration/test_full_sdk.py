import sys
from pathlib import Path
from unittest.mock import patch, MagicMock
import pytest

# Add src to path to allow importing mapigen
sys.path.append(str(Path(__file__).resolve().parent.parent.parent / 'src'))

from mapigen import Mapi
from mapigen.client.config import ResponseMetadata


def test_proxy_success():
    """Tests that a valid proxy call succeeds and returns the new structure."""
    print("\n--- Running Test: test_proxy_success ---")
    client = Mapi()
    result = client.pokeapi.api_v2_pokemon_retrieve(id='ditto')
    
    assert isinstance(result, dict)
    assert "data" in result and "metadata" in result
    assert result["data"] is not None
    assert result["data"].get('name') == 'ditto'
    assert result["metadata"].status == "success"
    print("SUCCESS: Proxy test successful!")


def test_proxy_non_existent_service():
    """Tests that calling a non-existent service raises an AttributeError."""
    print("\n--- Running Test: test_proxy_non_existent_service ---")
    client = Mapi()
    with pytest.raises(AttributeError):
        client.non_existent_service.foo.bar()
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
    _, kwargs = mock_request.call_args
    assert kwargs.get("auth") == "my-dummy-token"
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
    assert result["metadata"].error_type == "sdk_error"
    print("SUCCESS: Validation error returned correct metadata structure.")