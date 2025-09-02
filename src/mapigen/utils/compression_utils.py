from __future__ import annotations
import zstandard as zstd

def compress_with_zstd(data: bytes, level: int = 22) -> bytes:
    """Compresses data using zstandard."""
    cctx = zstd.ZstdCompressor(level=level)
    return cctx.compress(data)

def decompress_zstd(compressed: bytes) -> bytes:
    """Decompresses zstandard data."""
    dctx = zstd.ZstdDecompressor()
    return dctx.decompress(compressed)
