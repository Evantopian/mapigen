"""Authentication provider framework."""
from __future__ import annotations
import abc
import base64


class AuthProvider(abc.ABC):
    """Abstract base class for all authentication providers."""

    @abc.abstractmethod
    def get_auth_headers(self) -> dict[str, str]:
        """Returns a dictionary of headers to be included in the request."""
        raise NotImplementedError

    def get_auth_params(self) -> dict[str, str]:
        """Returns a dictionary of query parameters to be included in the request."""
        return {}


class BearerTokenProvider(AuthProvider):
    """Provides Bearer Token authentication."""

    def __init__(self, token: str):
        if not token:
            raise ValueError("Token cannot be empty.")
        self._token = token

    def get_auth_headers(self) -> dict[str, str]:
        return {"Authorization": f"Bearer {self._token}"}


class BasicAuthProvider(AuthProvider):
    """Provides HTTP Basic authentication."""

    def __init__(self, username: str, password: str = ""):
        if not username:
            raise ValueError("Username cannot be empty.")
        self._username = username
        self._password = password

    def get_auth_headers(self) -> dict[str, str]:
        token = base64.b64encode(
            f"{self._username}:{self._password}".encode("utf-8")
        ).decode("utf-8")
        return {"Authorization": f"Basic {token}"}


class ApiKeyProvider(AuthProvider):
    """Provides API Key authentication in a header or query parameter."""

    def __init__(self, key: str, key_name: str, placement: str = 'header'):
        if not key:
            raise ValueError("API key cannot be empty.")
        if placement not in ['header', 'query']:
            raise ValueError("Placement must be 'header' or 'query'.")
        self._key = key
        self._key_name = key_name
        self._placement = placement

    def get_auth_headers(self) -> dict[str, str]:
        if self._placement == 'header':
            return {self._key_name: self._key}
        return {}

    def get_auth_params(self) -> dict[str, str]:
        if self._placement == 'query':
            return {self._key_name: self._key}
        return {}
