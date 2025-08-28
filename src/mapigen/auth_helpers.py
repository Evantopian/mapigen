from __future__ import annotations
from urllib.parse import urlparse, urlunparse, parse_qs, urlencode

from niquests.auth import AuthBase
from niquests.models import PreparedRequest


class ApiKey(AuthBase):
    """Attaches API Key authentication to a given Request object."""

    def __init__(self, key: str, name: str, placement: str = 'header'):
        if not key:
            raise ValueError("API key cannot be empty.")
        if placement not in ['header', 'query', 'cookie']:
            raise ValueError("Placement must be 'header', 'query', or 'cookie'.")
        self.key = key
        self.name = name
        self.placement = placement

    def __call__(self, r: PreparedRequest) -> PreparedRequest:
        if self.placement == 'header':
            if r.headers is not None:
                r.headers[self.name] = self.key
        elif self.placement == 'query' and r.url is not None:
            parsed_url = urlparse(r.url)
            query_params = parse_qs(parsed_url.query)
            query_params[self.name] = [self.key]
            new_query = urlencode(query_params, doseq=True)
            new_url_parts = parsed_url._replace(query=new_query)
            r.url = urlunparse(new_url_parts)
        return r

class BearerAuth(AuthBase):
    """Attaches Bearer Token authentication to a given Request object."""

    def __init__(self, token: str):
        self.token = token

    def __call__(self, r: PreparedRequest) -> PreparedRequest:
        if r.headers is not None:
            r.headers["Authorization"] = f"Bearer {self.token}"
        return r

class AuthHelpers:
    """Provides a namespace for authentication helper classes."""
    ApiKey = ApiKey
    BearerAuth = BearerAuth
