from __future__ import annotations
import json
import logging
from functools import lru_cache
from pathlib import Path
from typing import Any, Optional

import requests

from mapigen.auth.providers import AuthProvider
from mapigen.discovery import services as service_discovery
from mapigen.proxy import ServiceProxy
from mapigen.tools.utils import load_metadata

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


class Mapi:
    """A metadata-driven API client."""

    def __init__(
        self,
        base_url: Optional[str] = None,
        auth_provider: Optional[AuthProvider] = None,
    ):
        self._service_cache: dict[str, dict[str, Any]] = {}
        self.base_url = base_url
        self.auth_provider = auth_provider
        # Load the list of available services for the proxy
        self._services = service_discovery.list_services()

    def __getattribute__(self, name: str) -> Any:
        """Overrides attribute access to enable dynamic service proxies."""
        # Use a try/except block to avoid RecursionError when accessing self._services
        try:
            if name in object.__getattribute__(self, "_services"):
                return ServiceProxy(self, name)
        except AttributeError:
            # This can happen during initialization before _services is set
            pass
        return object.__getattribute__(self, name)

    def set_auth_provider(self, provider: AuthProvider) -> None:
        """Sets the authentication provider for this client instance."""
        self.auth_provider = provider

    def with_auth(self, provider: AuthProvider) -> Mapi:
        """Creates a new client instance with the specified authentication provider."""
        return Mapi(base_url=self.base_url, auth_provider=provider)

    @lru_cache(maxsize=128)
    def _load_service_data(self, service_name: str) -> dict[str, Any]:
        """Loads the metadata for a single service, checking for uncompressed or compressed files."""
        data_dir = Path(__file__).parent / "data"
        service_dir = data_dir / service_name

        uncompressed_path = service_dir / f"{service_name}.utilize.json"
        compressed_path = service_dir / f"{service_name}.utilize.json.lz4"

        if uncompressed_path.exists():
            logging.info(f"Loading uncompressed service data for '{service_name}'.")
            return json.loads(uncompressed_path.read_text())
        elif compressed_path.exists():
            logging.info(f"Loading compressed service data for '{service_name}'.")
            return load_metadata(compressed_path)
        else:
            raise FileNotFoundError(
                f"Service data for '{service_name}' not found. Please ensure data is populated."
            )

    def execute(
        self, service: str, operation: str, **kwargs: Any
    ) -> Optional[dict[str, Any]]:
        """Executes a generic API operation."""
        try:
            service_data = self._load_service_data(service)
        except FileNotFoundError as e:
            logging.error(f"Could not load service data for '{service}'. {e}")
            return None

        op_details: Optional[dict[str, Any]] = service_data.get("operations", {}).get(
            operation
        )
        if not op_details:
            logging.error(f"Operation '{operation}' not found in service '{service}'.")
            return None

        # Determine the base URL
        base_url: Optional[str] = self.base_url
        if not base_url:
            servers: list[dict[str, Any]] = service_data.get("servers", [])
            if not servers:
                logging.error(
                    f"No server URL configured for service '{service}' and no base_url provided."
                )
                return None
            base_url = servers[0].get("url")

        path_params: dict[str, Any] = {}
        query_params: dict[str, Any] = {}
        body_params: dict[str, Any] = {}
        headers: dict[str, str] = {}

        # Apply authentication if a provider is set
        if self.auth_provider:
            headers.update(self.auth_provider.get_auth_headers())
            query_params.update(self.auth_provider.get_auth_params())

        for param_ref in op_details.get("parameters", []):
            param_details: dict[str, Any]
            if "$ref" in param_ref:
                ref_path: str = param_ref["$ref"]
                component_name: str = ref_path.split("/")[-1]
                param_details = (
                    service_data.get("components", {})
                    .get("parameters", {})
                    .get(component_name, {})
                )
            else:
                param_details = param_ref

            param_name: Optional[str] = param_details.get("name")
            if param_name in kwargs:
                value: Any = kwargs[param_name]
                param_in: Optional[str] = param_details.get("in")
                if param_in == "path":
                    path_params[param_name] = value
                elif param_in == "query":
                    query_params[param_name] = value
                elif param_in == "body":
                    body_params[param_name] = value

        # Construct the full URL
        path_template: str = op_details.get("path", "")
        final_path: str = path_template.format(**path_params)
        full_url: str = f"{base_url.rstrip('/') if base_url else ''}{final_path}"

        # Execute the request
        try:
            logging.info(f"Executing {op_details.get('method')} request to {full_url}")
            response = requests.request(
                method=op_details.get("method", "GET"),
                url=full_url,
                params=query_params,
                headers=headers,
                json=body_params,
            )
            response.raise_for_status()  # Raise an exception for bad status codes
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"HTTP Request failed: {e}")
            return None
