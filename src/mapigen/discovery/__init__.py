"""Discovery client for services and operations."""
from __future__ import annotations
from typing import List, Optional

from mapigen.models import ApiInfo, Operation

from . import services
from . import operations


class DiscoveryClient:
    """Provides methods for discovering available services and their details."""

    # Provider-level methods
    @staticmethod
    def list_providers() -> list[str]:
        return services.list_providers()

    @staticmethod
    def provider_exists(provider: str) -> bool:
        return services.provider_exists(provider)

    # API-level methods
    @staticmethod
    def list_apis(provider: str) -> list[str]:
        return services.list_apis(provider)

    @staticmethod
    def api_exists(provider: str, api: str) -> bool:
        return services.api_exists(provider, api)

    @staticmethod
    def get_api_info(provider: str, api: str) -> ApiInfo:
        return services.get_api_info(provider, api)

    # Operation-level methods
    @staticmethod
    def list_operations(provider: str, api: str, source: Optional[str] = None) -> List[str]:
        if source is None:
            api_info = services.get_api_info(provider, api)
            if not api_info.sources:
                raise ValueError(f"No sources found for API '{api}' of provider '{provider}'.")
            source = api_info.sources[0]
        return operations.list_operations(provider, api, source)

    @staticmethod
    def operation_exists(provider: str, api: str, operation: str, source: Optional[str] = None) -> bool:
        if source is None:
            api_info = services.get_api_info(provider, api)
            if not api_info.sources:
                return False
            source = api_info.sources[0]
        return operations.operation_exists(provider, api, source, operation)

    @staticmethod
    def get_operation(provider: str, api: str, operation: str, source: Optional[str] = None) -> Optional[Operation]:
        if source is None:
            api_info = services.get_api_info(provider, api)
            if not api_info.sources:
                return None
            source = api_info.sources[0]
        return operations.get_operation(provider, api, source, operation)
