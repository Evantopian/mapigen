"""Handles loading service data from the disk cache."""
from __future__ import annotations
import logging
from pathlib import Path
from typing import Any

import msgspec
import zstandard as zstd

def _load_zstd_metadata(zst_path: Path) -> dict[str, Any]:
    """Loads and decompresses metadata from a zstd file."""
    dctx = zstd.ZstdDecompressor()
    compressed = zst_path.read_bytes()
    decompressed = dctx.decompress(compressed)
    return msgspec.json.decode(decompressed)

def load_service_from_disk(service_name: str) -> dict[str, Any]:
    """Loads the metadata for a single service, checking for uncompressed or compressed files."""
    data_dir = Path(__file__).resolve().parent.parent / "data"
    service_dir = data_dir / service_name

    uncompressed_path = service_dir / f"{service_name}.utilize.json"
    compressed_path = service_dir / f"{service_name}.utilize.json.zst"

    if uncompressed_path.exists():
        logging.info(f"Loading uncompressed service data for '{service_name}' from disk.")
        return msgspec.json.decode(uncompressed_path.read_bytes())
    
    if compressed_path.exists():
        logging.info(f"Loading compressed service data for '{service_name}' from disk.")
        return _load_zstd_metadata(compressed_path)

    raise FileNotFoundError(
        f"Service data for '{service_name}' not found. Please ensure data is populated."
    )
