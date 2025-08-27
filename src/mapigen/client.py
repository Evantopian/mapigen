from pathlib import Path
import logging
from functools import lru_cache

from .tools.utils import load_metadata

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ServiceMetadata:
    """Loads and holds the metadata for a single service."""
    def __init__(self, service_name: str):
        self.service_name = service_name
        self._data = self._load_data()
        self.operations = self._data.get("operations", {})
        self.components = self._data.get("components", {})

    @lru_cache(maxsize=None)
    def _load_data(self) -> dict:
        """Loads the metadata from the compressed file."""
        data_dir = Path(__file__).parent / "data"
        service_path = data_dir / self.service_name / f"{self.service_name}.utilize.json.lz4"
        if not service_path.exists():
            raise AttributeError(f"Service '{self.service_name}' not found. Please ensure data is populated.")
        return load_metadata(service_path)

    def get_operation(self, operation_id: str) -> dict:
        """Gets the details for a single operation."""
        return self.operations.get(operation_id)

    def resolve_parameter(self, param: dict) -> dict:
        """Resolves a parameter, following a $ref if necessary."""
        if "$ref" in param:
            ref_path = param["$ref"]
            component_name = ref_path.split("/")[-1]
            return self.components.get("parameters", {}).get(component_name, {})
        return param

class CallableOperation:
    """Represents a single, callable API operation."""
    def __init__(self, metadata: ServiceMetadata, operation_id: str):
        self.metadata = metadata
        self.operation_id = operation_id
        self.op_details = self.metadata.get_operation(operation_id)
        if not self.op_details:
            raise AttributeError(f"Operation '{self.operation_id}' not found in service '{self.metadata.service_name}'.")

    def __call__(self, **kwargs):
        """Executes the API call."""
        logging.info(f"--- Calling {self.metadata.service_name}.{self.operation_id} ---")
        
        path_params = {}
        query_params = {}
        body_params = {}

        # Resolve and sort parameters based on user input
        for param_ref in self.op_details.get("parameters", []):
            param_details = self.metadata.resolve_parameter(param_ref)
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
        
        # Construct the URL
        path_template = self.op_details.get("path", "")
        final_path = path_template.format(**path_params)

        # For now, just print the details of the would-be request
        print(f"Method: {self.op_details.get('method')}")
        print(f"URL Path: {final_path}")
        if query_params:
            print(f"Query Params: {query_params}")
        if body_params:
            print(f"Body Params: {body_params}")
        print("-----------------------------------------------------")

class ServiceProxy:
    """A proxy object that provides access to a service's operations."""
    def __init__(self, service_name: str):
        self.service_name = service_name
        self.metadata = ServiceMetadata(service_name)

    def __getattr__(self, name: str) -> CallableOperation:
        # Replace dashes with underscores for Python-friendly names
        operation_id = name.replace("_", "-")
        return CallableOperation(self.metadata, operation_id)

class MapigenClient:
    """A dynamic API client generated from metadata."""
    @lru_cache(maxsize=32)
    def __getattr__(self, name: str) -> ServiceProxy:
        return ServiceProxy(name)
