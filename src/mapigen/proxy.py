"""Dynamic proxy for enabling client.provider.api(...) syntax."""
from __future__ import annotations
from typing import TYPE_CHECKING, Any, Generator, Dict, Union, Optional

from .client.exceptions import MapiError

if TYPE_CHECKING:
    from mapigen.client import Mapi
    from mapigen.client.config import ResponseMetadata


class ProviderProxy:
    """Represents a provider and provides dynamic access to its APIs."""

    def __init__(self, client: Mapi, provider_name: str):
        self._client = client
        self._provider_name = provider_name

    def __getattr__(self, api_name: str) -> ApiProxy:
        """Dynamically creates a callable API proxy."""
        if not self._client.discovery.api_exists(self._provider_name, api_name):
            raise AttributeError(f"API '{api_name}' not found for provider '{self._provider_name}'.")
        return ApiProxy(self._client, self._provider_name, api_name)


class ApiProxy:
    """Represents a specific API and handles operation calls and source selection."""

    def __init__(self, client: Mapi, provider_name: str, api_name: str, source: Optional[str] = None):
        self._client = client
        self._provider_name = provider_name
        self._api_name = api_name
        self._source = source

    def __call__(self, operation_id: str, **kwargs: Any) -> Dict[str, Union[Dict[str, Any], ResponseMetadata, None]]:
        """Executes the API call synchronously."""
        source_to_use = self._source
        if source_to_use is None:
            api_info = self._client.discovery.get_api_info(self._provider_name, self._api_name)
            if not api_info.sources:
                raise MapiError(f"No sources found for API '{self._api_name}'", service=f"{self._provider_name}/{self._api_name}")
            source_to_use = api_info.sources[0]  # Use first source as default

        return self._client.execute(
            self._provider_name, self._api_name, source_to_use, operation_id, **kwargs
        )

    def __getattr__(self, source_name: str) -> ApiProxy:
        """Returns a new ApiProxy instance configured for a specific source."""
        api_info = self._client.discovery.get_api_info(self._provider_name, self._api_name)
        if source_name not in api_info.sources:
            raise AttributeError(f"Source '{source_name}' not found for API '{self._api_name}'.")
        # Return a new instance of itself with the source explicitly set
        return ApiProxy(self._client, self._provider_name, self._api_name, source=source_name)

    def aexecute(self, operation_id: str, **kwargs: Any) -> Generator[Any, None, Dict[str, Union[Dict[str, Any], ResponseMetadata, None]]]:
        """Allows awaiting the operation directly."""
        source_to_use = self._source
        if source_to_use is None:
            api_info = self._client.discovery.get_api_info(self._provider_name, self._api_name)
            if not api_info.sources:
                raise MapiError(f"No sources found for API '{self._api_name}'", service=f"{self._provider_name}/{self._api_name}")
            source_to_use = api_info.sources[0]

        return self._client.aexecute(
            self._provider_name, self._api_name, source_to_use, operation_id, **kwargs
        ).__await__()