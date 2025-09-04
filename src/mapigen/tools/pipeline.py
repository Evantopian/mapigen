from __future__ import annotations
import logging
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path
from typing import Any, Dict, List

from tqdm import tqdm

from mapigen.metadata.converter import normalize_spec
from mapigen.metadata.extractor import extract_operations_and_components, save_metadata
from mapigen.tools.utils import extract_auth_info, count_openapi_operations
from mapigen.utils.memory_manager import trigger_gc_if_needed

# Define paths relative to this module
SRC_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = SRC_DIR / "data"
FORMAT_VERSION = 3

def process_spec_file(spec_path: Path) -> dict[str, Any]:
    """Worker function to process a single OpenAPI spec file, returning metrics."""
    try:
        # Derive names from path
        api_name = spec_path.parent.name
        source_name = spec_path.parent.parent.name
        provider_name = spec_path.parent.parent.parent.name
        service_key = f"{provider_name}:{api_name}:{source_name}"
        
        metrics: Dict[str, Any] = {"service_key": service_key, "status": "failure"}

        t_parse_start = time.perf_counter()
        compressed_content = spec_path.read_bytes()
        raw_spec = dict(normalize_spec(compressed_content=compressed_content))
        metrics["parse_duration"] = time.perf_counter() - t_parse_start

        t_extract_start = time.perf_counter()
        processed_data = extract_operations_and_components(service_key, raw_spec)
        metrics["extract_duration"] = time.perf_counter() - t_extract_start

        processed_data["servers"] = raw_spec.get("servers", [])
        processed_data["format_version"] = FORMAT_VERSION
        processed_data["service_name"] = api_name # Keep original api name for metadata
        
        # Save the processed utilize.json file in the same directory as the spec
        utilize_path = save_metadata(api_name, processed_data, spec_path.parent)

        reusable_param_count = processed_data.get("reusable_param_count", 0)
        original_op_count = count_openapi_operations(raw_spec)
        processed_op_count = len(processed_data.get("operations", {}))
        coverage = f"{processed_op_count}/{original_op_count}" if original_op_count > 0 else "0/0"

        metrics.update({
            "status": "success",
            "auth_info": extract_auth_info(raw_spec),
            "processed_op_count": processed_op_count,
            "reusable_param_count": reusable_param_count,
            "coverage": coverage,
            "utilize_path": utilize_path,
            "provider": provider_name,
            "api": api_name,
            "source": source_name,
        })
        return metrics
    except Exception as e:
        logging.error(f"Failed to process spec {spec_path}: {e}")
        # Return a failure metric with the key if possible
        service_key_failure = f"{spec_path.parent.parent.parent.name}:{spec_path.parent.name}:{spec_path.parent.parent.name}"
        return {"service_key": service_key_failure, "status": "failure"}

def create_balanced_batches(specs_to_process: List[Path], num_batches: int) -> List[List[Path]]:
    """Creates balanced batches based on file size using a greedy algorithm."""
    if not specs_to_process:
        return []

    # Create a list of tuples (path, size)
    spec_info = [(p, p.stat().st_size) for p in specs_to_process if p.exists()]
    spec_info.sort(key=lambda x: x[1], reverse=True)

    num_batches = min(num_batches, len(spec_info))
    if num_batches == 0:
        return []
        
    batches: List[List[Path]] = [[] for _ in range(num_batches)]
    batch_sizes = [0] * num_batches

    for path, size in spec_info:
        min_index = batch_sizes.index(min(batch_sizes))
        batches[min_index].append(path)
        batch_sizes[min_index] += size

    return [batch for batch in batches if batch]

def run_processing_pipeline(specs_to_process: List[Path], args: Any) -> List[Dict[str, Any]]:
    """Runs the parallel processing pipeline for all found spec files."""
    if not specs_to_process:
        logging.info("No specs found to process.")
        return []

    logging.info("Creating balanced batches based on file size...")
    processing_batches = create_balanced_batches(specs_to_process, args.process_workers)

    logging.info(f"Processing {len(specs_to_process)} specs in {len(processing_batches)} batches...")
    processing_results: List[Dict[str, Any]] = []
    for batch in tqdm(processing_batches, desc="Processing Batches"):
        with ProcessPoolExecutor(max_workers=args.process_workers) as executor:
            futures = {executor.submit(process_spec_file, spec_path): spec_path for spec_path in batch}
            for future in as_completed(futures):
                result = future.result()
                processing_results.append(result)
                trigger_gc_if_needed(args.memory_threshold)
    return processing_results
