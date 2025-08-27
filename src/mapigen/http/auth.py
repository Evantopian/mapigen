"""Custom, niquests-native authentication helpers."""
from __future__ import annotations
from niquests.auth import AuthBase
from niquests.models import PreparedRequest


class ApiKeyAuth(AuthBase):
    """Attaches API Key authentication to a given Request object."""

    def __init__(self, key: str, name: str, placement: str = 'header'):
        if not key:
            raise ValueError("API key cannot be empty.")
        if placement not in ['header', 'query']:
            raise ValueError("Placement must be 'header' or 'query'.")
        self.key = key
        self.name = name
        self.placement = placement

    def __call__(self, r: PreparedRequest) -> PreparedRequest:
        if self.placement == 'header':
            if r.headers is not None:
                r.headers[self.name] = self.key
        elif self.placement == 'query' and r.url is not None:
            # This is a simplified way to add a query parameter.
            # A more robust solution would parse the URL, add the param, and reconstruct.
            if '?' in r.url:
                r.url += f"&{self.name}={self.key}"
            else:
                r.url += f"?{self.name}={self.key}"
        return r
