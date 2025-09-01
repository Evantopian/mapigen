from __future__ import annotations
import time
from functools import wraps
from typing import Any, Callable
from pathlib import Path


def timing_decorator(func: Callable[..., Any]) -> Callable[..., Any]:
    """A decorator to time the execution of a function."""

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed_time = (end_time - start_time) * 1000  # to milliseconds
        print(f"\n--- Timing: {func.__name__} took {elapsed_time:.2f}ms ---")
        return result

    return wrapper

def create_unsupported_file(tmp_path: Path, extension: str) -> Path:
    """Creates a temporary file with an unsupported extension."""
    unsupported_file = tmp_path / f"test.{extension}"
    unsupported_file.write_text("test content")
    return unsupported_file

def create_mock_spec_with_broken_ref() -> dict[str, Any]:
    """Creates a mock spec with a broken $ref."""
    return {"components": {"parameters": {"param1": {"name": "param1"}}}}
