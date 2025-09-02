# Mapigen API Reference

## 1. Introduction

This document provides a detailed technical reference for the `mapigen` Python library. It is intended for developers who are using the library and need to understand its classes, methods, and data structures in detail.

For a general overview, installation instructions, and quickstart examples, please see the [README.md](../README.md).

## 2. The `Mapi` Client

The `mapigen.Mapi` class is the primary entry point for all interactions with the library.

### 2.1. Initialization

You initialize the client by creating an instance of the `Mapi` class.

```python
from mapigen import Mapi

mapi = Mapi(
    auth=None, 
    default_timeout=30.0, 
    log_level="INFO", 
    validate_on_execute=True
)
```

**Constructor: `Mapi(auth, default_timeout, log_level, validate_on_execute, **transport_kwargs)`**

-   **`auth`** (`Optional[AuthBase]`): An authentication object from the `niquests` library or a compatible class. See the [Authentication](#2.4-authentication) section for more details. Defaults to `None`.
-   **`default_timeout`** (`float`): The default timeout in seconds for all HTTP requests. Defaults to `30.0`.
-   **`log_level`** (`str`): The logging level for the client (e.g., `"INFO"`, `"DEBUG"`). Defaults to `"INFO"`.
-   **`validate_on_execute`** (`bool`): If `True`, the client will validate parameters against the API schema before making a request, raising a `MapiError` on failure. Defaults to `True`.
-   **`**transport_kwargs`**: Additional keyword arguments to pass to the underlying `niquests` HTTP transport, such as `verify=False` to disable SSL verification.

### 2.2. Executing Operations

#### Proxy-Based Calls (Sync & Async)

This is the recommended, IDE-friendly method for calling API operations.

-   **Synchronous:**
    ```python
    # Returns a dict: {"data": ..., "metadata": ...}
    response = mapi.pokeapi.api_v2_pokemon_retrieve(id='ditto')
    ```
-   **Asynchronous:** Asynchronous operations are powered by `niquests`.
    ```python
    # This must be run inside an async function
    async def fetch_pokemon():
        response = await mapi.pokeapi.api_v2_pokemon_retrieve.aexecute(id='ditto')
        return response
    ```

#### Direct `execute()` and `aexecute()`

These methods are ideal for dynamic scenarios where the service and operation names are not known until runtime.

-   **`execute(service: str, operation: str, **kwargs: Any) -> Dict`**
    -   Executes a synchronous API call.
    -   **Returns:** A dictionary containing `data` and `metadata` keys.

-   **`aexecute(service: str, operation: str, **kwargs: Any) -> Coroutine[Any, Any, Dict]`**
    -   Asynchronously executes an API call using `niquests`.
    -   **Returns:** A coroutine that resolves to a dictionary containing `data` and `metadata` keys.

**Example:**
```python
# Sync
response = mapi.execute('pokeapi', 'api_v2_pokemon_retrieve', id='pikachu')

# Async
async def fetch_pikachu_async():
    async_response = await mapi.aexecute('pokeapi', 'api_v2_pokemon_retrieve', id='pikachu')
    return async_response
```

### 2.3. Service Discovery

The `mapi.discovery` property provides access to a `DiscoveryClient` instance for exploring available services and operations.

-   **`list_services() -> List[str]`**: Returns a list of all available service names.
-   **`service_exists(service: str) -> bool`**: Checks if a service is available.
-   **`get_service_info(service: str) -> ServiceInfo`**: Returns a `ServiceInfo` data object for a service.
-   **`list_operations(service: str) -> List[str]`**: Returns a list of all operation IDs for a given service.
-   **`get_operation(service: str, operation: str) -> Operation`**: Returns a detailed `Operation` data object.

**Example:**
```python
if mapi.discovery.service_exists('github'):
    info = mapi.discovery.get_service_info('github')
    print(f"GitHub has {info.operation_count} operations.")

    operations = mapi.discovery.list_operations('github')
    print(f"First 5 operations: {operations[:5]}")
```

### 2.4. Authentication

Authentication is handled by injecting a `niquests.auth.AuthBase` compatible object into the `Mapi` client's constructor via the `auth` parameter.

This dependency injection approach allows you to use any authentication mechanism that conforms to the `niquests` authentication interface.

**Example with a standard `niquests` authenticator:**
```python
from niquests.auth import HTTPBasicAuth
from mapigen import Mapi

# Use a standard auth object from the underlying http library
basic_auth = HTTPBasicAuth('user', 'pass')

mapi = Mapi(auth=basic_auth)
```

For convenience, `mapigen` also provides helper classes under the `mapigen.Auth` namespace that create common authentication objects for you. In the future, these helpers may be moved to a separate `mapitools` package.

-   **`Auth.ApiKey(key: str, name: str, placement: str)`**: For API key authentication.
    -   `placement` can be `'header'` or `'query'`.
-   **`Auth.BearerAuth(token: str)`**: For Bearer token authentication.

**Example with `mapigen.Auth` convenience helpers:**
```python
from mapigen import Mapi, Auth

# For an API that uses a Bearer token
github_auth = Auth.BearerAuth(token="YOUR_GITHUB_TOKEN")
github_mapi = Mapi(auth=github_auth)
```

### 2.5. Error Handling

All exceptions raised by the `mapigen` library are subclasses of `MapiError`. This allows for targeted error handling.

-   **`mapigen.MapiError`**: The base exception class.
    -   `service` (`str`): The service that was called.
    -   `operation` (`str`): The operation that was called.
    -   `error_type` (`str`): The category of error (e.g., `"validation"`, `"network_error"`, `"sdk"`).

**Example:**
```python
from mapigen import Mapi, MapiError

mapi = Mapi()

try:
    # This will fail validation because 'id' is missing
    mapi.pokeapi.api_v2_pokemon_retrieve()
except MapiError as e:
    print(f"Caught a MapiError!")
    print(f"  Service: {e.service}")
    print(f"  Operation: {e.operation}")
    print(f"  Error Type: {e.error_type}")
    print(f"  Message: {e}")
```

## 3. Core Data Models

These are the primary data structures returned by the client's methods.

-   **`ResponseMetadata`**: Returned in the `metadata` key of every `execute` call.
    -   `service` (`str`): The name of the service.
    -   `operation` (`str`): The name of the operation.
    -   `duration_ms` (`int`): The duration of the API call in milliseconds.
    -   `status` (`str`): `"success"` or `"error"`.
    -   `http_status` (`Optional[int]`): The HTTP status code of the response.
    -   `error_type` (`Optional[str]`): The category of error if one occurred.

-   **`ServiceInfo`**: Returned by `discovery.get_service_info()`.
    -   `operation_count` (`int`): Total number of operations.
    -   `popularity_rank` (`int`): The service's rank.
    -   `auth_types` (`List[str]`): A list of supported authentication types.
    -   `primary_auth` (`str`): The main authentication type.

-   **`Operation`**: Returned by `discovery.get_operation()`.
    -   `service` (`str`): The service name.
    -   `path` (`str`): The URL path for the operation.
    -   `method` (`str`): The HTTP method (e.g., `"GET"`, `"POST"`).
    -   `parameters` (`List[ParameterUnion]`): A list of parameters for the operation.

## 4. Complexity and Runtime

This section provides an overview of the computational complexity and runtime characteristics of key operations in the `mapigen` library. This information is useful for understanding the performance implications of using the library in different scenarios.

The complexities are expressed in Big O notation, where:
-   `N`: Represents the size of the input data (e.g., an API specification file).
-   `S`: Represents the number of services.
-   `P`: Represents the number of parameters in an operation.
-   `R`: Represents the size of the request/response payload.
-   `M`: Represents the size of the metadata for a service.
-   `K`: Represents the number of pinned keys in the cache.

#### Client Operations (`mapigen.client`)

| Method/Operation | Time Complexity | Space Complexity | Runtime Specs | Notes |
| :--- | :--- | :--- | :--- | :--- |
| `Mapi.__init__` | `O(S)` | `O(S)` | - | Initialization involves loading the service registry. |
| `Mapi.__getattribute__` | `O(1)` | `O(1)` | - | Accessing a service proxy is a constant time operation. |
| `Mapi._load_service_data` | `O(N)` | `O(N)` | File I/O, Decompression | Loading a service definition from disk is linear to its size. |
| `Mapi.execute` / `aexecute` | `O(P + R)` | `O(P + R)` | Network | Dominated by parameter preparation and network latency. |

#### Discovery Operations (`mapigen.discovery`)

| Method/Operation | Time Complexity | Space Complexity | Runtime Specs | Notes |
| :--- | :--- | :--- | :--- | :--- |
| `list_services` | `O(1)` (cached) | `O(1)` | File I/O (first call) | The service registry is cached after the first read. |
| `get_service_info` | `O(1)` (cached) | `O(1)` | File I/O (first call) | The service registry is cached after the first read. |
| `list_operations` | `O(N)` | `O(N)` | File I/O, Decompression | Requires loading the service data from disk. |
| `get_operation` | `O(N)` | `O(N)` | File I/O, Decompression | Requires loading the service data from disk. |

#### Caching (`mapigen.cache`)

| Method/Operation | Time Complexity | Space Complexity | Runtime Specs | Notes |
| :--- | :--- | :--- | :--- | :--- |
| `PinnedLRUCache.get` | `O(1)` (amortized) | `O(M+K)` | Threading | Cache hits are constant time. Misses trigger a disk load. |

## 5. Appendix: Internal Architecture

This section provides a high-level overview of the internal components of `mapigen`.

-   **`metadata`**: This package is the core of the data processing pipeline. It contains modules for:
    -   `fetcher`: Downloads OpenAPI specifications from remote URLs.
    -   `converter`: Normalizes and validates raw specs.
    -   `extractor`: Reduces the spec into the lightweight `utilize.json` format, fingerprinting and componentizing reusable parameters.

-   **`cache`**: Manages the storage and retrieval of processed service data.
    -   `storage.py`: Handles loading service data from disk (either compressed or uncompressed) and implements the `PinnedLRUCache` for efficient in-memory caching.
    -   `ranking.py`: Manages the popularity ranking of services, which determines whether they are compressed.

-   **`tools`**: A collection of developer-facing scripts for managing the data pipeline.
    -   `populate_data.py`: The main script that orchestrates the entire fetch -> process -> store workflow.
    -   `validate_data.py` & `deep_validate.py`: Scripts for ensuring the integrity and correctness of the processed data.

-   **`proxy`**: Contains the `ServiceProxy` and `OperationProxy` classes that enable the dynamic `mapi.service.operation()` syntax.

-   **`http`**: A simple transport layer built on `niquests` that handles making synchronous and asynchronous HTTP requests.