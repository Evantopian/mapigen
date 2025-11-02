from __future__ import annotations
from typing import Any
from pathlib import Path
import msgspec

from mapigen.models import ErrorRecord, ErrorStage
from mapigen.types import SupportedFileType, FILE_TYPE_MAP, DECODER_MAP
 

def detect_file_type(path: Path) -> SupportedFileType:
    ext = path.suffix.lower()
    return FILE_TYPE_MAP.get(ext, "unknown")


def read_file_auto(path: Path) -> dict[str, Any]:
    file_type = detect_file_type(path)

    decoder = DECODER_MAP.get(file_type)
    
    if decoder is None:
        raise ValueError(
            ErrorRecord(
                stage=ErrorStage.LOAD,
                message="Unsupported file type for decoding.",
                detail=f"Detected type '{file_type}' for path '{path}' is not supported. Supported: {list(DECODER_MAP.keys())}",
                file=str(path),
            )
        )

    try:
        with open(path, "rb") as f:
            data = f.read()
    except OSError as e:
        raise ValueError(
            ErrorRecord(
                stage=ErrorStage.LOAD,
                message="Failed to read file.",
                detail=f"An I/O error occurred while reading file '{path}': {e}",
                file=str(path),
            )
        ) from e
    
    try:
        return decoder(data)
    except msgspec.DecodeError as e:
        raise ValueError(
            ErrorRecord(
                stage=ErrorStage.PARSE,
                message=f"Failed to decode {file_type.upper()} file content.",
                detail=f"Decoding error in file '{path}': {e}",
                file=str(path),
            )
        ) from e