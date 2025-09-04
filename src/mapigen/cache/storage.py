"""Handles loading service data from the disk cache and in-memory caching."""
from __future__ import annotations
import logging
import threading
from functools import lru_cache
from pathlib import Path
from typing import Callable, Any, Dict, Set

import msgspec
import zstandard as zstd

from ..models import ServiceData


def _load_zstd_metadata(zst_path: Path) -> ServiceData:
    """Loads and decompresses metadata from a zstd file."""
    dctx = zstd.ZstdDecompressor()
    compressed = zst_path.read_bytes()
    decompressed = dctx.decompress(compressed)
    return msgspec.json.decode(decompressed, type=ServiceData)


def load_service_from_disk(service_path: Path) -> ServiceData:
    """Loads the metadata for a single service from a specific file path."""
    uncompressed_path = service_path.with_suffix(".json")
    compressed_path = service_path.with_suffix(".json.zst")

    if uncompressed_path.exists():
        logging.info(f"Loading uncompressed service data from {uncompressed_path}")
        return msgspec.json.decode(uncompressed_path.read_bytes(), type=ServiceData)
    
    if compressed_path.exists():
        logging.info(f"Loading compressed service data from {compressed_path}")
        return _load_zstd_metadata(compressed_path)

    raise FileNotFoundError(
        f"Service data not found at {service_path.parent}. Please ensure data is populated."
    )

class PinnedLRUCache:
    """A thread-safe, pinned LRU cache."""

    def __init__(self, load_func: Callable[[str], Any], pinned_keys: Set[str], maxsize: int):
        self._load_func = load_func
        self._pinned_keys = pinned_keys
        self._pinned_cache: Dict[str, Any] = {}
        self._lock = threading.Lock()

        @lru_cache(maxsize=maxsize)
        def _lru_load_func(key: str) -> Any:
            """This function will be called by the LRU cache when a key is not present."""
            return self._load_func(key)
        
        self._lru_load_func = _lru_load_func

    def get(self, key: str) -> Any:
        """Retrieves an item from the cache, loading it if necessary."""
        if key in self._pinned_keys:
            # Fast path check without lock for already loaded pinned items
            if key in self._pinned_cache:
                return self._pinned_cache[key]
            
            # Slow path with lock to load data for a pinned item
            with self._lock:
                # Double-checked locking pattern to prevent re-loading in concurrent scenarios
                if key not in self._pinned_cache:
                    self._pinned_cache[key] = self._load_func(key)
                return self._pinned_cache[key]
        else:
            return self._lru_load_func(key)

    def clear(self):
        """Clears both the pinned and LRU caches."""
        with self._lock:
            self._pinned_cache.clear()
        self._lru_load_func.cache_clear()

    def info(self):
        """Returns diagnostic information about the cache state."""
        with self._lock:
            return {
                "pinned_keys": self._pinned_keys,
                "pinned_cache_size": len(self._pinned_cache),
                "lru_cache_info": self._lru_load_func.cache_info()
            }