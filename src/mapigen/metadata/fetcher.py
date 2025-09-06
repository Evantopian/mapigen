from __future__ import annotations
import logging
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from itertools import islice
from typing import Any, Dict, Iterable, Iterator, List
import os
import re
import json

import msgspec
import niquests
from tqdm import tqdm

from mapigen.utils.compression_utils import compress_with_zstd
from mapigen.utils.path_utils import get_service_data_path, get_data_dir

REGISTRY_DIR = get_data_dir().parent / "registry"
POSTMAN_SOURCES_PATH = REGISTRY_DIR / "postman_sources.yaml"

def _sanitize_api_name(name: str) -> str:
    """Sanitizes a string to be a valid directory and api name."""
    name = name.lower()
    name = re.sub(r'\s+', '-', name)
    name = re.sub(r'[^a-z0-9-]', '', name)
    return name

def _update_postman_sources_yaml(updated_sources: List[Dict[str, Any]]):
    """Updates the postman_sources.yaml file with the latest collection names."""
    try:
        from collections import defaultdict
        grouped_sources = defaultdict(list)
        for source in updated_sources:
            grouped_sources[source['provider']].append(source)

        final_yaml_string = ""
        for provider, sources in grouped_sources.items():
            for source in sources:
                final_yaml_string += f"- provider: {source['provider']}\n"
                final_yaml_string += f"  url: {source['url']}\n"
                if 'apis' in source:
                    final_yaml_string += "  apis:\n"
                    for api in sorted(source['apis']):
                        final_yaml_string += f"  - {api}\n"
            final_yaml_string += "\n"

        # Remove the last newline
        if final_yaml_string:
            final_yaml_string = final_yaml_string[:-1]

        POSTMAN_SOURCES_PATH.write_text(final_yaml_string)
        logging.info(f"Updated {POSTMAN_SOURCES_PATH} with the latest collection details.")
    except Exception as e:
        logging.error(f"Failed to update {POSTMAN_SOURCES_PATH}: {e}")

def _discover_postman_collections(workspaces: List[Dict[str, Any]], session: niquests.Session) -> List[Dict[str, Any]]:
    """Discovers all collections from a list of Postman workspaces."""
    all_collections = []
    updated_yaml_entries = []

    for workspace_info in tqdm(workspaces, desc="Discovering Postman Collections"):
        workspace_id = workspace_info["url"]
        provider = workspace_info["provider"]
        workspace_url = f"https://api.getpostman.com/workspaces/{workspace_id}"
        
        try:
            resp = session.get(workspace_url, timeout=30)
            resp.raise_for_status()
            workspace_data = resp.json()
            collections = workspace_data.get("workspace", {}).get("collections", [])
            
            source_for_yaml = workspace_info.copy()
            if 'source' in source_for_yaml:
                del source_for_yaml['source']
            source_for_yaml["apis"] = [_sanitize_api_name(c.get("name")) for c in collections if c.get("name")]
            updated_yaml_entries.append(source_for_yaml)

            for collection in collections:
                if collection.get("name") and collection.get("uid"):
                    all_collections.append({
                        "provider": provider,
                        "api": _sanitize_api_name(collection.get("name")),
                        "uid": collection.get("uid"),
                        "source": "postman"
                    })
        except Exception as e:
            logging.error(f"Failed to fetch workspace {workspace_id}: {e}")
            # Create a copy to avoid modifying the original
            entry = workspace_info.copy()
            if 'source' in entry:
                del entry['source']
            updated_yaml_entries.append(entry) # Keep old entry on failure

    _update_postman_sources_yaml(updated_yaml_entries)
    return all_collections

def _fetch_single_postman_collection(collection_info: Dict[str, Any], session: niquests.Session, args: Any) -> Dict[str, Any]:
    """Fetches and transforms a single Postman collection."""
    provider = collection_info["provider"]
    api_name = collection_info["api"]
    collection_uid = collection_info["uid"]
    
    service_data_dir = get_service_data_path(provider, api_name, "postman")
    spec_path_zst = service_data_dir / f"{api_name}.openapi.json.zst"

    if not args.force_reprocess and (service_data_dir / "metadata.yml").exists() and spec_path_zst.exists():
        return {"status": "skipped", "provider": provider, "api": api_name, "source": "postman"}

    transform_url = f"https://api.getpostman.com/collections/{collection_uid}/transformations?format=json"
    t_start = time.perf_counter()

    try:
        spec_resp = session.get(transform_url, timeout=60)
        spec_resp.raise_for_status()
        raw_response_data = spec_resp.json()
        content_str = raw_response_data.get("output")
        if not content_str:
            return {"status": "failure", "provider": provider, "api": api_name, "source": "postman", "reason": "'output' key not found in response"}
        
        content = json.dumps(json.loads(content_str), indent=2).encode('utf-8')
        download_duration = time.perf_counter() - t_start

        service_data_dir.mkdir(parents=True, exist_ok=True)
        spec_path_zst.write_bytes(compress_with_zstd(content))

        if args.no_compress_original:
            (service_data_dir / f"{api_name}.openapi.json").write_bytes(content)

        return {"status": "success", "provider": provider, "api": api_name, "source": "postman", "download_duration": download_duration, "url": transform_url}
    except Exception as e:
        logging.error(f"Failed to download collection {api_name} ({collection_uid}): {e}")
        return {"status": "failure", "provider": provider, "api": api_name, "source": "postman", "reason": str(e)}

def fetch_postman_specs(sources: List[Dict[str, Any]], args: Any) -> List[Dict[str, Any]]:
    """Orchestrates the discovery and fetching of Postman collections."""
    api_key = os.getenv("POSTMAN_API_KEY")
    if not api_key:
        logging.warning("POSTMAN_API_KEY not set. Skipping Postman sources.")
        return []

    headers = {"X-API-Key": api_key}
    all_results: List[Dict[str, Any]] = []

    with niquests.Session() as session:
        session.headers.update(headers)
        collections_to_fetch = _discover_postman_collections(sources, session)
        
        with ThreadPoolExecutor(max_workers=args.download_workers) as executor:
            futures = {executor.submit(_fetch_single_postman_collection, c, session, args): c["api"] for c in collections_to_fetch}
            for future in as_completed(futures):
                all_results.append(future.result())

    return all_results

def fetch_single_spec(provider: str, api: str, source: str, url: str, session: niquests.Session, args: Any) -> Dict[str, Any]:
    """Fetches, normalizes, and compresses a single OpenAPI spec from a URL."""
    service_data_dir = get_service_data_path(provider, api, source)
    spec_path_zst = service_data_dir / f"{api}.openapi.json.zst"

    if not args.force_reprocess and (service_data_dir / "metadata.yml").exists() and spec_path_zst.exists():
        return {"status": "skipped", "provider": provider, "api": api}

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

        service_data_dir.mkdir(parents=True, exist_ok=True)
        spec_path_zst.write_bytes(compress_with_zstd(content))

        if args.no_compress_original:
            (service_data_dir / f"{api}.openapi.json").write_bytes(content)

        return {"status": "success", "provider": provider, "api": api, "source": source, "download_duration": download_duration, "url": url}
    except Exception as e:
        logging.error(f"Failed to download {api} from {source}: {e}")
        return {"status": "failure", "provider": provider, "api": api, "source": source, "reason": str(e)}

def batcher(iterable: Iterable, batch_size: int) -> Iterator[List[Any]]:
    """Yields successive n-sized chunks from an iterable."""
    iterator = iter(iterable)
    while chunk := list(islice(iterator, batch_size)):
        yield chunk

def fetch_specs_concurrently(sources: List[Dict[str, Any]], batch_size: int, args: Any) -> List[Dict[str, Any]]:
    """Fetches and compresses multiple specs concurrently in batches, saving them to disk."""
    if not sources:
        return []
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
