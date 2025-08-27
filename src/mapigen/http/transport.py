"""Unified HTTP transport for sync and async requests using niquests."""
from __future__ import annotations
import logging
from typing import Any, Optional, Dict

import niquests
from niquests.models import Response


class HttpTransport:
    """A unified HTTP transport using niquests."""

    def __init__(self, **transport_kwargs: Any) -> None:
        self._transport_kwargs = transport_kwargs
        self._sync_session = niquests.Session(**self._transport_kwargs)
        self._async_session: Optional[niquests.AsyncSession] = None
        logging.info(f"HttpTransport initialized with options: {transport_kwargs}")

    def _ensure_async_session(self) -> niquests.AsyncSession:
        """Lazily initializes the async session."""
        if self._async_session is None:
            logging.info("Initializing async session.")
            self._async_session = niquests.AsyncSession(**self._transport_kwargs)
        return self._async_session

    def request(
        self,
        method: str,
        url: str,
        **kwargs: Any,
    ) -> Optional[Dict[str, Any]]:
        """Makes a synchronous HTTP request and returns the JSON response."""
        try:
            logging.info(f"Executing sync {method} request to {url}")
            # Type annotation helps the type checker understand the return type
            response: Response = self._sync_session.request(method, url, **kwargs)  # type: ignore[misc]
            response.raise_for_status()
            return response.json()
        except niquests.exceptions.RequestException as e:
            logging.error(f"HTTP Request failed: {e}")
            return None

    async def arequest(
        self,
        method: str,
        url: str,
        **kwargs: Any,
    ) -> Optional[Dict[str, Any]]:
        """Makes an asynchronous HTTP request and returns the JSON response."""
        session = self._ensure_async_session()
        try:
            logging.info(f"Executing async {method} request to {url}")
            # Type annotation helps the type checker understand the return type
            response: Response = await session.request(method, url, **kwargs)  # type: ignore[misc]
            response.raise_for_status()
            return response.json()
        except niquests.exceptions.RequestException as e:
            logging.error(f"Async HTTP Request failed: {e}")
            return None

    def close(self) -> None:
        """Closes the synchronous session."""
        self._sync_session.close()

    async def aclose(self) -> None:
        """Closes the asynchronous session if it exists."""
        if self._async_session:
            await self._async_session.close()