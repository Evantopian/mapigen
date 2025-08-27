"""Service discovery methods for reading from the service registry."""
from __future__ import annotations
import json
from functools import lru_cache
from pathlib import Path
from typing import Any

# Define path to the service registry
REGISTRY_PATH = Path(__file__).resolve().parent.parent / "services.json"

@lru_cache(maxsize=1)
def _load_registry() -> dict[str, Any]:
    """Loads the service registry from services.json, cached for performance."""
    if not REGISTRY_PATH.exists():
        raise FileNotFoundError(
            f"Service registry not found at {REGISTRY_PATH}. "
            "Please run the data population script."
        )
    return json.loads(REGISTRY_PATH.read_text())

def list_services() -> list[str]:
    """Returns a list of all available service keys."""
    registry = _load_registry()
    return list(registry.keys())

def service_exists(service: str) -> bool:
    """Checks if a given service exists in the registry."""
    registry = _load_registry()
    return service in registry

def get_service_info(service: str) -> dict[str, Any]:
    """Returns the entire metadata dictionary for a single service."""
    registry = _load_registry()
    if not service_exists(service):
        raise ValueError(f"Service '{service}' not found in registry.")
    return registry[service]

def get_auth_types(service: str) -> list[str]:
    """Returns the list of supported auth_types for a service."""
    info = get_service_info(service)
    return info.get("auth_types", [])

def get_primary_auth(service: str) -> str:
    """Returns the primary_auth method for a service."""
    info = get_service_info(service)
    return info.get("primary_auth", "none")
