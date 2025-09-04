from __future__ import annotations
import pytest
from unittest.mock import patch, MagicMock
from pathlib import Path
import threading

from mapigen.cache import storage
from mapigen.models import ServiceData


from mapigen.discovery import DiscoveryClient

def test_load_service_from_disk_uncompressed(tmp_path: Path, monkeypatch):
    """Tests that load_service_from_disk can load an uncompressed file."""
    # Use pokeapi as it is small and does not require auth
    service_key = "pokeapi:pokeapi:github"
    discovery = DiscoveryClient()
    provider, api, source = discovery.parse_service_key(service_key)
    service_path = discovery.get_service_path(provider, source, api)
    service_data = storage.load_service_from_disk(service_path)
    assert isinstance(service_data, ServiceData)
    assert service_data.service_name == api

def test_load_service_from_disk_file_not_found():
    """Tests that load_service_from_disk raises FileNotFoundError for a missing service."""
    with pytest.raises(FileNotFoundError):
        storage.load_service_from_disk(Path("/non/existent/path"))

def test_pinned_lru_cache_eviction():
    """Tests that the LRU cache evicts items when maxsize is reached."""
    load_func = MagicMock(side_effect=lambda key: f"data_for_{key}")
    cache = storage.PinnedLRUCache(load_func=load_func, pinned_keys=set(), maxsize=2)

    cache.get("key1")
    cache.get("key2")
    cache.get("key3")  # This should evict key1

    # Check that key1 was evicted
    assert cache._lru_load_func.cache_info().currsize == 2
    with patch.object(cache, '_load_func', wraps=cache._load_func) as spy:
        cache.get("key1")
        spy.assert_called_once_with("key1")

def test_pinned_lru_cache_thread_safety():
    """Tests that the PinnedLRUCache is thread-safe."""
    load_func = MagicMock(side_effect=lambda key: {key: "data"})
    cache = storage.PinnedLRUCache(load_func=load_func, pinned_keys={"pinned1"}, maxsize=5)

    def worker(key):
        for _ in range(100):
            cache.get(key)

    threads = []
    for i in range(10):
        key = f"key{i}"
        if i == 0:
            key = "pinned1"
        thread = threading.Thread(target=worker, args=(key,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    # The load function should be called only once for each key
    assert load_func.call_count == 10