# src/mapigen/metadata/utils.py
import json
import yaml
from pathlib import Path
from typing import Any, Dict

def load_spec(path: Path) -> Dict[str, Any]:
    """
    Load an OpenAPI spec from either JSON or YAML.
    """
    text = path.read_text(encoding="utf-8")
    
    # Try JSON first
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    
    # Fallback to YAML
    try:
        return yaml.safe_load(text)
    except yaml.YAMLError as e:
        raise ValueError(f"File {path} is not valid JSON or YAML: {e}")
