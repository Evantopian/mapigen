"""Manages API popularity ranking and tiers."""
from __future__ import annotations
import json
from functools import lru_cache
from pathlib import Path

POPULARITY_PATH = Path(__file__).resolve().parent.parent / "registry" / "popularity.json"

@lru_cache(maxsize=1)
def load_popularity_ranks() -> dict[str, int]:
    """Loads the popularity rank for each service."""
    if not POPULARITY_PATH.exists():
        return {}
    return json.loads(POPULARITY_PATH.read_text())

def get_rank(service: str) -> int:
    """Gets the popularity rank for a single service. Defaults to a low rank."""
    ranks = load_popularity_ranks()
    # Default to 999 for services not in the list
    return ranks.get(service, 999)
