from __future__ import annotations
import time
import json
from pathlib import Path
from typing import Any
import structlog
 
from mapigen.fetcher.base import BaseFetcher, HTTPClient 
from mapigen.models import ErrorRecord, ErrorStage
from mapigen.utils.compression import compress_zstd
from mapigen.types import PathLike, POSTMAN_BASE_URL

logger = structlog.get_logger(__name__)


class PostmanFetcher(BaseFetcher):
    """Handles discovery and fetching of API specs from Postman workspaces."""

    def __init__(self, *, api_key: str, compression_level: int = 7, user_agent: str = "mapigen-fetcher/2.0") -> None:
        super().__init__(user_agent) 
        self.api_key = api_key
        self.compression_level = compression_level

    def create_session(self) -> HTTPClient:
        """Create and configure an HTTP session, injecting the Postman API key."""
        session = super().create_session() 
        session.headers.update({"X-API-Key": self.api_key})  # type: ignore
        return session


    def discover_collections(self, workspaces: list[dict[str, Any]]) -> list[dict[str, str]]:
        """Discover all collections under each workspace entry."""
        results: list[dict[str, str]] = []

        with self.create_session() as session: 
            for ws in workspaces:
                workspace_id = ws["url"]
                provider = ws["provider"]
                url = f"{POSTMAN_BASE_URL}/workspaces/{workspace_id}"

                try:
                    resp = session.get(url, timeout=30)
                    resp.raise_for_status()
                    data = resp.json()
                    collections = data.get("workspace", {}).get("collections", [])
                    
                    for c in collections:
                        name = c.get("name")
                        uid = c.get("uid")
                        if not name or not uid:
                            continue
                        results.append({
                            "provider": provider,
                            "api": name.lower().replace(" ", "-"),
                            "uid": uid,
                        })

                except Exception as e:
                    err = ErrorRecord(
                        stage=ErrorStage.LOAD,
                        message="Failed to discover Postman workspace",
                        detail=str(e),
                        provider=provider,
                        api=workspace_id,
                    )
                    logger.error("Workspace discovery failed", provider=provider, error=str(e))
                    results.append({
                        "provider": provider,
                        "api": workspace_id,
                        "error": err.message,
                    })

        return results


    def fetch_collection(self, collection: dict[str, str], output_dir: PathLike) -> dict[str, str | float | None]:
        """Fetch and transform a single Postman collection into a JSON spec."""
        provider = collection["provider"]
        api = collection["api"]
        uid = collection["uid"]

        output_dir = Path(output_dir) / provider / api
        output_dir.mkdir(parents=True, exist_ok=True)

        zst_path = output_dir / f"{api}.openapi.json.zst"
        url = f"{POSTMAN_BASE_URL}/collections/{uid}/transformations?format=json"

        start = time.perf_counter()
        with self.create_session() as session: 
            try:
                resp = session.get(url, timeout=60)
                resp.raise_for_status()
                data = resp.json()
                output = data.get("output")
                if not output:
                    raise ValueError("Missing 'output' key in Postman response")

                content_bytes = json.dumps(json.loads(output), indent=2).encode("utf-8")
                compressed = compress_zstd(content_bytes, level=self.compression_level)
                zst_path.write_bytes(compressed)

                elapsed = round(time.perf_counter() - start, 3)
                logger.info("Fetched Postman collection", api=api, provider=provider, duration=elapsed)

                return {
                    "status": "success",
                    "provider": provider,
                    "api": api,
                    "uid": uid,
                    "url": url,
                    "duration_s": elapsed,
                    "path": str(zst_path),
                }

            except Exception as e:
                err = ErrorRecord(
                    stage=ErrorStage.LOAD,
                    message="Failed to fetch Postman collection",
                    detail=str(e),
                    provider=provider,
                    api=api,
                )
                logger.error("Collection fetch failed", provider=provider, api=api, error=str(e))
                return {
                    "status": "failure",
                    "provider": provider,
                    "api": api,
                    "url": url,
                    "error": err.message,
                    "detail": err.detail,
                }