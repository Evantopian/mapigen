"""Parameter validation using JSON Schema."""
from __future__ import annotations
from typing import Any
import importlib.util
import zstandard as zstd
from pathlib import Path

import msgspec

from ..client.exceptions import MapiError

def _import_schema_module(service_name: str):
    """Dynamically imports the _schemas.py.zst module for a service."""
    data_dir = Path(__file__).resolve().parent.parent / "data"
    compressed_path = data_dir / service_name / f"{service_name}_schemas.py.zst"
    
    if not compressed_path.exists():
        # Fallback to uncompressed for debugging
        uncompressed_path = data_dir / service_name / f"{service_name}_schemas.py"
        if not uncompressed_path.exists():
            raise ImportError(f"Schema file not found for service: {service_name}")
        
        spec = importlib.util.spec_from_file_location(f"{service_name}_schemas", uncompressed_path)
        if spec is None:
            raise ImportError(f"Could not create spec from file: {uncompressed_path}")
        module = importlib.util.module_from_spec(spec)
        if spec.loader is None:
            raise ImportError(f"Spec loader is None for file: {uncompressed_path}")
        spec.loader.exec_module(module)
        return module

    dctx = zstd.ZstdDecompressor()
    decompressed = dctx.decompress(compressed_path.read_bytes())
    schema_code = decompressed.decode('utf-8')
    
    # Debug: Print the schema content to see what's wrong
    print("=== DEBUG: Schema content ===")
    print(schema_code)
    print("=== END DEBUG ===")
    
    spec = importlib.util.spec_from_loader(f"{service_name}_schemas", loader=None)
    if spec is None:
        raise ImportError(f"Could not create spec from loader for service: {service_name}")
    module = importlib.util.module_from_spec(spec)

    try:
        # Create a clean execution environment with all necessary imports
        from typing import Optional, List, Dict, Union, Any
        
        module_globals = {
            '__name__': f"{service_name}_schemas",
            '__file__': str(compressed_path),
            '__builtins__': __builtins__,
            'msgspec': msgspec,
            'Any': Any,
            'Optional': Optional,
            'List': List,
            'Dict': Dict,
            'Union': Union,
        }
        
        # Execute the schema code with proper globals
        exec(schema_code, module_globals, module.__dict__)
                
    except Exception as e:
        print(f"Error executing schema code: {e}")
        print(f"Schema code (first 500 chars):\n{schema_code[:500]}...")
        raise
        
    return module


def build_and_validate_parameters(
    service_name: str,
    operation_id: str,
    parameters: dict[str, Any],
) -> None:
    """
    Validates parameters using a dynamically loaded msgspec.Struct.
    """
    try:
        schema_module = _import_schema_module(service_name)
        struct_name = f"{operation_id.replace('/', '_').replace('-', '_')}_params"
        struct_class = getattr(schema_module, struct_name)
        
        # msgspec validates during decoding
        msgspec.json.decode(msgspec.json.encode(parameters), type=struct_class)

    except (ImportError, AttributeError) as e:
        raise MapiError(f"Schema validation setup failed for {service_name}.{operation_id}: {e}", service=service_name, operation=operation_id, error_type="sdk", original_exception=e) from e
    except msgspec.ValidationError as e:
        raise MapiError(f"Parameter validation failed: {e}", service=service_name, operation=operation_id, error_type="validation", original_exception=e) from e