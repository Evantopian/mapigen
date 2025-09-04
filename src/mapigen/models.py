# src/mapigen/models.py
from __future__ import annotations
from typing import Any, Dict, List, Optional, Union, Literal
from typing_extensions import Annotated
import msgspec
from msgspec import Meta, field

# Base struct with optimal performance configuration
class BaseStruct(msgspec.Struct, frozen=True):
    """Base struct with optimal performance configuration."""
    pass

# Custom exception types for model-related errors
class MapiModelError(Exception): ...
class ValidationError(MapiModelError): ...
class SerializationError(MapiModelError): ...

# Common validation constraints
PositiveInt = Annotated[int, Meta(ge=1)]
NonEmptyStr = Annotated[str, Meta(min_length=1)]
HttpMethod = Literal["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS", "TRACE"]
ParameterLocation = Literal["query", "path", "header", "cookie", "body"]

# --- Parameter Models (for Tagged Union) ---

class Parameter(BaseStruct, frozen=True, tag='inline'):
    """Represents a fully defined API parameter."""
    name: NonEmptyStr
    in_: ParameterLocation = field(name="in")
    schema_: Dict[str, Any] = field(name="schema")
    description: str = ""
    required: bool = False

class ParameterRef(BaseStruct, frozen=True, tag='ref'):
    """Reference to a reusable parameter component."""
    ref: NonEmptyStr = field(name="$ref")
    
    @property
    def component_name(self) -> str:
        return self.ref.split("/")[-1]

ParameterUnion = Union[Parameter, ParameterRef]

# --- Operation, Component, and Service Models ---

class Server(BaseStruct, frozen=True):
    url: NonEmptyStr
    description: str = ""
    variables: Optional[Dict[str, Any]] = None

class Operation(BaseStruct, frozen=True):
    """API operation with comprehensive metadata."""
    service: NonEmptyStr
    path: NonEmptyStr
    method: HttpMethod
    operation_id: Optional[str] = field(name="operationId", default=None)
    summary: str = ""
    description: str = ""
    parameters: List[ParameterUnion] = msgspec.field(default_factory=list)
    deprecated: bool = False

class Components(BaseStruct, frozen=True):
    """Reusable OpenAPI components."""
    parameters: Dict[str, Parameter] = msgspec.field(default_factory=dict)
    schemas: Dict[str, Dict[str, Any]] = msgspec.field(default_factory=dict)

class ServiceData(BaseStruct, frozen=True):
    """Complete processed service data structure (utilize.json)."""
    format_version: Annotated[int, Meta(ge=3)]
    service_name: NonEmptyStr
    servers: List[Server]
    components: Components
    operations: Dict[str, Operation]

# --- Registry Models ---

class ServiceMetadata(BaseStruct, frozen=True):
    """Service metadata for the new registry format."""
    resolvable: bool
    tested: bool
    last_updated: str = field(name="lastUpdated")

class ServiceRegistry(BaseStruct, frozen=True):
    """Complete service registry index."""
    version: NonEmptyStr
    generated_at: str  # ISO 8601 timestamp
    services: Dict[str, ServiceMetadata]
