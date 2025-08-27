"""Discovery client for services and operations."""
from __future__ import annotations
from typing import Any

from . import services


class DiscoveryClient:
    """Provides methods for discovering available services and their details."""

    @staticmethod
    def list_services() -> list[str]:
        return services.list_services()

    @staticmethod
    def service_exists(service: str) -> bool:
        return services.service_exists(service)

    @staticmethod
    def get_service_info(service: str) -> dict[str, Any]:
        return services.get_service_info(service)

    @staticmethod
    def get_auth_types(service: str) -> list[str]:
        return services.get_auth_types(service)

    @staticmethod
    def get_primary_auth(service: str) -> str:
        return services.get_primary_auth(service)
