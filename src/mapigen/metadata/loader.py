import json
from pathlib import Path
from typing import Dict, Any
import lz4.frame


def compress_metadata(json_path: Path) -> Path:
    """
    Read JSON file, compress it into LZ4 frame, and write to disk.
    """
    raw_bytes: bytes = json_path.read_bytes()

    compressed: bytes = lz4.frame.compress(raw_bytes)

    out_path = json_path.with_suffix(json_path.suffix + ".lz4")
    out_path.write_bytes(compressed)
    return out_path


def load_metadata(lz4_path: Path) -> Dict[str, Any]:
    compressed: bytes = lz4_path.read_bytes()
    decompressed: bytes = lz4.frame.decompress(compressed)
    text: str = decompressed.decode("utf-8")
    return json.loads(text)