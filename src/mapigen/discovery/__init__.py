"""Discovery client for services and operations."""
from __future__ import annotations
from typing import List, Optional

from mapigen.models import ServiceInfo, Operation

from . import services
from . import operations


class DiscoveryClient:
    """Provides methods for discovering available services and their details."""

    # Service-level methods
    @staticmethod
    def list_services() -> list[str]:
        return services.list_services()

    @staticmethod
    def service_exists(service: str) -> bool:
        return services.service_exists(service)

    @staticmethod
    def get_service_info(service: str) -> ServiceInfo:
        return services.get_service_info(service)

    @staticmethod
    def get_auth_types(service: str) -> list[str]:
        return services.get_auth_types(service)

    @staticmethod
    def get_primary_auth(service: str) -> str:
        return services.get_primary_auth(service)

    # Operation-level methods
    @staticmethod
    def list_operations(service: str) -> List[str]:
        return operations.list_operations(service)

    @staticmethod
    def operation_exists(service: str, operation: str) -> bool:
        return operations.operation_exists(service, operation)

    @staticmethod
    def get_operation(service: str, operation: str) -> Optional[Operation]:
        return operations.get_operation(service, operation)