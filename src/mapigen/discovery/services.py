"""Service discovery methods for reading from the service registry."""
from __future__ import annotations
import msgspec
from functools import lru_cache
from pathlib import Path

from ..models import ServiceInfo, ServiceRegistry

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

def list_services() -> list[str]:
    """Returns a list of all available service keys."""
    registry = _load_registry()
    return list(registry.services.keys())

def service_exists(service: str) -> bool:
    """Checks if a given service exists in the registry."""
    registry = _load_registry()
    return service in registry.services

def get_service_info(service: str) -> ServiceInfo:
    """Returns the entire metadata dictionary for a single service."""
    registry = _load_registry()
    service_info = registry.services.get(service)
    if service_info is None:
        raise ValueError(f"Service '{service}' not found in registry.")
    return service_info

def get_auth_types(service: str) -> list[str]:
    """Returns the list of supported auth_types for a service."""
    info = get_service_info(service)
    return info.auth_types

def get_primary_auth(service: str) -> str:
    """Returns the primary_auth method for a service."""
    info = get_service_info(service)
    return info.primary_auth
