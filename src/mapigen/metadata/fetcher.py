import requests
from pathlib import Path
import logging

def fetch_spec(service: str, url: str, out_dir: Path) -> Path:
    """
    Fetch an OpenAPI spec for a given service and save it locally,
    preserving the original file extension. Skips download if file exists.
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    
    file_ext = ".json"
    if url.lower().endswith(".yml"):
        file_ext = ".yml"
    elif url.lower().endswith(".yaml"):
        file_ext = ".yaml"

    path = out_dir / f"{service}.openapi{file_ext}"

    if path.exists():
        logging.info(f"Using cached raw spec file: {path}")
        return path

    logging.info(f"Downloading raw spec from {url}...")
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()
    path.write_text(resp.text, encoding="utf-8")
    return path
