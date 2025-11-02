from __future__ import annotations
import time
from pathlib import Path
import structlog
from niquests import Timeout, ConnectionError  # type: ignore

from mapigen.fetcher.base import BaseFetcher
from mapigen.models import ErrorRecord, ErrorStage
from mapigen.types import PathLike
from mapigen.utils.compression import compress_zstd

logger = structlog.get_logger(__name__)


class HTTPFetcher(BaseFetcher):
    """Generic HTTP-based fetcher for OpenAPI specs (GitHub, custom, etc.)."""

    def __init__(self, *, compression_level: int = 7, user_agent: str = "mapigen-fetcher/2.0") -> None:
        super().__init__(user_agent)
        self.compression_level = compression_level

    def fetch_spec(
        self,
        provider: str,
        api: str,
        url: str,
        output_dir: PathLike,
        *,
        timeout: int = 30,
        compress: bool = True,
    ) -> dict[str, str | float | None]:
        """Fetch any OpenAPI spec over HTTP and store it compressed locally."""
        start = time.perf_counter()
        output_dir = Path(output_dir) / provider / api
        output_dir.mkdir(parents=True, exist_ok=True)

        spec_path = output_dir / f"{api}.openapi"
        spec_path_zst = spec_path.with_suffix(".json.zst")

        try:
            with self.create_session() as session:
                resp = session.get(url, timeout=timeout)
                resp.raise_for_status()
                content = resp.content
                if not content:
                    raise ValueError("Empty response body")

                if compress:
                    compressed = compress_zstd(content, level=self.compression_level)
                    spec_path_zst.write_bytes(compressed)
                else:
                    spec_path.write_bytes(content)

            elapsed = round(time.perf_counter() - start, 3)
            logger.info("Fetched spec", provider=provider, api=api, duration=elapsed)

            return {
                "status": "success",
                "provider": provider,
                "api": api,
                "url": url,
                "duration_s": elapsed,
                "path": str(spec_path_zst if compress else spec_path),
            }

        except (Timeout, ConnectionError) as e:
            err = ErrorRecord(
                stage=ErrorStage.LOAD,
                message="Network error while fetching spec",
                detail=str(e),
                provider=provider,
                api=api,
            )
            logger.error("HTTP fetch network error", provider=provider, api=api, error=str(e))
            return {"status": "failure", "error": err.message, "detail": err.detail}

        except Exception as e:
            err = ErrorRecord(
                stage=ErrorStage.LOAD,
                message="Unexpected fetch failure",
                detail=str(e),
                provider=provider,
                api=api,
            )
            logger.error("HTTP fetch failure", provider=provider, api=api, error=str(e))
            return {"status": "failure", "error": err.message, "detail": err.detail}
