from pathlib import Path
from typing import Any, Mapping, cast
from openapi_spec_validator import validate_spec
from mapigen.metadata import load_spec

def normalize_spec(path: Path) -> Mapping[str, Any]:
    spec: dict[str, Any] = load_spec(path)
    validate_spec(cast(Mapping[Any, Any], spec))
    return spec
