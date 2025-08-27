"""Dynamic proxy for enabling client.service.operation() syntax."""
from __future__ import annotations
from typing import TYPE_CHECKING, Any, Generator

if TYPE_CHECKING:
    from mapigen.client import Mapi


class OperationProxy:
    """Represents a callable API operation with sync and async capabilities."""

    def __init__(self, client: Mapi, service_name: str, operation_name: str):
        self._client = client
        self._service_name = service_name
        self._operation_name = operation_name

    def __call__(self, **kwargs: Any) -> Any:
        """Executes the API call synchronously."""
        return self._client.execute(self._service_name, self._operation_name, **kwargs)

    def __await__(self) -> Generator[Any, None, Any]:
        """Allows awaiting the operation directly for parameter-less calls."""
        return self._client.aexecute(self._service_name, self._operation_name).__await__()

    async def aexecute(self, **kwargs: Any) -> Any:
        """Executes the API call asynchronously with parameters."""
        return await self._client.aexecute(
            self._service_name, self._operation_name, **kwargs
        )


class ServiceProxy:
    """Represents a service and provides dynamic access to its operations."""

    def __init__(self, client: Mapi, service_name: str):
        self._client = client
        self._service_name = service_name

    def __getattr__(self, name: str) -> OperationProxy:
        """Dynamically creates a callable operation proxy."""
        return OperationProxy(self._client, self._service_name, name)