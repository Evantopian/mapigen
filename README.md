<div align="center">
<picture>
  <source media="(prefers-color-scheme: light)" srcset="./docs/banner.svg">
  <img alt="mapigen-logo" src="./docs/banner.svg" width="100%" height="100%">
</picture>

![Build Status](https://img.shields.io/badge/Build-TBD-lightgrey?style=flat)
![PyPI Version](https://img.shields.io/badge/PyPI-not--released-lightgrey?style=flat)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue?style=flat)](./LICENSE)
[![API Ref-mapigen](https://img.shields.io/badge/API%20Reference-mapigen-blue?style=flat)](./docs/API_REFERENCE.md)
</div>

> Notes: Working on auto-updates, adding support for templated URLs for dynamic endpoint configuration.

`mapigen` is a Python framework that transforms OpenAPI specifications into lightweight, normalized metadata, enabling efficient and dynamic API access.

## Overview

`mapigen` acts as a universal API client generator. It processes any OpenAPI specification, creating a highly optimized and compressed metadata file. The `Mapi` client then uses this metadata to provide a dynamic, ready-to-use Python interface for any API, complete with authentication and validation.

This approach is ideal for workflow orchestrators, node executors, and LLM tool integrations where performance and adaptability are critical.

## Installation

To get started, install `mapigen` from PyPI:

```bash
pip install mapigen
```

## Quickstart

`mapigen` comes with a set of pre-processed APIs, so you can use it right out of the box.

```python
from mapigen import Mapi

# Initialize the client
mapi = Mapi()

# 1. Discover available services
print(f"Available services: {mapi.discovery.list_services()}")
# Expected output: ['github', 'discord', 'pokeapi', 'stripe']

# 2. Call an API using the dynamic proxy
try:
    response = mapi.pokeapi.api_v2_pokemon_retrieve(id='pikachu')
    if response.get('data'):
        print(f"Successfully fetched data for {response['data'].get('name')}")
except Exception as e:
    print(f"An error occurred: {e}")
```

## Usage Patterns

`mapigen` is designed for both synchronous and asynchronous applications and provides detailed metadata with every call.

### The `Mapi` Client and Caching

When you initialize the `Mapi` client, it sets up an efficient in-memory caching system. The first time you access a service (e.g., `mapi.github`), its processed metadata is loaded from disk and cached. All subsequent operations for that service during the client's lifetime will use the cached data, making them extremely fast.

### Return Value: Data and Metadata

Every call to `execute` or `aexecute` returns a dictionary containing two keys:
-   `data`: The JSON response from the API, or `None` on error.
-   `metadata`: A `ResponseMetadata` object containing useful information about the call, such as `duration_ms`, `http_status`, and `error_type`.

### Synchronous Usage

#### 1. Proxy-Based Calls (Recommended)

This is the most intuitive and IDE-friendly method. It's great for interactive use and when you know the service and operation names beforehand.

```python
# Retrieve a specific pokemon
response = mapi.pokeapi.api_v2_pokemon_retrieve(id='ditto')

# The response is a dictionary containing data and metadata
ditto_data = response['data']
call_metadata = response['metadata']

print(f"Fetched data for: {ditto_data['name']}")
print(f"Call took {call_metadata.duration_ms}ms with status: {call_metadata.status}")
```

#### 2. Direct `execute()` Calls
---
The `execute()` method is perfect for dynamic scenarios where the service and operation names are determined at runtime, such as from a UI form or a variable.

```python
# These values could come from a web form or variables
service_name = "pokeapi"
operation_id = "api_v2_pokemon_retrieve"
params = {"id": "snorlax"}

# Execute the call dynamically
response = mapi.execute(service_name, operation_id, **params)
if response['data']:
    print(f"Successfully fetched {response['data']['name']}")
```

### Asynchronous Usage

For high-performance applications, `mapigen` provides asynchronous methods powered by `niquests`. All `execute` methods have an `aexecute` counterpart.

```python
# You must run this within an async function
async def fetch_all_pokemon():
    # 1. Async Proxy-Based Calls
    # Use the .aexecute() method and await the result
    response = await mapi.pokeapi.api_v2_pokemon_retrieve.aexecute(id='bulbasaur')
    if response['data']:
        print(f"Async fetch successful for: {response['data']['name']}")

    # 2. Async Direct `aexecute()` Calls
    response = await mapi.aexecute("pokeapi", "api_v2_pokemon_retrieve", id='charmander')
    if response['data']:
        print(f"Async fetch successful for: {response['data']['name']}")
```

## Adding New APIs (scoped to development, non published; working on dynamic updates)

While `mapigen` comes with bundled API data, you can easily add your own.

1.  **Add your source:** Add the URL of your OpenAPI specification to `src/mapigen/registry/custom_sources.json`.
    ```json
    {
        "my_api": "https://api.example.com/openapi.json" // or yaml
    }
    ```
2.  **Run the population tool:** From the cloned repository, run the `populate_data` script. This fetches, processes, and compresses the spec into the required format.
    ```bash
    # Ensure you have cloned the repo and installed dependencies with poetry
    poetry run python -m mapigen.tools.populate_data
    ```
Your new API will now be available through the `Mapi` client.

## Future Work

I am continuously improving `mapigen`. Here are some features on the roadmap:
-   **Dynamic Updates:** Distrubuted updates for ensuring all my API registries are updated daily, ideally 2-3+ checks a day.
-   **CLI:** A command-line interface for easier configuration and data management.
-   **Simplified Custom Population:** A more streamlined workflow for adding and updating custom API specifications without needing to run scripts from the source.
-   **Local Web Server:** A local UI for faster configuration and testing.

## Contributing
I've considered utilizing [Postman](https://www.postman.com/) as another registry method—even as the first priority. However, it seems that Postman does not offer API endpoints to retrieve data publicly. Continuously web scraping Postman to track metrics such as popularity, relevancy, and view counts is unsustainable and time-consuming, especially when updates occur. No webhooks appear to exist for this purpose. I've also attempted forking, which allows me to fetch the workspaces and collections, but it removes the ability to update autonomously. If anyone comes across a solution for this, I would love to know.
 
1.  **Linting**:
    ```bash
    make lint
    ```
2.  **Testing**:
    ```bash
    make test
    ```

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](./LICENSE) file for details.