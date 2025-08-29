from __future__ import annotations
import gc
import psutil

def get_memory_usage() -> float:
    """Returns the current memory usage of the process in MB."""
    process = psutil.Process()
    return process.memory_info().rss / (1024 * 1024)

def trigger_gc_if_needed(threshold_mb: float):
    """Triggers garbage collection if memory usage exceeds a threshold."""
    if get_memory_usage() > threshold_mb:
        gc.collect()

def estimate_decompressed_size(compressed: bytes) -> int:
    """Estimates the decompressed size of a zstd frame."""
    # This is a placeholder. A more accurate estimation would require
    # reading the zstd frame header, which is more complex.
    # A common heuristic is to assume a compression ratio.
    # For now, we return 0 as this is not yet implemented.
    return 0
