"""Service discovery methods for reading from the service registry."""
from __future__ import annotations
import msgspec
from functools import lru_cache
from pathlib import Path
from typing import List, Tuple

from ..models import ServiceRegistry, ServiceMetadata

# Define paths
ROOT_DIR = Path(__file__).resolve().parent.parent.parent.parent
SRC_DIR = ROOT_DIR / "src" / "mapigen"
DATA_DIR = SRC_DIR / "data"
REGISTRY_PATH = SRC_DIR / "services.json"

@lru_cache(maxsize=1)
def _load_registry() -> ServiceRegistry:
    """Loads the service registry from services.json, cached for performance."""
    if not REGISTRY_PATH.exists():
        raise FileNotFoundError(
            f"Service registry not found at {REGISTRY_PATH}. "
            "Please run the data population script."
        )
    return msgspec.json.decode(REGISTRY_PATH.read_bytes(), type=ServiceRegistry)

def list_apis() -> List[str]:
    """Returns a unique list of all available API names (the middle part of the key)."""
    registry = _load_registry()
    apis = {key.split(":")[1] for key in registry.services.keys()}
    return sorted(list(apis))

def list_sources_for_api(api_name: str) -> List[str]:
    """Returns a list of available sources for a given API name."""
    registry = _load_registry()
    sources = {key.split(":")[2] for key in registry.services.keys() if key.split(":")[1] == api_name}
    return sorted(list(sources))

def service_exists(service_key: str) -> bool:
    """Checks if a given service key exists in the registry."""
    registry = _load_registry()
    return service_key in registry.services

def get_service_details(service_key: str) -> ServiceMetadata:
    """Returns the metadata dictionary for a single service key."""
    registry = _load_registry()
    details = registry.services.get(service_key)
    if details is None:
        raise ValueError(f"Service key '{service_key}' not found in registry.")
    return details

def parse_service_key(service_key: str) -> Tuple[str, str, str]:
    """Parses a service key into its provider, api, and source components."""
    try:
        provider, api, source = service_key.split(":")
        return provider, api, source
    except (ValueError, IndexError):
        raise ValueError(f"Invalid service key format: '{service_key}'. Expected 'provider:api:source'.")

def get_service_path(provider: str, source: str, api: str) -> Path:
    """Constructs the expected path to a processed utilize.json.zst file."""
    # Note: The source from the key for Postman is the workspace name.
    return DATA_DIR / provider / source / api / f"{api}.utilize.json.zst"
