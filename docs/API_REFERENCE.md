# API Reference

This document provides a detailed reference for the `mapigen` client API.

## `Mapi` Client

The `Mapi` class is the main entry point for interacting with the SDK.

### Initialization

```python
from mapigen import Mapi

client = Mapi(
    auth=("user", "pass"),
    default_timeout=60.0
)
```

### Service Access

Services are no longer accessed as direct attributes. Use the `s()` method with the full service key to get a service proxy object.

**New Usage Pattern:**

```python
# Get a proxy for a specific service version
stripe_proxy = client.s("stripe:payments:github")

# Execute an operation
response = stripe_proxy.get_charges()

print(response)
```

### Direct Execution

The `execute()` and `aexecute()` methods still exist, but they now require the full service key as the first argument.

```python
# Execute an operation directly
response = client.execute(
    service_key="stripe:payments:github",
    operation="get_charges",
    limit=10
)
```

## Discovery Client

The `DiscoveryClient` provides methods for exploring the available APIs and services.

```python
from mapigen.discovery import DiscoveryClient

discovery = DiscoveryClient()
```

### `list_apis()`

Returns a list of unique API names available in the registry.

```python
>>> discovery.list_apis()
['calendar', 'drive', 'payments', 'pokeapi', ...]
```

### `list_sources_for_api(api_name: str)`

Returns a list of available sources (e.g., `github`, `postman` workspace name) for a given API.

```python
>>> discovery.list_sources_for_api("drive")
['github', 'google_apis']
```

### `get_service_details(service_key: str)`

Returns the detailed metadata for a specific service key.

```python
>>> discovery.get_service_details("google:drive:github")
{
  "resolvable": True,
  "tested": False,
  "lastUpdated": "2025-09-05T12:00:00Z"
}
```
