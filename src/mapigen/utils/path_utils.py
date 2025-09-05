from __future__ import annotations
from pathlib import Path

# This assumes the file is at src/mapigen/utils/path_utils.py
DATA_DIR = Path(__file__).resolve().parent.parent / "data"

def get_data_dir() -> Path:
    """Returns the path to the root data directory."""
    return DATA_DIR

def get_legacy_service_path(service_name: str) -> Path:
    """
    Constructs the path to a service's data directory using the legacy flat structure.
    e.g., data/github
    """
    return get_data_dir() / service_name

def get_service_data_path(provider: str, api: str, source: str) -> Path:
    """
    Deterministically constructs the path to a service's data directory in the new format.
    e.g., data/github/github/rest
    """
    return get_data_dir() / provider / source / api
