"""Unit tests for the authentication providers."""
import sys
from pathlib import Path

import pytest

# Add src to path to allow importing mapigen
sys.path.append(str(Path(__file__).resolve().parent.parent.parent / 'src'))

from mapigen.auth.providers import (
    ApiKeyProvider,
    BasicAuthProvider,
    BearerTokenProvider,
)

def test_bearer_token_provider():
    """Tests that the BearerTokenProvider generates the correct header."""
    provider = BearerTokenProvider(token="my-secret-token")
    headers = provider.get_auth_headers()
    assert headers == {"Authorization": "Bearer my-secret-token"}
    assert provider.get_auth_params() == {}

def test_basic_auth_provider():
    """Tests that the BasicAuthProvider generates the correct header."""
    # With password
    provider = BasicAuthProvider(username="user", password="pass")
    headers = provider.get_auth_headers()
    assert headers == {"Authorization": "Basic dXNlcjpwYXNz"} # user:pass
    assert provider.get_auth_params() == {}

    # Without password
    provider_no_pass = BasicAuthProvider(username="user")
    headers_no_pass = provider_no_pass.get_auth_headers()
    assert headers_no_pass == {"Authorization": "Basic dXNlcjo="} # user:

def test_api_key_provider():
    """Tests that the ApiKeyProvider generates correct headers or params."""
    # Header placement (default)
    provider_header = ApiKeyProvider(key="my-api-key", key_name="X-API-Key")
    assert provider_header.get_auth_headers() == {"X-API-Key": "my-api-key"}
    assert provider_header.get_auth_params() == {}

    # Query param placement
    provider_query = ApiKeyProvider(
        key="my-api-key", key_name="api_key", placement="query"
    )
    assert provider_query.get_auth_headers() == {}
    assert provider_query.get_auth_params() == {"api_key": "my-api-key"}

def test_provider_validation():
    """Tests that providers raise errors on invalid input."""
    with pytest.raises(ValueError):
        BearerTokenProvider(token="")

    with pytest.raises(ValueError):
        BasicAuthProvider(username="")

    with pytest.raises(ValueError):
        ApiKeyProvider(key="", key_name="foo")

    with pytest.raises(ValueError):
        ApiKeyProvider(key="key", key_name="foo", placement="invalid")
