"""Discovery client for services and operations."""
from __future__ import annotations
from typing import List

from mapigen.models import ServiceMetadata
from . import services


class DiscoveryClient:
    """Provides methods for discovering available services and their details."""

    # --- API & Source Level Methods ---
    @staticmethod
    def list_apis() -> List[str]:
        return services.list_apis()

    @staticmethod
    def list_sources_for_api(api_name: str) -> List[str]:
        return services.list_sources_for_api(api_name)

    # --- Service Key Level Methods ---
    @staticmethod
    def service_exists(service_key: str) -> bool:
        return services.service_exists(service_key)

    @staticmethod
    def get_service_details(service_key: str) -> ServiceMetadata:
        return services.get_service_details(service_key)

    # --- Path and Key Utilities ---
    @staticmethod
    def parse_service_key(service_key: str) -> tuple[str, str, str]:
        return services.parse_service_key(service_key)
    
    @staticmethod
    def get_service_path(provider: str, source: str, api: str):
        return services.get_service_path(provider, source, api)

    
