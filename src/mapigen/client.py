from __future__ import annotations
import logging
from functools import lru_cache
from typing import Any, Optional, NamedTuple, Dict, Union

from niquests.auth import AuthBase

from mapigen.discovery import DiscoveryClient
from mapigen.http.transport import HttpTransport
from mapigen.proxy import ServiceProxy
from mapigen.cache.storage import load_service_from_disk
from mapigen.validation.schemas import build_and_validate_parameters
from jsonschema.exceptions import ValidationError

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class RequestConfig(NamedTuple):
    """A container for the prepared request details."""
    method: str
    url: str
    params: Dict[str, Any]
    headers: Dict[str, Any]
    json_body: Dict[str, Any]

class Mapi:
    """A metadata-driven API client."""

    def __init__(
        self,
        base_url: Optional[str] = None,
        auth: Optional[Union[AuthBase, tuple[Any, Any], str]] = None,
        **transport_kwargs: Any,
    ) -> None:
        self._service_cache: Dict[str, Dict[str, Any]] = {}
        self.base_url = base_url
        self.http_client = HttpTransport(auth=auth, **transport_kwargs)
        self.discovery = DiscoveryClient()
        self._services = self.discovery.list_services()

    def __getattribute__(self, name: str) -> Any:
        """Overrides attribute access to enable dynamic service proxies."""
        try:
            if name in object.__getattribute__(self, "_services"):
                return ServiceProxy(self, name)
        except AttributeError:
            pass
        return object.__getattribute__(self, name)

    @lru_cache(maxsize=128)
    def _load_service_data(self, service_name: str) -> Dict[str, Any]:
        """Loads the metadata for a single service from the cache/disk."""
        return load_service_from_disk(service_name)

    def _prepare_request_config(
        self, service: str, operation: str, **kwargs: Any
    ) -> Optional[RequestConfig]:
        """Prepares the configuration for an API request."""
        try:
            service_data = self._load_service_data(service)
        except FileNotFoundError as e:
            logging.error(f"Could not load service data for '{service}'. {e}")
            return None

        try:
            build_and_validate_parameters(service_data, operation, kwargs)
        except ValidationError as e:
            logging.error(f"Parameter validation failed for {service}.{operation}: {e.message}")
            return None
        except ValueError as e:
            logging.error(f"Could not validate parameters: {e}")
            return None

        op_details = service_data.get("operations", {}).get(operation)
        if not op_details:
            logging.error(f"Operation '{operation}' not found in service '{service}'.")
            return None

        base_url = self.base_url or next((s.get("url") for s in service_data.get("servers", [])), None)
        if not base_url:
            logging.error(f"No server URL found for service '{service}'.")
            return None

        path_params: Dict[str, Any] = {}
        query_params: Dict[str, Any] = {}
        body_params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}

        for param_ref in op_details.get("parameters", []):
            param_details = param_ref
            if "$ref" in param_ref:
                ref_path = param_ref["$ref"]
                component_name = ref_path.split("/")[-1]
                param_details = service_data.get("components", {}).get("parameters", {}).get(component_name, {})

            param_name = param_details.get("name")
            if param_name in kwargs:
                value = kwargs[param_name]
                param_in = param_details.get("in")
                if param_in == "path":
                    path_params[param_name] = value
                elif param_in == "query":
                    query_params[param_name] = value
                elif param_in == "body":
                    body_params[param_name] = value

        final_path = op_details.get("path", "").format(**path_params)
        full_url = f"{base_url.rstrip('/')}{final_path}"

        return RequestConfig(
            method=op_details["method"],
            url=full_url,
            params=query_params,
            headers=headers,
            json_body=body_params,
        )

    def execute(
        self, service: str, operation: str, **kwargs: Any
    ) -> Optional[Dict[str, Any]]:
        """Executes a synchronous API operation."""
        config = self._prepare_request_config(service, operation, **kwargs)
        if not config:
            return None
        request_kwargs = {
            "method": config.method,
            "url": config.url,
            "params": config.params,
            "headers": config.headers,
        }
        if config.method != 'GET':
            request_kwargs["json"] = config.json_body

        return self.http_client.request(**request_kwargs)

    async def aexecute(
        self, service: str, operation: str, **kwargs: Any
    ) -> Optional[Dict[str, Any]]:
        """Executes an asynchronous API operation."""
        config = self._prepare_request_config(service, operation, **kwargs)
        if not config:
            return None
        request_kwargs = {
            "method": config.method,
            "url": config.url,
            "params": config.params,
            "headers": config.headers,
        }
        if config.method != 'GET':
            request_kwargs["json"] = config.json_body

        return await self.http_client.arequest(**request_kwargs)