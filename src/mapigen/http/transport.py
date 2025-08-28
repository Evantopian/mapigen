"""Unified HTTP transport for sync and async requests using niquests."""
from __future__ import annotations
import logging
from typing import Any, Optional

import niquests
from niquests.auth import AuthBase
from niquests.models import Response


class HttpTransport:
    """A unified HTTP transport using niquests."""

    def __init__(self, **transport_kwargs: Any) -> None:
        self._transport_kwargs = transport_kwargs
        self._sync_session = niquests.Session(**self._transport_kwargs)

    def request(self, method: str, url: str, auth: Optional[AuthBase] = None, **kwargs: Any) -> Response:
        """Makes a synchronous HTTP request and returns the Response object."""
        logging.info(f"Executing sync {method} request to {url}")
        response = self._sync_session.request(method, url, auth=auth, **kwargs)  # type: ignore[misc]
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        return response

    async def arequest(self, method: str, url: str, auth: Optional[AuthBase] = None, **kwargs: Any) -> Response:
        """Makes an asynchronous HTTP request and returns the Response object."""
        # Niquests AsyncSession is a context manager
        async with niquests.AsyncSession(**self._transport_kwargs) as session:
            logging.info(f"Executing async {method} request to {url}")
            response = await session.request(method, url, auth=auth, **kwargs)  # type: ignore[misc]
            response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)
            return response
