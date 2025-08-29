# Mapi Data Models: A Concrete Proposal (v4)

This document proposes a unified, high-performance data model system for the `mapigen` library, incorporating industry best practices and advanced `msgspec` optimizations. This is a living document that refines our architectural approach.

---

## 1. Core Principles & Refinements

This proposal is based on the following principles and includes refinements from our previous discussions.

- **Performance**: We will reuse `Encoder`/`Decoder` instances and configure all structs with `frozen=True`, `gc=False`, and `slots=True` for maximum performance, following `msgspec` best practices.
- **Type Safety**: We will leverage `msgspec`'s built-in validation, `Annotated` constraints for specific fields, and Tagged Unions for handling polymorphic types like parameters.
- **Maintainability**: We will use Python-idiomatic naming (`in_`) and map it to the correct JSON name (`in`) using `msgspec.field`. This keeps the Python code clean while ensuring correct serialization.
- **Separation of Concerns**: Data models will be stateless containers. Logic like caching will be handled in the services that use the models, not in the models themselves. Similarly, we will avoid re-implementing a complex OpenAPI/JSON Schema parser and will keep schema definitions as flexible dictionaries to be handled by dedicated libraries.

---

## 2. The Unified Model System

All models will be defined in a central `src/mapigen/models.py` file.

### 2.1. Base Configuration & Utilities

```python
# src/mapigen/models.py
from __future__ import annotations
from typing import Any, Dict, List, Optional, Union, Literal
from typing_extensions import Annotated
import msgspec
from msgspec import Meta, field

# Base struct with optimal performance configuration
class BaseStruct(msgspec.Struct, frozen=True, gc=False, slots=True):
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
ParameterLocation = Literal["query", "path", "header", "cookie"]
```

### 2.2. Core Data Models

These models define the structure of the processed `utilize.json` files.

```python
# src/mapigen/models.py

# --- Parameter Models (for Tagged Union) ---

class Parameter(BaseStruct):
    """Represents a fully defined API parameter."""
    type: Literal["inline"]  # Tag for the union
    name: NonEmptyStr
    in_: ParameterLocation = field(name="in")
    description: str = ""
    required: bool = False
    # The schema is kept as a dict to be handled by the jsonschema library
    schema_: Dict[str, Any] = field(name="schema")

class ParameterRef(BaseStruct):
    """Reference to a reusable parameter component."""
    type: Literal["ref"]  # Tag for the union
    ref: NonEmptyStr = field(name="$ref")
    
    @property
    def component_name(self) -> str:
        return self.ref.split("/")[-1]

ParameterUnion = Union[Parameter, ParameterRef]

# --- Operation, Component, and Service Models ---

class Server(BaseStruct):
    url: NonEmptyStr
    description: str = ""
    variables: Optional[Dict[str, Any]] = None

class Operation(BaseStruct):
    """API operation with comprehensive metadata."""
    service: NonEmptyStr
    path: NonEmptyStr
    method: HttpMethod
    operation_id: Optional[str] = field(name="operationId", default=None)
    summary: str = ""
    description: str = ""
    parameters: List[ParameterUnion] = msgspec.field(default_factory=list)
    deprecated: bool = False

class Components(BaseStruct):
    """Reusable OpenAPI components."""
    parameters: Dict[str, Parameter] = msgspec.field(default_factory=dict)
    schemas: Dict[str, Dict[str, Any]] = msgspec.field(default_factory=dict)

class ServiceData(BaseStruct):
    """Complete processed service data structure (utilize.json)."""
    format_version: Annotated[int, Meta(ge=3)]
    service_name: NonEmptyStr
    servers: List[Server]
    components: Components
    operations: Dict[str, Operation]
```

### 2.3. Registry Model

This defines the structure of the main `services.json` registry file.

```python
# src/mapigen/models.py

class ServiceInfo(BaseStruct):
    """Service metadata for registry discovery (services.json)."""
    operation_count: PositiveInt
    auth_types: List[str] = msgspec.field(default_factory=list)
    primary_auth: str = "none"
    popularity_rank: PositiveInt

class ServiceRegistry(BaseStruct):
    """Complete service registry index."""
    version: NonEmptyStr
    generated_at: str  # ISO 8601 timestamp
    services: Dict[str, ServiceInfo]
```

---

## 3. Implementation Guide

The refactoring will involve creating a `ModelManager` class to handle the reusable `Encoder` and `Decoder` instances, ensuring maximum performance. The client's `_load_service_data` method will be updated to use this manager to decode service data directly into the `ServiceData` struct, and the rest of the client will be updated to use these typed objects, eliminating risky dictionary lookups.
