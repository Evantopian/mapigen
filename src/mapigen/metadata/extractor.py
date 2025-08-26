import json
from pathlib import Path

def extract_operations(service: str, spec: dict) -> dict:
    """
    Reduce OpenAPI spec into lightweight operation metadata.
    """
    operations = {}
    for path, methods in spec.get("paths", {}).items():
        for method, details in methods.items():
            op_id = details.get("operationId") or f"{service}_{method}_{path}"
            params = details.get("parameters", [])
            required = [p["name"] for p in params if p.get("required")]
            optional = [p["name"] for p in params if not p.get("required")]
            operations[op_id] = {
                "service": service,
                "path": path,
                "method": method.upper(),
                "parameters": {
                    "required": required,
                    "optional": optional
                }
            }
    return operations

def save_metadata(service: str, operations: dict, out_dir: Path) -> Path:
    """
    Save extracted metadata into a utilize.json file.
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"{service}.utilize.json"
    path.write_text(json.dumps(operations, indent=2))
    return path
