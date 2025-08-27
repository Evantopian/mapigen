from __future__ import annotations
from pathlib import Path
import logging
from functools import lru_cache
from typing import Any, Optional
import requests

from mapigen.tools.utils import load_metadata
from mapigen.discovery import services as service_discovery
from mapigen.proxy import ServiceProxy

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Mapi:
    """A metadata-driven API client."""

    def __init__(self, base_url: Optional[str] = None):
        self._service_cache: dict[str, dict[str, Any]] = {}
        self.base_url = base_url
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

    @lru_cache(maxsize=128)
    def _load_service_data(self, service_name: str) -> dict[str, Any]:
        """Loads the metadata for a single service from its compressed file."""
        data_dir = Path(__file__).parent / "data"
        service_path = data_dir / service_name / f"{service_name}.utilize.json.lz4"
        if not service_path.exists():
            raise FileNotFoundError(f"Service '{service_name}' not found. Please ensure data is populated.")
        return load_metadata(service_path)

    def execute(self, service: str, operation: str, **kwargs: Any) -> Optional[dict[str, Any]]:
        """Executes a generic API operation."""
        try:
            service_data = self._load_service_data(service)
        except FileNotFoundError as e:
            logging.error(f"Could not load service data for '{service}'. {e}")
            return None

        op_details: Optional[dict[str, Any]] = service_data.get("operations", {}).get(operation)
        if not op_details:
            logging.error(f"Operation '{operation}' not found in service '{service}'.")
            return None

        # Determine the base URL
        base_url: Optional[str] = self.base_url
        if not base_url:
            servers: list[dict[str, Any]] = service_data.get("servers", [])
            if not servers:
                logging.error(f"No server URL configured for service '{service}' and no base_url provided.")
                return None
            base_url = servers[0].get("url")

        path_params: dict[str, Any] = {}
        query_params: dict[str, Any] = {}
        body_params: dict[str, Any] = {}

        for param_ref in op_details.get("parameters", []):
            param_details: dict[str, Any]
            if "$ref" in param_ref:
                ref_path: str = param_ref["$ref"]
                component_name: str = ref_path.split("/")[-1]
                param_details = service_data.get("components", {}).get("parameters", {}).get(component_name, {})
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
                json=body_params
            )
            response.raise_for_status()  # Raise an exception for bad status codes
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"HTTP Request failed: {e}")
            return None
