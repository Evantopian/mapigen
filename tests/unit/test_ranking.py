from __future__ import annotations
from unittest.mock import patch

from mapigen.cache import ranking

def test_load_popularity_ranks_file_not_found(monkeypatch):
    """Tests that load_popularity_ranks returns an empty dict when the file is missing."""
    monkeypatch.setattr('pathlib.Path.exists', lambda self: False)
    # Clear the cache to ensure the function is re-run
    ranking.load_popularity_ranks.cache_clear()
    assert ranking.load_popularity_ranks() == {}

def test_get_rank_with_nonexistent_service():
    """Tests that get_rank returns the default rank for a non-existent service."""
    with patch.object(ranking, 'load_popularity_ranks', return_value={'service_a': 1}):
        assert ranking.get_rank('service_b') == 999
