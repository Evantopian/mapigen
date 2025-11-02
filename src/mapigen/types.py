from __future__ import annotations
from pathlib import Path
from typing import Literal, TypeAlias, Callable, Any, Final
import msgspec


PathLike: TypeAlias = str | Path
LogLevel: TypeAlias = Literal["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG", "TRACE"]
CompressionStrategy: TypeAlias = Literal["zstd", "none"]


POSTMAN_BASE_URL: Final[str] = "https://api.getpostman.com"

BundleFormat: TypeAlias = Literal["tar.zst"]
ParseableFileType: TypeAlias = Literal["yaml", "json", "msgspec"] 
SupportedFileType: TypeAlias = Literal["yaml", "json", "zst", "msgspec", "unknown"]

InputFileType: TypeAlias = Literal["yaml", "json"]
OutputFileType: TypeAlias = Literal["msgspec", "zst"]

DECODER_MAP: Final[dict[ParseableFileType, Callable[[bytes], Any]]] = {
    "yaml": msgspec.yaml.decode,
    "json": msgspec.json.decode,
    "msgspec": msgspec.msgpack.decode,
}

FILE_TYPE_MAP: Final[dict[str, SupportedFileType]] = {
    ".yaml": "yaml",
    ".yml": "yaml",
    ".json": "json",
    ".zst": "zst",
    ".msgspec": "msgspec",
}

class defaults(msgspec.Struct, frozen=True):
    REGISTRY_PATH: str = "/etc/mapigen/registry"
    EXPORT_DIR: str = "/var/lib/mapispec"
    TEMP_DIR: str = "/var/tmp/mapigen"
    COMPRESSION: int = 7
    WORKERS: int = 8
    LOG_LEVEL: str = "INFO"
    BUNDLE_SUFFIX: str = ".bundle.tar.zst"
    METADATA_FILE: str = "metadata.json"
