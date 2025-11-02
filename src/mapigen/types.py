from __future__ import annotations
from pathlib import Path
from typing import Literal, TypeAlias, TypeVar
import msgspec

PathLike: TypeAlias = str | Path
LogLevel: TypeAlias = Literal["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG", "TRACE"]
CompressionStrategy: TypeAlias = Literal["zstd", "gzip", "none"]
BundleFormat: TypeAlias = Literal["tar.zst", "tar.gz", "directory"]

class defaults(msgspec.Struct, frozen=True):
    REGISTRY_PATH: str = "/etc/mapigen/registry"
    EXPORT_DIR: str = "/var/lib/mapispec"
    TEMP_DIR: str = "/var/tmp/mapigen"
    COMPRESSION: int = 7
    WORKERS: int = 8
    LOG_LEVEL: str = "INFO"
    BUNDLE_SUFFIX: str = ".bundle.tar.zst"
    METADATA_FILE: str = "metadata.json"



K = TypeVar("K")
V = TypeVar("V")
T = TypeVar("T")
R = TypeVar("R")