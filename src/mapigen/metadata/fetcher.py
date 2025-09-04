from __future__ import annotations
import logging
import time
import os
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
    provider: str, api: str, source: str, url: str, session: niquests.Session, args: Any
) -> Dict[str, Any]:
    """Fetches, normalizes, and compresses a single OpenAPI spec, returning metrics."""
    headers = {"User-Agent": "mapigen-builder/1.0"}
    t_start = time.perf_counter()
    service_key = f"{provider}:{api}:{source}"
    try:
        resp = session.get(url, timeout=30, headers=headers)
        resp.raise_for_status()
        content = resp.content
        download_duration = time.perf_counter() - t_start

        if not content:
            return {"status": "failure", "service_key": service_key, "reason": "No content"}

        if url.endswith((".yaml", ".yml")):
            data = msgspec.yaml.decode(content)
            content = msgspec.json.encode(data)

        service_data_dir = DATA_DIR / provider / source / api
        service_data_dir.mkdir(parents=True, exist_ok=True)

        spec_path = service_data_dir / f"{api}.openapi.json.zst"
        if args.no_compress_original:
            spec_path = spec_path.with_suffix(".json")
            spec_path.write_bytes(content)
        else:
            compressed_content = compress_with_zstd(content)
            spec_path.write_bytes(compressed_content)

        return {"status": "success", "service_key": service_key, "download_duration": download_duration}

    except Exception as e:
        logging.error(f"Failed to download {service_key}: {e}")
        return {"status": "failure", "service_key": service_key, "reason": str(e)}


def fetch_postman_specs(providers: List[Dict[str, Any]], args: Any) -> List[Dict[str, Any]]:
    """Fetches and transforms collections from Postman workspaces."""
    api_key = os.environ.get("POSTMAN_API_KEY")
    if not api_key:
        logging.warning("POSTMAN_API_KEY environment variable not set. Skipping Postman fetch.")
        return []

    headers = {"X-API-Key": api_key, "User-Agent": "mapigen-builder/1.0"}
    all_results: List[Dict[str, Any]] = []

    with niquests.Session() as session:
        for provider_config in providers:
            provider_name = provider_config["provider"]
            for workspace in tqdm(provider_config.get("workspaces", []), desc=f"Processing {provider_name} workspaces"):
                workspace_name = workspace["name"]
                workspace_id = workspace["id"]
                try:
                    # Get all collections in the workspace
                    ws_url = f"https://api.getpostman.com/workspaces/{workspace_id}"
                    ws_resp = session.get(ws_url, headers=headers, timeout=30)
                    ws_resp.raise_for_status()
                    collections = ws_resp.json().get("workspace", {}).get("collections", [])

                    for collection in tqdm(collections, desc=f"  -> Collections in {workspace_name}", leave=False):
                        collection_id = collection["uid"]
                        collection_name = collection["name"].lower().replace(" ", "_")
                        service_key = f"{provider_name}:{collection_name}:{workspace_name}"
                        t_start = time.perf_counter()

                        # Fetch and transform the collection to OpenAPI
                        transform_url = f"https://api.getpostman.com/collections/{collection_id}/transformations"
                        transform_resp = session.get(transform_url, headers=headers, timeout=60)
                        transform_resp.raise_for_status()
                        spec_content = transform_resp.json().get("output", "").encode('utf-8')
                        download_duration = time.perf_counter() - t_start

                        if not spec_content:
                            all_results.append({"status": "failure", "service_key": service_key, "reason": "Empty transformed spec"})
                            continue

                        # Save the spec
                        service_data_dir = DATA_DIR / provider_name / workspace_name / collection_name
                        service_data_dir.mkdir(parents=True, exist_ok=True)
                        spec_path = service_data_dir / f"{collection_name}.openapi.json.zst"
                        
                        if args.no_compress_original:
                            spec_path = spec_path.with_suffix(".json")
                            spec_path.write_bytes(spec_content)
                        else:
                            compressed_content = compress_with_zstd(spec_content)
                            spec_path.write_bytes(compressed_content)
                        
                        all_results.append({"status": "success", "service_key": service_key, "download_duration": download_duration})

                except Exception as e:
                    logging.error(f"Failed to process Postman workspace {workspace_name}: {e}")
                    all_results.append({"status": "failure", "service_key": f"{provider_name}:<unknown>:{workspace_name}", "reason": str(e)})
    return all_results

def batcher(iterable: Iterable, batch_size: int) -> Iterator[List[Any]]:
    """Yields successive n-sized chunks from an iterable."""
    iterator = iter(iterable)
    while chunk := list(islice(iterator, batch_size)):
        yield chunk

def fetch_specs_concurrently(
    sources: List[Dict[str, Any]], source_type: str, batch_size: int, args: Any
) -> List[Dict[str, Any]]:
    """
    Fetches and compresses multiple URL-based specs concurrently in batches.
    """
    # Create a flat list of all individual specs to download
    all_specs_to_download = []
    for provider_config in sources:
        provider = provider_config["provider"]
        for api_config in provider_config.get("apis", []):
            all_specs_to_download.append({
                "provider": provider,
                "api": api_config["name"],
                "url": api_config["url"],
            })

    if not all_specs_to_download:
        return []

    logging.info(f"Downloading {len(all_specs_to_download)} {source_type} specs in batches of {batch_size}...")
    all_results: List[Dict[str, Any]] = []

    for batch in tqdm(list(batcher(all_specs_to_download, batch_size)), desc=f"Downloading {source_type} Batches"):
        with niquests.Session() as session:
            with ThreadPoolExecutor(max_workers=args.download_workers) as executor:
                futures = {}
                for spec_job in batch:
                    future = executor.submit(
                        fetch_single_spec, 
                        spec_job['provider'], 
                        spec_job['api'], 
                        source_type, 
                        spec_job['url'], 
                        session, 
                        args
                    )
                    futures[future] = f"{spec_job['provider']}:{spec_job['api']}:{source_type}"

                for future in as_completed(futures):
                    result = future.result()
                    all_results.append(result)
    return all_results
