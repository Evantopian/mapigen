from __future__ import annotations
import logging
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from itertools import islice
from typing import Any, Dict, Iterable, Iterator, List

from tqdm import tqdm

from mapigen.metadata.converter import normalize_spec
from mapigen.metadata.extractor import extract_operations_and_components, save_metadata
from mapigen.tools.utils import extract_auth_info
from mapigen.utils.memory_manager import trigger_gc_if_needed
from mapigen.utils.path_utils import get_service_data_path

# Define paths relative to this module
FORMAT_VERSION = 3

def batcher(iterable: Iterable, batch_size: int) -> Iterator[list]:
    """Yields successive n-sized chunks from an iterable."""
    iterator = iter(iterable)
    while chunk := list(islice(iterator, batch_size)):
        yield chunk

def process_single_service(service_info: dict[str, Any]) -> dict[str, Any]:
    """Worker function to process a single service, returning metrics."""
    provider = service_info["provider"]
    api = service_info["api"]
    source = service_info["source"]
    url = service_info["url"]

    metrics: Dict[str, Any] = {"provider": provider, "api": api, "source": source, "url": url}
    try:
        service_data_dir = get_service_data_path(provider, api, source)
        t_parse_start = time.perf_counter()
        compressed_spec_path = service_data_dir / f"{api}.openapi.json.zst"
        compressed_content = compressed_spec_path.read_bytes()
        raw_spec = dict(normalize_spec(compressed_content=compressed_content))
        metrics["parse_duration"] = time.perf_counter() - t_parse_start

        t_extract_start = time.perf_counter()
        processed_data = extract_operations_and_components(api, raw_spec)
        metrics["extract_duration"] = time.perf_counter() - t_extract_start

        processed_data["servers"] = raw_spec.get("servers", [])
        processed_data["format_version"] = FORMAT_VERSION
        processed_data["service_name"] = api
        
        utilize_path = save_metadata(api, processed_data, service_data_dir)

        metrics.update({
            "status": "success",
            "auth_info": extract_auth_info(raw_spec),
            "processed_op_count": len(processed_data["operations"]),
            "reusable_param_count": len(processed_data.get("components", {}).get("parameters", {})),
            "utilize_path": utilize_path
            })
        return metrics
    except Exception as e:
        logging.error(f"Failed to process service {api} from {source}: {e}")
        metrics["status"] = "failure"
        return metrics

def create_balanced_batches(service_info: List[Dict[str, Any]], num_batches: int) -> List[List[Dict[str, Any]]]:
    """Creates balanced batches based on file size using a greedy algorithm."""
    service_info = [s for s in service_info if s.get("size", 0) > 0]
    if not service_info:
        return []

    # For small numbers of items, don't bother with complex batching.
    if len(service_info) < num_batches * 2:
        logging.info("Number of items is small, creating a single batch.")
        return [service_info]

    service_info.sort(key=lambda x: x["size"], reverse=True)

    num_batches = min(num_batches, len(service_info))
    if num_batches == 0:
        return []
        
    batches: List[List[Dict[str, Any]]] = [[] for _ in range(num_batches)]
    batch_sizes = [0] * num_batches

    for service in service_info:
        min_index = batch_sizes.index(min(batch_sizes))
        batches[min_index].append(service)
        batch_sizes[min_index] += service["size"]

    return [batch for batch in batches if batch]

def run_processing_pipeline(services_to_process: List[Dict[str, Any]], args: Any) -> List[Dict[str, Any]]:
    """Runs the parallel processing pipeline and returns the results."""
    if args.batch_size:
        processing_batches = list(batcher(services_to_process, args.batch_size))
    else:
        logging.info("Creating balanced batches based on file size...")
        processing_batches = create_balanced_batches(services_to_process, args.process_workers)

    if not services_to_process:
        return []

    logging.info(f"Processing {len(services_to_process)} services in {len(processing_batches)} batches...")
    processing_results: List[Dict[str, Any]] = []
    for batch in tqdm(processing_batches, desc="Processing Batches"):
        with ProcessPoolExecutor(max_workers=args.process_workers) as executor:
            futures = {executor.submit(process_single_service, service): service["api"] for service in batch}
            for future in as_completed(futures):
                result = future.result()
                processing_results.append(result)
                trigger_gc_if_needed(args.memory_threshold)
    return processing_results