from __future__ import annotations
import zstandard as zstd

def compress_zstd(data: bytes, level: int = 7) -> bytes:
    """Compress raw bytes using Zstandard."""
    compressor = zstd.ZstdCompressor(level=level)
    return compressor.compress(data)

def decompress_zstd(data: bytes) -> bytes:
    """Decompress Zstandard-compressed bytes."""
    decompressor = zstd.ZstdDecompressor()
    return decompressor.decompress(data)
