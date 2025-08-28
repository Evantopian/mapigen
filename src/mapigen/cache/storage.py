"""Handles loading service data from the disk cache."""
from __future__ import annotations
import orjson as json
import logging
from pathlib import Path
from typing import Any, cast

import lz4.frame  # type: ignore


def _load_compressed_metadata(lz4_path: Path) -> dict[str, Any]:
    """Loads and decompresses metadata from an lz4 file."""
    compressed: bytes = lz4_path.read_bytes()
    decompressed: bytes = lz4.frame.decompress(compressed)  # type: ignore
    text: str = cast(str, decompressed.decode("utf-8"))  # type: ignore
    return json.loads(text)


def load_service_from_disk(service_name: str) -> dict[str, Any]:
    """Loads the metadata for a single service, checking for uncompressed or compressed files."""
    data_dir = Path(__file__).resolve().parent.parent / "data"
    service_dir = data_dir / service_name

    uncompressed_path = service_dir / f"{service_name}.utilize.json"
    compressed_path = service_dir / f"{service_name}.utilize.json.lz4"

    if uncompressed_path.exists():
        logging.info(f"Loading uncompressed service data for '{service_name}' from disk.")
        return json.loads(uncompressed_path.read_text())
    
    if compressed_path.exists():
        logging.info(f"Loading compressed service data for '{service_name}' from disk.")
        return _load_compressed_metadata(compressed_path)

    raise FileNotFoundError(
        f"Service data for '{service_name}' not found. Please ensure data is populated."
    )
