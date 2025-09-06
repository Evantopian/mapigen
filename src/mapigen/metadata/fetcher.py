from __future__ import annotations
import logging
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from itertools import islice
from typing import Any, Dict, Iterable, Iterator, List

import msgspec
import niquests
from tqdm import tqdm

from mapigen.utils.compression_utils import compress_with_zstd
from mapigen.utils.path_utils import get_service_data_path

def fetch_single_spec(
    provider: str, api: str, source: str, url: str, session: niquests.Session, args: Any
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
            return {"status": "failure", "provider": provider, "api": api, "source": source, "reason": "No content"}

        if url.endswith((".yaml", ".yml")):
            data = msgspec.yaml.decode(content)
            content = msgspec.json.encode(data)

        service_data_dir = get_service_data_path(provider, api, source)
        service_data_dir.mkdir(parents=True, exist_ok=True)

        # Always save the compressed version for the pipeline to use
        compressed_content = compress_with_zstd(content)
        spec_path_zst = service_data_dir / f"{api}.openapi.json.zst"
        spec_path_zst.write_bytes(compressed_content)

        # If the flag is set, also save the original for debugging
        if args.no_compress_original:
            spec_path_json = service_data_dir / f"{api}.openapi.json"
            spec_path_json.write_bytes(content)

        return {"status": "success", "provider": provider, "api": api, "source": source, "download_duration": download_duration}

    except Exception as e:
        logging.error(f"Failed to download {api} from {source}: {e}")
        return {"status": "failure", "provider": provider, "api": api, "source": source, "reason": str(e)}

def batcher(iterable: Iterable, batch_size: int) -> Iterator[List[Any]]:
    """Yields successive n-sized chunks from an iterable."""
    iterator = iter(iterable)
    while chunk := list(islice(iterator, batch_size)):
        yield chunk

def fetch_specs_concurrently(
    sources: List[Dict[str, Any]], batch_size: int, args: Any
) -> List[Dict[str, Any]]:
    """
    Fetches and compresses multiple specs concurrently in batches, saving them to disk.
    Returns a list of result dictionaries.
    """
    logging.info(f"Downloading {len(sources)} specs in batches of {batch_size}...")
    all_results: List[Dict[str, Any]] = []

    for batch in tqdm(list(batcher(sources, batch_size)), desc="Downloading Batches"):
        with niquests.Session() as session:
            with ThreadPoolExecutor(max_workers=args.download_workers) as executor:
                futures = {
                    executor.submit(fetch_single_spec, entry['provider'], entry['api'], entry['source'], entry['url'], session, args): entry['api']
                    for entry in batch
                }
                for future in as_completed(futures):
                    result = future.result()
                    all_results.append(result)
    return all_results