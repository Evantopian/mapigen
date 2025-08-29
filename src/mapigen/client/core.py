from __future__ import annotations
import logging
import time
import sys
from functools import lru_cache
from typing import Any, Optional, Dict, Union

import structlog
from niquests.auth import AuthBase
from niquests.exceptions import RequestException
from niquests.models import Response

from ..auth_helpers import AuthHelpers
from ..discovery import DiscoveryClient
from ..http.transport import HttpTransport
import msgspec
from ..models import ServiceData, Parameter, ParameterRef
from ..proxy import ServiceProxy
from ..cache.storage import load_service_from_disk
from ..validation.schemas import build_and_validate_parameters

from .config import RequestOptions, RequestConfig, ResponseMetadata
from .exceptions import MapiError

# Configure structlog
structlog.configure(
    processors=[
        structlog.processors.add_log_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.JSONRenderer(),
    ],
    logger_factory=structlog.stdlib.LoggerFactory(),
    wrapper_class=structlog.stdlib.BoundLogger,
    cache_logger_on_first_use=True,
)

log = structlog.get_logger()

class Mapi:
    auth = AuthHelpers

    def __init__(
        self,
        base_url: Optional[str] = None,
        auth: Optional[Union[AuthBase, tuple[Any, Any], str]] = None,
        default_timeout: float = 30.0,
        log_level: str = "INFO",
        validate_on_execute: bool = True,
        **transport_kwargs: Any,
    ) -> None:
        self.base_url = base_url
        self.auth = auth
        self.default_timeout = default_timeout
        self.http_client = HttpTransport(**transport_kwargs)
        self.discovery = DiscoveryClient()
        self._services = self.discovery.list_services()
        self.validate_on_execute = validate_on_execute
        logging.basicConfig(
            level=getattr(logging, log_level.upper(), logging.INFO),
            stream=sys.stdout,
        )

    def __getattribute__(self, name: str) -> Any:
        try:
            if name in object.__getattribute__(self, "_services"):
                return ServiceProxy(self, name)
        except AttributeError:
            pass
        return object.__getattribute__(self, name)

    @lru_cache(maxsize=128)
    def _load_service_data(self, service_name: str) -> ServiceData:
        try:
            # The data is now decoded into a ServiceData object with version validation
            return load_service_from_disk(service_name)
        except FileNotFoundError as e:
            raise MapiError(f"Service '{service_name}' not found", service=service_name, error_type="sdk", original_exception=e) from e
        except msgspec.ValidationError as e:
            raise MapiError(
                f"Service data for '{service_name}' is invalid. "
                f"Please regenerate the service data. Error: {e}", service=service_name, error_type="sdk", original_exception=e
            ) from e

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
            return exception.error_type, "client"
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
        if self.validate_on_execute:
            try:
                build_and_validate_parameters(service, operation, kwargs)
            except MapiError as e:
                log.error("validation_failed", service=service, operation=operation, error=str(e))
                raise e

        service_data = self._load_service_data(service)
        op_details = service_data.operations.get(operation)
        if not op_details:
            raise MapiError(f"Operation '{operation}' not found", service=service, operation=operation, error_type="sdk")

        base_url = self.base_url or (service_data.servers[0].url if service_data.servers else None)
        if not base_url:
            raise MapiError(f"No server URL found for service '{service}'", service=service, operation=operation, error_type="sdk")

        path_params, query_params, body_params, headers = {}, {}, {}, {}
        
        for param_union in op_details.parameters:
            param_details: Parameter
            if isinstance(param_union, ParameterRef):
                # Resolve the reference from the components
                param_details = service_data.components.parameters[param_union.component_name]
            else:
                # It's an inline parameter
                param_details = param_union

            if param_details.name in kwargs:
                value = kwargs[param_details.name]
                if param_details.in_ == "path":
                    path_params[param_details.name] = value
                elif param_details.in_ == "query":
                    query_params[param_details.name] = value
                # Note: 'body' params are handled differently in OpenAPI 3 vs 2.
                # This implementation assumes a simplified model where named body params are collected.
                # A more robust implementation would handle requestBody schemas.
                elif param_details.in_ == "body":
                    body_params[param_details.name] = value

        try:
            final_path = op_details.path.format(**path_params)
        except KeyError as e:
            raise MapiError(f"Missing required path parameter: {e}", service=service, operation=operation, error_type="validation", original_exception=e) from e
            
        full_url = f"{base_url.rstrip('/')}{final_path}"
        options = request_options or RequestOptions(timeout=self.default_timeout)
        
        return RequestConfig(method=op_details.method, url=full_url, params=query_params,
                           headers=headers, json_body=body_params, options=options)

    def execute(self, service: str, operation: str, **kwargs: Any) -> Dict[str, Union[Dict[str, Any], ResponseMetadata, None]]:
        start_time = time.time()
        response: Optional[Response] = None
        try:
            config = self._prepare_request_config(service, operation, RequestOptions(), **kwargs)
            request_kwargs: Dict[str, Any] = {
                "method": config.method, "url": config.url, "params": config.params,
                "headers": config.headers, "timeout": config.options.timeout, "auth": self.auth,
            }
            if config.method != 'GET' and config.json_body:
                request_kwargs["json"] = config.json_body

            response = self.http_client.request(**request_kwargs)
            result = response.json()
            return {"data": result, "metadata": self._create_metadata(service, operation, start_time, response)}
        except Exception as e:
            response = getattr(e, 'response', None)
            log.error("request_failed", service=service, operation=operation, error=str(e), exc_info=True)
            return {"data": None, "metadata": self._create_metadata(service, operation, start_time, response, e)}

    async def aexecute(self, service: str, operation: str, **kwargs: Any) -> Dict[str, Union[Dict[str, Any], ResponseMetadata, None]]:
        start_time = time.time()
        response: Optional[Response] = None
        try:
            config = self._prepare_request_config(service, operation, RequestOptions(), **kwargs)
            request_kwargs: Dict[str, Any] = {
                "method": config.method, "url": config.url, "params": config.params,
                "headers": config.headers, "timeout": config.options.timeout, "auth": self.auth,
            }
            if config.method != 'GET' and config.json_body:
                request_kwargs["json"] = config.json_body

            response = await self.http_client.arequest(**request_kwargs)
            result = response.json()
            return {"data": result, "metadata": self._create_metadata(service, operation, start_time, response)}
        except Exception as e:
            response = getattr(e, 'response', None)
            log.error("request_failed", service=service, operation=operation, error=str(e), exc_info=True)
            return {"data": None, "metadata": self._create_metadata(service, operation, start_time, response, e)}
