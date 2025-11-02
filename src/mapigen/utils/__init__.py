from __future__ import annotations
from .compression import decompress_zstd, compress_zstd
from .file import detect_file_type, read_file_auto

__all__ = [
    "decompress_zstd", "compress_zstd",
    "detect_file_type", "read_file_auto"
]