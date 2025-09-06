from __future__ import annotations
import msgspec
from functools import lru_cache
from pathlib import Path

from ..models import ServiceRegistry, ApiInfo

# Define path to the service registry
REGISTRY_PATH = Path(__file__).resolve().parent.parent / "services.json"

@lru_cache(maxsize=1)
def _load_registry() -> ServiceRegistry:
    """Loads the service registry from services.json, cached for performance."""
    if not REGISTRY_PATH.exists():
        raise FileNotFoundError(
            f"Service registry not found at {REGISTRY_PATH}. "
            "Please run the data population script."
        )
    return msgspec.json.decode(REGISTRY_PATH.read_bytes(), type=ServiceRegistry)

def list_providers() -> list[str]:
    """Returns a list of all available provider keys."""
    registry = _load_registry()
    return list(registry.providers.keys())

def provider_exists(provider: str) -> bool:
    """Checks if a given provider exists in the registry."""
    registry = _load_registry()
    return provider in registry.providers

def list_apis(provider: str) -> list[str]:
    """Returns a list of all available API keys for a given provider."""
    registry = _load_registry()
    if provider in registry.providers:
        return list(registry.providers[provider].keys())
    return []

def api_exists(provider: str, api: str) -> bool:
    """Checks if an API exists for a given provider."""
    registry = _load_registry()
    return provider in registry.providers and api in registry.providers[provider]

def get_api_info(provider: str, api: str) -> ApiInfo:
    """Returns the entire metadata object for a single API."""
    registry = _load_registry()
    api_info = registry.providers.get(provider, {}).get(api)
    if api_info is None:
        raise ValueError(f"API '{api}' not found for provider '{provider}'.")
    return api_info