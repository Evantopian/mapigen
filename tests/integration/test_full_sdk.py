import sys
from pathlib import Path
from unittest.mock import patch, MagicMock

# Add src to path to allow importing mapigen
sys.path.append(str(Path(__file__).resolve().parent.parent / 'src'))

from mapigen import Mapi



def test_proxy_success():
    """Tests that a valid proxy call succeeds."""
    print("\n--- Running Test: test_proxy_success ---")
    client = Mapi()
    print("Testing dynamic proxy for PokeAPI...")
    try:
        result = client.pokeapi.api_v2_pokemon_retrieve(id='ditto')
        if result and 'name' in result and result['name'] == 'ditto':
            print("SUCCESS: Proxy test successful! Received data for Ditto.")
            # Print condensed JSON
            condensed_result = {
                "id": result.get("id"),
                "name": result.get("name"),
                "height": result.get("height"),
                "weight": result.get("weight"),
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
    try:
        client.non_existent_service.foo.bar()
    except AttributeError:
        print("SUCCESS: Caught expected AttributeError for non-existent service.")
    except Exception as e:
        print(f"FAILURE: Caught unexpected exception for non-existent service: {e}")


@patch('niquests.Session.request')
def test_native_auth(mock_request: MagicMock):
    """Tests that the native niquests auth object is correctly passed."""
    print("\n--- Running Test: test_native_auth ---")
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"status": "mock success"}
    mock_request.return_value = mock_response

    print("Initializing client with a direct auth token...")
    client = Mapi(auth="my-dummy-token")

    print("Executing call with auth...")
    client.pokeapi.api_v2_pokemon_retrieve(id='ditto')

    # Check that the mock request was called
    if not mock_request.called:
        print("FAILURE: niquests.Session.request was not called.")
        return

    # Inspect the auth object passed to the mock
    _, kwargs = mock_request.call_args
    sent_auth = kwargs.get("auth")
    
    print(f"Sent auth object: {sent_auth}")
    if sent_auth == "my-dummy-token":
        print("SUCCESS: Auth object was correctly passed to the request.")
    else:
        print(f"FAILURE: Auth object is incorrect. Expected 'my-dummy-token', got {sent_auth}")



def test_validation_missing_required():
    """Tests that a call with a missing required parameter fails validation."""
    print("\n--- Running Test: test_validation_missing_required ---")
    client = Mapi()
    # This call should fail because 'id' is required.
    result = client.pokeapi.api_v2_pokemon_retrieve()
    if result is None:
        print("SUCCESS: Call with missing required parameter correctly failed validation.")
    else:
        print(f"FAILURE: Call with missing required parameter did not fail. Result: {result}")


def test_validation_unexpected_param():
    """Tests that a call with an unexpected parameter fails validation."""
    print("\n--- Running Test: test_validation_unexpected_param ---")
    client = Mapi()
    # This call should fail because 'foo' is not a valid parameter.
    result = client.pokeapi.api_v2_pokemon_retrieve(id='ditto', foo='bar')
    if result is None:
        print("SUCCESS: Call with unexpected parameter correctly failed validation.")
    else:
        print(f"FAILURE: Call with unexpected parameter did not fail. Result: {result}")



if __name__ == "__main__":
    test_proxy_success()
    test_proxy_non_existent_service()
    test_native_auth()
    test_validation_missing_required()
    test_validation_unexpected_param()
