import requests
from pathlib import Path

def fetch_spec(service: str, url: str, out_dir: Path) -> Path:
    """
    Fetch an OpenAPI spec for a given service and save it locally.
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"{service}.openapi.json"
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()
    path.write_text(resp.text, encoding="utf-8")
    return path
