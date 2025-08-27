import sys
from pathlib import Path
from unittest.mock import patch, MagicMock

# Add src to path to allow importing mapigen
sys.path.append(str(Path(__file__).resolve().parent.parent / 'src'))

from mapigen import Mapi
from mapigen.auth.providers import BearerTokenProvider


def test_proxy_success():
    """Tests that a valid proxy call succeeds."""
    print("\n--- Running Test: test_proxy_success ---")
    client = Mapi()
    print("Testing dynamic proxy for PokeAPI...")
    try:
        result = client.pokeapi.api_v2_pokemon_retrieve(id='ditto')
        if result and 'name' in result and result['name'] == 'ditto':
            print("SUCCESS: Proxy test successful! Received data for Ditto.")
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


@patch('requests.request')
def test_auth_provider_headers(mock_request: MagicMock):
    """Tests that the auth provider correctly adds headers to the request."""
    print("\n--- Running Test: test_auth_provider_headers ---")
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"status": "mock success"}
    mock_request.return_value = mock_response

    print("Initializing client with BearerTokenProvider...")
    auth_provider = BearerTokenProvider(token="my-dummy-token")
    client = Mapi(auth_provider=auth_provider)

    print("Executing call with auth...")
    client.pokeapi.api_v2_pokemon_retrieve(id='ditto')

    # Check that requests.request was called
    if not mock_request.called:
        print("FAILURE: requests.request was not called.")
        return

    # Inspect the headers passed to the mock
    _, kwargs = mock_request.call_args
    sent_headers = kwargs.get("headers", {})
    expected_header = {"Authorization": "Bearer my-dummy-token"}

    print(f"Sent headers: {sent_headers}")
    if "Authorization" in sent_headers and sent_headers["Authorization"] == expected_header["Authorization"]:
        print("SUCCESS: Auth headers were correctly passed to the request.")
    else:
        print(f"FAILURE: Auth headers are incorrect. Expected {expected_header}")



if __name__ == "__main__":
    test_proxy_success()
    test_proxy_non_existent_service()
    test_auth_provider_headers()
