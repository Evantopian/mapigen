import yaml
from dataclasses import fields
from typing import Any, Union

from mapigen.client.config import ResponseMetadata

def format_type(type_hint: Any) -> str:
    """Formats a type hint into a readable string."""
    if hasattr(type_hint, '__origin__') and type_hint.__origin__ is Union:
        # Handle Optional[T] which is Union[T, None]
        args = getattr(type_hint, '__args__', ())
        if len(args) == 2 and args[1] is type(None):
            return f"Optional[{format_type(args[0])}]"
    if hasattr(type_hint, '__name__'):
        return type_hint.__name__
    return str(type_hint).replace('typing.', '')

def main():
    """Prints the standard response format of the Mapigen SDK."""
    
    print("#-- Mapigen SDK Standard Response Format --#\n")

    metadata_fields = {f.name: format_type(f.type) for f in fields(ResponseMetadata)}

    response_structure = {
        "data": "# The JSON payload from the API service (or null on error).",
        "metadata": metadata_fields
    }

    # Use yaml for a clean, readable output
    print(yaml.dump(response_structure, sort_keys=False, indent=2, default_flow_style=False))

if __name__ == "__main__":
    main()
