<div align="center">
<picture>
  <source media="(prefers-color-scheme: light)" srcset="./docs/banner.svg">
  <img alt="mapigen-logo" src="./docs/banner.svg" width="100%" height="100%">
</picture>

![Build Status](https://img.shields.io/badge/Build-TBD-lightgrey?style=flat)
![PyPI Version](https://img.shields.io/badge/PyPI-not--released-lightgrey?style=flat)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue?style=flat)](./LICENSE)
[![Docs](https://img.shields.io/badge/docs-mapigen-blue?style=flat)](https://github.com/SpoungeAI/mapigen/wiki)

</div>

> Notes: Currently working on dynamic updates for registry, higher accuracy validation, and more tooling. Future considerations include a CLI and local web server for faster configuration.


`mapigen` is a Python SDK/framework designed for workflow orchestrators, node executors, and LLM tool integrations that transforms OpenAPI specifications into lightweight, normalized metadata for efficient, "secure" API access. Its preprocessing pipeline fetches, validates, and normalizes specifications, fingerprints reusable components using hashes, and compresses the resulting data, for example: `GitHub spec: 11.1 MB  →  0.3 MB  (97.2% reduction)`. 

The `Mapi` client runs directly on the compressed metadata, decompressing large files at runtime using LZ4 (avg <0.06 ms). A ranking system allows skipping decompression for container adapters that do not require it. `Mapi` supports synchronous and asynchronous operations, enabling event-driven workflows such as webhooks, message queues, and background tasks. 
 
### Key functionality includes:
- **OpenAPI Specification Fetching**: Downloads OpenAPI specs from specified URLs (registry).
- **Specification Normalization and Validation**: Ensures specs conform to OpenAPI standards and prepares them for processing.
- **Metadata Extraction and Compression**: Reduces OpenAPI specs into a lightweight structure, identifying and referencing reusable components, and optionally compressing the output.
- **Dynamic API Client**: Provides a Python client (`Mapi`) that dynamically exposes services and their operations based on the processed metadata.
- **Authentication Handling**: Supports various authentication methods and allows for manual overrides.
- **Data Validation**: Tools for validating the integrity and consistency of the processed metadata.

## Installation

### Dependencies

`mapigen` relies on the following core dependencies:
- `niquests`: Asynchronous HTTP client.
- `pydantic`: Data validation and settings management.
- `jsonschema`: JSON Schema validation.
- `lz4`: For data compression.
- `openapi-spec-validator`: OpenAPI specification validation.
- `openapi-schema-validator`: OpenAPI schema validation.
- `structlog`: Structured logging.
- `orjson`: Fast JSON serialization.

Development dependencies include `pytest`, `pytest-cov`, `pytest-asyncio`, `python-dotenv`, and `pyyaml`.

### Supported Python Versions

`mapigen` officially supports Python 3.10 and above.

### Environment Setup

It is recommended to use `poetry` for dependency management.

### Installation Instructions

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/meoya/mapigen.git
    cd mapigen
    ```
2.  **Install dependencies using Poetry:**
    ```bash
    poetry install
    ```
3.  **Activate the Poetry shell (optional, but recommended):**
    ```bash
    poetry shell
    ```

## Core Concepts & Architecture

`mapigen` is structured around a pipeline that transforms raw OpenAPI specifications into an optimized, client-consumable format.

### The Data Pipeline

The SDK does not fetch API specifications in real-time. Instead, it relies on a pre-built cache of processed OpenAPI specifications. This ensures that all discovery and validation operations are extremely fast (typically <1ms).

The data pipeline works as follows:

1.  **Source**: An OpenAPI specification URL is added to the registry (`src/mapigen/registry/`).
2.  **Population**: The `tools/populate_data.py` script fetches the spec, extracts only the essential information (operations, parameters, etc.), and saves it as a lightweight `utilize.json` file in the data cache (`src/mapigen/data/{service}/`).
3.  **Ranking & Compression**: Based on a service's popularity rank (`registry/popularity.json`), the `utilize.json` file is either stored uncompressed (for top-tier, fast-access APIs) or compressed with LZ4 (for standard-tier APIs).
4.  **Client Usage**: The `Mapi` client reads from this pre-processed cache at runtime.

### Dynamic Client Interface

The SDK provides a dynamic, attribute-based proxy interface that allows you to explore and execute API operations fluently. Instead of a traditional method call like `client.execute('pokeapi', 'api_v2_pokemon_retrieve', ...)` you can use a more intuitive, IDE-friendly syntax:

```python
# The dynamic proxy syntax
client.pokeapi.api_v2_pokemon_retrieve(id='ditto')
```
This is the recommended way to interact with the client.

### Module Organization

-   **Raw OpenAPI Specification**: The initial input, typically a JSON or YAML file, defining an API.
-   **`fetcher`**: Downloads raw OpenAPI specs from remote URLs.
-   **`converter`**: Normalizes and validates the fetched OpenAPI specs, ensuring they are well-formed.
-   **`extractor`**: The core transformation engine. It processes the normalized OpenAPI spec to:
    -   Identify and fingerprint reusable parameters.
    -   Create a lightweight `utilize.json` structure containing only essential operation details and references to reusable components. This significantly reduces the size and complexity compared to the original OpenAPI spec.
-   **`cache`**: Manages the storage and retrieval of processed service data (`utilize.json` and `metadata.yml`), including optional LZ4 compression for `utilize.json`.
-   **`client` (`Mapi`)**: The primary interface for interacting with processed APIs. It dynamically exposes services and their operations based on the `utilize.json` metadata.
    -   **`ServiceProxy`**: Enables dynamic access to services (e.g., `mapi.github`).
    -   **`DiscoveryClient`**: Lists available services based on the processed metadata.
-   **`tools`**: A collection of utility scripts for managing the data population pipeline:
    -   `populate_data.py`: Orchestrates the entire process of fetching, normalizing, extracting, and saving service metadata.
    -   `validate_data.py`: Performs basic integrity checks on the processed data.
    -   `deep_validate.py`: Conducts a thorough validation, comparing extracted components against original raw spec parameters to ensure consistency.
-   **`registry`**: Stores configuration files like `custom_sources.json`, `github_sources.json`, `popularity.json`, and `overrides.json`, which define the services to be processed and their authentication configurations.
-   **`schemas`**: Defines the JSON Schema for the `utilize.json` format, ensuring data consistency.

The overall flow involves `populate_data.py` using `fetcher`, `converter`, and `extractor` to generate `utilize.json` and `metadata.yml` files for each service. The `Mapi` client then loads and interprets these files to provide a dynamic API interface.

## Usage Examples

### Populating Service Data

To fetch, process, and store API metadata:

```bash
poetry run python -m mapigen.tools.populate_data
```

Options for `populate_data`:
- `--keep-raw-specs`: Retain original downloaded OpenAPI spec files.
- `--no-compress`: Do not compress the final `utilize.json` file.
- `--rank <int>`: Set the popularity rank threshold for compression (services with rank >= threshold are compressed).
- `--cache`: Skip processing services if metadata already exists.

Example with options:
```bash
poetry run python -m mapigen.tools.populate_data --cache --no-compress
```

### Using the `Mapi` Client

Initialize the `Mapi` client and interact with services:

```python
from mapigen import Mapi
from mapigen.auth.providers import BearerTokenProvider, BasicAuthProvider, ApiKeyProvider

# Initialize Mapi client
# Optional: base_url for overriding service base URLs, auth_provider for global authentication
mapi = Mapi()

# 1. Service Discovery
print("--- Service Discovery ---")
all_services = mapi.discovery.list_services()
print(f"Available services: {all_services}")

if mapi.discovery.service_exists('github'):
    print("
GitHub service found!")
    info = mapi.discovery.get_service_info('github')
    print(f"GitHub operations count: {info.get('operation_count')}")
    auth_types = mapi.discovery.get_auth_types('github')
    primary_auth = mapi.discovery.get_primary_auth('github')
    print(f"Supported auth types: {auth_types}")
    print(f"Primary auth type: {primary_auth}")

# 2. Executing Operations
print("
--- Executing Operations ---")
try:
    # Dynamic proxy syntax (recommended)
    response = mapi.pokeapi.api_v2_pokemon_retrieve(id='pikachu')
    if response:
        print(f"Successfully fetched data for {response['data'].get('name')}")

    # Direct execute method (for dynamic service/operation names)
    service_name = "pokeapi"
    operation_id = "api_v2_pokemon_retrieve"
    params = {"id": "snorlax"}
    response = mapi.execute(service_name, operation_id, **params)
    if response:
        print(f"Successfully fetched data for {response['data'].get('name')}")

except Exception as e:
    print(f"An error occurred during operation execution: {e}")

# 3. Parameter Validation
print("
--- Parameter Validation ---")
# This will fail validation (missing required 'id')
print("Attempting invalid call (missing 'id'):")
invalid_response = mapi.pokeapi.api_v2_pokemon_retrieve()
if invalid_response and invalid_response['data'] is None:
    print("Validation failed as expected.")

# This will fail validation ('foo' is not a valid parameter)
print("Attempting invalid call (unexpected parameter 'foo'):")
invalid_response = mapi.pokeapi.api_v2_pokemon_retrieve(id='ditto', foo='bar')
if invalid_response and invalid_response['data'] is None:
    print("Validation failed as expected.")

# 4. Authentication
print("
--- Authentication ---")
# Using Auth Provider at client instantiation (recommended)
# from mapigen import Mapi
# from mapigen.auth.providers import BearerTokenProvider
# auth_provider = BearerTokenProvider(token="YOUR_GITHUB_TOKEN")
# github_mapi = Mapi(auth_provider=auth_provider)
# user_info = github_mapi.github.users_get_authenticated() # Example operation

# Using with_auth() for a single call
# from mapigen import Mapi
# from mapigen.auth.providers import BasicAuthProvider
# client_no_auth = Mapi()
# stripe_auth = BasicAuthProvider(username="YOUR_STRIPE_SECRET_KEY")
# charges = client_no_auth.with_auth(stripe_auth).charges.list(limit=5) # Example operation
```

### Validating Processed Data

To validate the integrity and consistency of the generated data:

```bash
poetry run python -m mapigen.tools.validate_data
poetry run python -m mapigen.tools.deep_validate
```

## API Reference

### `mapigen.Mapi` Class

The main client for interacting with processed APIs.

**Constructor:**
`Mapi(base_url: Optional[str] = None, auth_provider: Optional[AuthBase] = None, default_timeout: float = 30.0, log_level: str = "INFO", **transport_kwargs: Any)`

-   `base_url` (Optional[str]): Overrides the base URL for all service requests.
-   `auth_provider` (Optional[AuthBase]): A `niquests.auth.AuthBase` instance (or compatible) for global authentication. Use classes from `mapigen.auth.providers`.
-   `default_timeout` (float): Default request timeout in seconds.
-   `log_level` (str): Logging level (e.g., "INFO", "DEBUG").
-   `**transport_kwargs` (Any): Additional keyword arguments passed to the underlying `HttpTransport`.

**Properties:**
-   `auth`: Access to `AuthHelpers` for generating authentication objects.
-   `discovery`: Access to `DiscoveryClient` methods for service and operation discovery.

**Methods:**
-   `execute(service: str, operation: str, **kwargs: Any) -> Dict[str, Union[Dict[str, Any], ResponseMetadata, None]]`
    -   Executes a synchronous API operation.
    -   `service` (str): The name of the service (e.g., "github", "stripe").
    -   `operation` (str): The `operationId` of the API endpoint.
    -   `**kwargs` (Any): Parameters required by the operation, passed as keyword arguments.
    -   **Returns**: A dictionary containing:
        -   `data` (Dict[str, Any] | None): The JSON response from the API, or `None` on error.
        -   `metadata` (ResponseMetadata): Metadata about the request, including duration, status, and error details.
-   `aexecute(service: str, operation: str, **kwargs: Any) -> Dict[str, Union[Dict[str, Any], ResponseMetadata, None]]`
    -   Asynchronously executes an API operation. Signature and return value are identical to `execute`.
-   `with_auth(auth_provider: AuthBase) -> Mapi`:
    -   Returns a *new* `Mapi` instance with the specified `auth_provider`, leaving the original client unchanged. Useful for per-request authentication.

**Exceptions:**
-   `MapiError`: Base exception for `mapigen` client errors.
-   `ServiceNotFoundError`: Raised when a requested service is not found.
-   `OperationNotFoundError`: Raised when a requested operation is not found within a service.
-   `ValidationError`: Raised when input parameters fail schema validation.
-   `RequestError`: Raised for issues during HTTP request preparation or execution.

### `mapigen.AuthHelpers` Class (`mapigen.Auth`)

Provides utility methods for generating authentication objects.

**Methods:**
-   `github_token(token: str) -> AuthBase`: Returns a `niquests` Auth object for GitHub token authentication.
-   *(Other authentication methods would be documented here as they are added)*

### `mapigen.auth.providers` Module

Provides concrete `AuthBase` implementations for common authentication schemes.

-   `BearerTokenProvider(token: str)`: For APIs using Bearer Token authentication.
-   `BasicAuthProvider(username: str, password: str = "")`: For APIs using HTTP Basic Auth.
-   `ApiKeyProvider(key: str, key_name: str, placement: str = 'header')`: Generic API key provider (`placement` can be `'header'` or `'query'`).

### `mapigen.discovery.DiscoveryClient` Class (accessed via `Mapi.discovery`)

Provides methods for discovering available services and their metadata.

-   `list_services() -> List[str]`: Lists all available service names.
-   `service_exists(service: str) -> bool`: Checks if a specific service exists.
-   `get_service_info(service: str) -> Optional[Dict[str, Any]]`: Retrieves metadata for a service (e.g., `operation_count`, `auth_types`).
-   `get_auth_types(service: str) -> List[str]`: Returns a list of supported authentication types for a service.
-   `get_primary_auth(service: str) -> str`: Returns the primary authentication type for a service.

### `mapigen.discovery.operations` Module

Functions for querying processed service operations.

-   `list_operations(service: str) -> List[str]`: Lists all operation IDs for a given service.
-   `operation_exists(service: str, operation: str) -> bool`: Checks if an operation exists for a service.
-   `get_operation(service: str, operation: str) -> Optional[Dict[str, Any]]`: Retrieves full details for a specific operation.

### `mapigen.metadata.converter` Module

-   `normalize_spec(path: Path) -> Mapping[str, Any]`: Loads an OpenAPI spec from a path, validates it, and returns a normalized representation.

### `mapigen.metadata.extractor` Module

-   `extract_operations_and_components(service: str, spec: dict[str, Any]) -> dict[str, Any]`: Reduces an OpenAPI spec into a lightweight structure, identifying reusable components via fingerprinting.
-   `save_metadata(service: str, data: dict[str, Any], out_dir: Path) -> Path`: Saves extracted metadata to a `utilize.json` file.

### `mapigen.metadata.fetcher` Module

-   `fetch_spec(service: str, url: str, out_dir: Path) -> Path`: Fetches an OpenAPI spec from a URL and saves it locally, with caching.

## Configuration & Extension Points

### Service Sources

`mapigen` discovers services from JSON files located in `src/mapigen/registry/`:
-   `custom_sources.json`: For user-defined or custom API sources.
-   `github_sources.json`: For API sources discovered from GitHub.

These files should contain a JSON object where keys are service names (e.g., "github", "stripe") and values are the URLs to their OpenAPI specifications.

Example `custom_sources.json`:
```json
{
    "my_api": "https://api.example.com/openapi.json",
    "another_api": "https://another.example.com/swagger.yaml"
}
```

### Authentication Overrides

The `src/mapigen/registry/overrides.json` file allows for manual overrides of authentication information for services. This is particularly useful when an OpenAPI spec does not fully declare its authentication methods.

Example `overrides.json`:
```json
{
    "my_api": {
        "auth": {
            "auth_types": ["BearerToken"],
            "primary_auth": "BearerToken"
        }
    }
}
```

### Popularity Ranking

The `src/mapigen/registry/popularity.json` file assigns a popularity rank to each service. This rank determines whether the service's `utilize.json` data is compressed (for space efficiency) or left uncompressed (for faster loading). Lower numbers indicate higher popularity.

### Environment Variables

Currently, no specific environment variables are directly consumed by `mapigen` for configuration. Logging level can be controlled via the `Mapi` constructor.

### Hooks/Plugin Mechanisms

`mapigen` does not currently offer explicit plugin or hook mechanisms. Extension is primarily achieved by modifying the source code or by adding new service sources and authentication overrides.

## Testing & Development

### How to Run Tests

`mapigen` uses `pytest` for its test suite.

1.  **Ensure development dependencies are installed:**
    ```bash
    poetry install --with dev
    ```
2.  **Run all tests:**
    ```bash
    poetry run pytest
    ```
3.  **Run specific tests:**
    ```bash
    poetry run pytest tests/unit/test_discovery.py
    ```
    Or using the Makefile:
    ```bash
    make test t=tests/unit/test_discovery.py
    ```
4.  **Generate a test coverage report:**
    ```bash
    poetry run pytest --cov=src/mapigen --cov-report=term-missing
    ```

### Testing Methodology

The test suite is divided into:
-   **Unit Tests (`tests/unit/`)**: Focus on individual components and functions in isolation.
-   **Integration Tests (`tests/integration/`)**: Verify the interaction between multiple components and the end-to-end flow, often involving mock external services or pre-processed data.

### Guidelines for Contributing or Extending the Library

1.  **Adhere to existing code style**: Use `ruff` for linting.
    ```bash
    poetry run ruff check .
    ```
    Or using the Makefile:
    ```bash
    make lint
    ```
2.  **Write tests**: Ensure new features or bug fixes are covered by appropriate unit and/or integration tests.
3.  **Update documentation**: If new features or significant changes are introduced, update the relevant sections of this `README.md`.
4.  **Run validation tools**: Before submitting changes, ensure all data validation tools pass.
    ```bash
    poetry run python -m mapigen.tools.validate_data
    poetry run python -m mapigen.tools.deep_validate
    ```

## Performance & Best Practices

### Runtime Considerations

`mapigen` is designed for high performance, with its core SDK overhead being negligible (typically <1-2ms for request preparation and response parsing). The primary runtime considerations are:

-   **Data Population**: The `populate_data` script can be time-consuming, especially for a large number of services or large OpenAPI specs, due to network requests, parsing, and processing. This is an I/O bound operation.
-   **Client Initialization**: `Mapi` client initialization involves loading service metadata from disk. While cached, the initial load can have a minor overhead, as it involves I/O operations.
-   **Request Execution**: API calls through the `Mapi` client are predominantly I/O bound, subject to external network latency and the processing time of the target API servers. Observed latencies of 200-350ms for external services are normal and expected, not indicative of `mapigen`'s performance.

### Efficiency Tips

`mapigen` is built with efficiency in mind:

-   **Caching**: Utilize the `--cache` option with `populate_data` to skip re-processing unchanged services.
-   **Compression**: Enable compression for `utilize.json` files (default behavior for services with sufficient popularity rank) to reduce disk space and potentially speed up loading.
-   **In-Memory Caching (`@lru_cache`)**: The `Mapi` client and discovery modules extensively use `lru_cache` for service data loading and registry lookups. This ensures that data is loaded from disk only once per service during runtime, leading to amortized O(1) performance for subsequent accesses.
-   **Optimized Libraries**: Leverages fast libraries like `niquests` for HTTP communication and `orjson` for JSON parsing.
-   **Asynchronous Operations**: Use `mapi.aexecute` for non-blocking API calls in asynchronous applications to improve concurrency.

### Recommended Usage Patterns

-   **Pre-process Data**: Run `populate_data` as a build step or a scheduled job to ensure that the `utilize.json` files are up-to-date before application deployment.
-   **Centralized Configuration**: Manage service sources and authentication overrides in the `src/mapigen/registry/` directory.
-   **Error Handling**: Implement robust error handling around `Mapi` client calls, catching specific `MapiError` subclasses for granular control.

## References

-   **OpenAPI Specification**: [https://swagger.io/specification/](https://swagger.io/specification/)
-   **Poetry**: Python packaging and dependency management: [https://python-poetry.org/](https://python-poetry.org/)
-   **niquests**: HTTP client library: [https://niquests.readthedocs.io/](https://niquests.readthedocs.io/)
-   **Pydantic**: Data validation: [https://pydantic.dev/](https://pydantic.dev/)
-   **JSON Schema**: [https://json-schema.org/](https://json-schema.org/)
-   **structlog**: Structured logging: [https://www.structlog.org/](https://www.structlog.org/)
-   **ruff**: Python linter: [https://docs.astral.sh/ruff/](https://docs.astral.sh/ruff/)
-   **pytest**: Testing framework: [https://docs.pytest.org/](https://docs.pytest.org/)