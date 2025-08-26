import requests
from pathlib import Path

def fetch_spec(service: str, url: str, out_dir: Path) -> Path:
    """
    Fetch an OpenAPI spec for a given service and save it locally,
    preserving the original file extension.
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    
    # Determine the file extension from the URL
    file_ext = ".json" # Default to .json
    if url.lower().endswith(".yml"):
        file_ext = ".yml"
    elif url.lower().endswith(".yaml"):
        file_ext = ".yaml"

    path = out_dir / f"{service}.openapi{file_ext}"
    
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()
    path.write_text(resp.text, encoding="utf-8")
    return path
