from __future__ import annotations
from pathlib import Path
from typing import Optional, Union, Any
import os
import msgspec

from mapigen.types import defaults


class MapigenConfig(msgspec.Struct, frozen=True, kw_only=True):
    """Global configuration for Mapigen build pipeline."""

    registry_path: Path = Path(defaults.REGISTRY_PATH)
    export_dir: Path = Path(defaults.EXPORT_DIR)
    compression_level: int = defaults.COMPRESSION
    workers: int = defaults.WORKERS
    registry_token: Optional[str] = None
    log_level: str = defaults.LOG_LEVEL

    _instance: Optional[MapigenConfig] = None

    @classmethod
    def from_env(cls) -> MapigenConfig:
        """Load configuration from environment variables."""
        instance = cls(
            registry_path=Path(os.getenv("MAPIGEN_REGISTRY_PATH", defaults.REGISTRY_PATH)),
            export_dir=Path(os.getenv("MAPIGEN_EXPORT_DIR", defaults.EXPORT_DIR)),
            compression_level=int(os.getenv("MAPIGEN_COMPRESSION", defaults.COMPRESSION)),
            workers=int(os.getenv("MAPIGEN_WORKERS", defaults.WORKERS)),
            registry_token=os.getenv("MAPIGEN_TOKEN"),
            log_level=os.getenv("MAPIGEN_LOG_LEVEL", defaults.LOG_LEVEL).upper(),
        )
        cls._set_instance(instance)
        return instance

    @classmethod
    def from_file(cls, path: Union[str, Path]) -> MapigenConfig:
        """Load configuration from a JSON file."""
        with open(path, "rb") as f:
            data = msgspec.json.decode(f.read())
        instance = cls.from_dict(data)
        cls._set_instance(instance)
        return instance

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> MapigenConfig:
        """Load configuration from a dictionary with type coercion."""
        return cls(
            registry_path=Path(str(data.get("registry_path", defaults.REGISTRY_PATH))),
            export_dir=Path(str(data.get("export_dir", defaults.EXPORT_DIR))),
            compression_level=int(data.get("compression_level", defaults.COMPRESSION)),
            workers=int(data.get("workers", defaults.WORKERS)),
            registry_token=str(data.get("registry_token"))
            if data.get("registry_token") is not None
            else None,
            log_level=str(data.get("log_level", defaults.LOG_LEVEL)).upper(),
        )

    @classmethod
    def from_params(
        cls,
        *,
        registry_path: Optional[Union[str, Path]] = None,
        export_dir: Optional[Union[str, Path]] = None,
        compression_level: Optional[int] = None,
        workers: Optional[int] = None,
        registry_token: Optional[str] = None,
        log_level: Optional[str] = None,
        cache_instance: bool = True,
    ) -> MapigenConfig:
        """Construct configuration programmatically."""
        instance = cls(
            registry_path=Path(registry_path or defaults.REGISTRY_PATH),
            export_dir=Path(export_dir or defaults.EXPORT_DIR),
            compression_level=compression_level or defaults.COMPRESSION,
            workers=workers or defaults.WORKERS,
            registry_token=registry_token,
            log_level=(log_level or defaults.LOG_LEVEL).upper(),
        )
        if cache_instance:
            cls._set_instance(instance)
        return instance

    def to_dict(self) -> dict[str, str | int | bool]:
        """Return a serializable dictionary version."""
        return {
            "registry_path": str(self.registry_path),
            "export_dir": str(self.export_dir),
            "compression_level": self.compression_level,
            "workers": self.workers,
            "registry_token": bool(self.registry_token),
            "log_level": self.log_level,
        }

    @classmethod
    def current(cls, overrides: Optional[dict[str, Any]] = None) -> MapigenConfig:
        """Return the active configuration, optionally with overrides."""
        base = cls._instance or cls.from_env()
        if overrides:
            return base.with_overrides(**overrides)
        return base

    def with_overrides(self, **overrides: Any) -> MapigenConfig:
        """Return a derived config with specific fields overridden."""
        updated = self.to_dict()
        updated.update(overrides)
        return MapigenConfig.from_dict(updated)

    @classmethod
    def _set_instance(cls, instance: MapigenConfig) -> None:
        """Cache and synchronize logging."""
        cls._instance = instance
        cls._sync_logging(instance)

    @staticmethod
    def _sync_logging(config: MapigenConfig) -> None:
        """Synchronize structlog logging with current config."""
        try:
            from mapigen.logging import setup_logging
            setup_logging(config)
        except Exception:
            pass

    def __repr__(self) -> str:
        return (
            f"<MapigenConfig "
            f"log_level={self.log_level} "
            f"workers={self.workers} "
            f"compression={self.compression_level}>"
        )
