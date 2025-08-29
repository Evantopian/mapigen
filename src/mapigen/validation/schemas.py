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
    
    spec = importlib.util.spec_from_loader(f"{service_name}_schemas", loader=None)
    if spec is None:
        raise ImportError(f"Could not create spec from loader for service: {service_name}")
    module = importlib.util.module_from_spec(spec)
    exec(decompressed, module.__dict__)
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
