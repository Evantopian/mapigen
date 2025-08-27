"""Synchronous HTTP client for making API requests."""
from __future__ import annotations
import logging
from typing import Any, Optional

import requests


class SyncHttpClient:
    """A synchronous HTTP client using the requests library."""

    def request(
        self,
        method: str,
        url: str,
        params: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
    ) -> Optional[dict[str, Any]]:
        """Makes an HTTP request and returns the JSON response."""
        try:
            logging.info(f"Executing {method} request to {url}")
            response = requests.request(
                method=method,
                url=url,
                params=params,
                headers=headers,
                json=json_body,
            )
            response.raise_for_status()  # Raise an exception for bad status codes
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"HTTP Request failed: {e}")
            return None
