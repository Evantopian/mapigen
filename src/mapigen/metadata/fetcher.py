from __future__ import annotations
import logging
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from itertools import islice
from pathlib import Path
from typing import Any, Dict, Iterable, Iterator, List

import msgspec
import niquests
from tqdm import tqdm

from mapigen.utils.compression_utils import compress_with_zstd

# Define paths relative to this file's location
SRC_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = SRC_DIR / "data"

def fetch_single_spec(
    service_name: str, url: str, session: niquests.Session, args: Any
) -> Dict[str, Any]:
    """Fetches, normalizes, and compresses a single OpenAPI spec, returning metrics."""
    headers = {"User-Agent": "mapigen-builder/1.0"}
    t_start = time.perf_counter()
    try:
        resp = session.get(url, timeout=30, headers=headers)
        resp.raise_for_status()
        content = resp.content
        download_duration = time.perf_counter() - t_start

        if not content:
            return {"status": "failure", "service_name": service_name, "reason": "No content"}

        if url.endswith((".yaml", ".yml")):
            data = msgspec.yaml.decode(content)
            content = msgspec.json.encode(data)

        service_data_dir = DATA_DIR / service_name
        service_data_dir.mkdir(parents=True, exist_ok=True)

        if args.no_compress_original:
            spec_path = service_data_dir / f"{service_name}.openapi.json"
            spec_path.write_bytes(content)
        else:
            compressed_content = compress_with_zstd(content)
            spec_path = service_data_dir / f"{service_name}.openapi.json.zst"
            spec_path.write_bytes(compressed_content)

        return {"status": "success", "service_name": service_name, "download_duration": download_duration}

    except Exception as e:
        logging.error(f"Failed to download {service_name}: {e}")
        return {"status": "failure", "service_name": service_name, "reason": str(e)}

def batcher(iterable: Iterable, batch_size: int) -> Iterator[List[Any]]:
    """Yields successive n-sized chunks from an iterable."""
    iterator = iter(iterable)
    while chunk := list(islice(iterator, batch_size)):
        yield chunk

def fetch_specs_concurrently(
    sources: Dict[str, str], batch_size: int, args: Any
) -> List[Dict[str, Any]]:
    """
    Fetches and compresses multiple specs concurrently in batches, saving them to disk.
    Returns a list of result dictionaries.
    """
    logging.info(f"Downloading {len(sources)} specs in batches of {batch_size}...")
    source_items = list(sources.items())
    all_results: List[Dict[str, Any]] = []

    for batch in tqdm(list(batcher(source_items, batch_size)), desc="Downloading Batches"):
        with niquests.Session() as session:
            with ThreadPoolExecutor(max_workers=args.download_workers) as executor:
                futures = {
                    executor.submit(fetch_single_spec, name, url, session, args): name
                    for name, url in batch
                }
                for future in as_completed(futures):
                    result = future.result()
                    all_results.append(result)
    return all_results
