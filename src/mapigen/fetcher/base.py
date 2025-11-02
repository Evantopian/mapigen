from __future__ import annotations
from typing import Protocol, Any, Mapping
import structlog
from niquests import Response, Session

logger = structlog.get_logger(__name__)


class HTTPClient(Protocol):
    """Minimal protocol for HTTP clients compatible with Niquests."""
    headers: Mapping[str, str]

    def __enter__(self) -> HTTPClient: ...
    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None: ...
    def get(self, url: str, *, timeout: int = 30) -> Response: ...
    def close(self) -> None: ...


class BaseFetcher:
    """Abstract fetcher providing common HTTP session utilities and logging."""

    def __init__(self, user_agent: str = "mapigen-fetcher/2.0") -> None:
        self._user_agent = user_agent
        self.logger = structlog.get_logger(self.__class__.__name__)

    def create_session(self) -> HTTPClient:
        """Create and configure an HTTP session."""
        session = Session()
        session.headers.update({"User-Agent": self._user_agent}) # type: ignore
        return session # type: ignore

    def fetch_raw(self, url: str, *, timeout: int = 30) -> bytes:
        """Fetch raw bytes from a URL."""
        self.logger.debug("Fetching raw content", url=url, timeout=timeout)
        with self.create_session() as session:
            resp = session.get(url, timeout=timeout)
            resp.raise_for_status()
            if not resp.content:
                raise ValueError(f"Received empty response for URL: {url}")
            return resp.content
