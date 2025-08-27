from __future__ import annotations
import logging
import time
from functools import lru_cache
from typing import Any, Optional, Dict, Union

from niquests.auth import AuthBase
from niquests.exceptions import RequestException
from niquests.models import Response

from ..discovery import DiscoveryClient
from ..http.transport import HttpTransport
from ..proxy import ServiceProxy
from ..cache.storage import load_service_from_disk
from ..validation.schemas import build_and_validate_parameters
from jsonschema import ValidationError as JsonSchemaValidationError

from .config import RequestOptions, RequestConfig, ResponseMetadata
from .exceptions import MapiError, ServiceNotFoundError, OperationNotFoundError, ValidationError, RequestError

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class Mapi:
    def __init__(
        self,
        base_url: Optional[str] = None,
        auth: Optional[Union[AuthBase, tuple[Any, Any], str]] = None,
        default_timeout: float = 30.0,
        **transport_kwargs: Any,
    ) -> None:
        self.base_url = base_url
        self.default_timeout = default_timeout
        self.http_client = HttpTransport(auth=auth, **transport_kwargs)
        self.discovery = DiscoveryClient()
        self._services = self.discovery.list_services()

    def __getattribute__(self, name: str) -> Any:
        try:
            if name in object.__getattribute__(self, "_services"):
                return ServiceProxy(self, name)
        except AttributeError:
            pass
        return object.__getattribute__(self, name)

    @lru_cache(maxsize=128)
    def _load_service_data(self, service_name: str) -> Dict[str, Any]:
        try:
            return load_service_from_disk(service_name)
        except FileNotFoundError as e:
            raise ServiceNotFoundError(f"Service '{service_name}' not found", service=service_name) from e

    def _classify_error(self, exception: Exception, response: Optional[Response] = None) -> tuple[str, str]:
        if isinstance(exception, RequestException):
            status = response.status_code if response is not None else None
            if status == 429:
                return "rate_limit", "transient"
            elif status and 400 <= status < 500:
                return "client_error", "client"
            elif status and 500 <= status < 600:
                return "server_error", "transient"
            return "network_error", "transient"
        if isinstance(exception, MapiError):
            return "sdk_error", "client"
        return "unknown_error", "system"

    def _create_metadata(
        self, service: str, operation: str, start_time: float, response: Optional[Response] = None, error: Optional[Exception] = None
    ) -> ResponseMetadata:
        duration_ms = int((time.time() - start_time) * 1000)
        status = "error" if error else "success"
        http_status = response.status_code if response is not None else None
        error_type, error_category = self._classify_error(error, response) if error else (None, None)

        return ResponseMetadata(
            service=service, operation=operation, duration_ms=duration_ms, status=status,
            http_status=http_status, timestamp=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
            error_type=error_type, error_category=error_category
        )

    def _prepare_request_config(self, service: str, operation: str, 
                               request_options: Optional[RequestOptions] = None, **kwargs: Any) -> RequestConfig:
        service_data = self._load_service_data(service)
        try:
            build_and_validate_parameters(service_data, operation, kwargs)
        except JsonSchemaValidationError as e:
            raise ValidationError(f"Parameter validation failed: {e.message}", service=service, operation=operation) from e

        op_details = service_data.get("operations", {}).get(operation)
        if not op_details:
            raise OperationNotFoundError(f"Operation '{operation}' not found", service=service, operation=operation)

        base_url = self.base_url or next((s.get("url") for s in service_data.get("servers", [])), None)
        if not base_url:
            raise RequestError(f"No server URL found for service '{service}'", service=service, operation=operation)

        path_params, query_params, body_params, headers = {}, {}, {}, {}
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
                if param_in == "path": path_params[param_name] = value
                elif param_in == "query": query_params[param_name] = value
                elif param_in == "body": body_params[param_name] = value

        final_path = op_details.get("path", "").format(**path_params)
        full_url = f"{base_url.rstrip('/')}{final_path}"
        options = request_options or RequestOptions(timeout=self.default_timeout)
        
        return RequestConfig(method=op_details["method"], url=full_url, params=query_params,
                           headers=headers, json_body=body_params, options=options)

    def execute(self, service: str, operation: str, 
                include_metadata: bool = False, **kwargs: Any) -> Union[Dict[str, Any], Dict[str, Union[Dict[str, Any], ResponseMetadata]]]:
        start_time = time.time()
        response: Optional[Response] = None
        try:
            config = self._prepare_request_config(service, operation, RequestOptions(include_metadata=include_metadata), **kwargs)
            request_kwargs: Dict[str, Any] = {
                "method": config.method, "url": config.url, "params": config.params,
                "headers": config.headers, "timeout": config.options.timeout,
            }
            if config.method != 'GET' and config.json_body:
                request_kwargs["json"] = config.json_body

            response = self.http_client.request(**request_kwargs)
            result = response.json()

            if include_metadata:
                return {"data": result, "metadata": self._create_metadata(service, operation, start_time, response)}
            return result
        except Exception as e:
            if include_metadata:
                response = getattr(e, 'response', None)
                return {"data": None, "metadata": self._create_metadata(service, operation, start_time, response, e)}
            raise RequestError(f"Request failed: {str(e)}", service=service, operation=operation) from e

    async def aexecute(self, service: str, operation: str, 
                      include_metadata: bool = False, **kwargs: Any) -> Union[Dict[str, Any], Dict[str, Union[Dict[str, Any], ResponseMetadata]]]:
        start_time = time.time()
        response: Optional[Response] = None
        try:
            config = self._prepare_request_config(service, operation, RequestOptions(include_metadata=include_metadata), **kwargs)
            request_kwargs: Dict[str, Any] = {
                "method": config.method, "url": config.url, "params": config.params,
                "headers": config.headers, "timeout": config.options.timeout,
            }
            if config.method != 'GET' and config.json_body:
                request_kwargs["json"] = config.json_body

            response = await self.http_client.arequest(**request_kwargs)
            result = response.json()

            if include_metadata:
                return {"data": result, "metadata": self._create_metadata(service, operation, start_time, response)}
            return result
        except Exception as e:
            if include_metadata:
                response = getattr(e, 'response', None)
                return {"data": None, "metadata": self._create_metadata(service, operation, start_time, response, e)}
            raise RequestError(f"Request failed: {str(e)}", service=service, operation=operation) from e