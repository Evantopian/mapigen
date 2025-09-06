from __future__ import annotations
from typing import List, Optional

from ..cache.storage import load_service_from_disk
from ..models import Operation

def list_operations(provider: str, api: str, source: str) -> List[str]:
    """Lists all operation keys for a given service."""
    try:
        service_data = load_service_from_disk(provider, api, source)
        return list(service_data.operations.keys())
    except FileNotFoundError:
        return []

def operation_exists(provider: str, api: str, source: str, operation: str) -> bool:
    """Checks if an operation exists for a given service."""
    try:
        service_data = load_service_from_disk(provider, api, source)
        return operation in service_data.operations
    except FileNotFoundError:
        return False

def get_operation(provider: str, api: str, source: str, operation: str) -> Optional[Operation]:
    """Gets the full details for a specific operation."""
    try:
        service_data = load_service_from_disk(provider, api, source)
        return service_data.operations.get(operation)
    except FileNotFoundError:
        return None