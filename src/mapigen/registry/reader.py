from __future__ import annotations
from pathlib import Path
from typing import Any, cast
import msgspec
import yaml

from mapigen.models import RegistrySource, ErrorRecord, ErrorStage


class RegistryReader:
    """Auto-detects and reads registry source files (YAML or JSON)."""


    @classmethod
    def load(cls, path: Path) -> tuple[list[RegistrySource], list[ErrorRecord]]:
        """Load a single registry file and collect parsing errors."""
        entries: list[RegistrySource] = []
        errors: list[ErrorRecord] = []

        try:
            ext = path.suffix.lower()
            if ext in {".yaml", ".yml"}:
                raw_data = cls._load_yaml(path)
            elif ext == ".json":
                raw_data = cls._load_json(path)
            else:
                raise ValueError(f"Unsupported registry format: {ext}")

            for entry in raw_data:
                try:
                    src = msgspec.convert(entry, type=RegistrySource)
                    entries.append(src)
                except Exception as exc:
                    errors.append(
                        ErrorRecord(
                            stage=ErrorStage.PARSE,
                            message=str(exc),
                            file=str(path),
                        )
                    )

        except Exception as exc:
            errors.append(
                ErrorRecord(
                    stage=ErrorStage.LOAD,
                    message=str(exc),
                    file=str(path),
                )
            )

        return entries, errors

    @classmethod
    def load_all(cls, directory: Path) -> tuple[list[RegistrySource], list[ErrorRecord]]:
        """Recursively load all registry source files in a directory."""
        all_entries: list[RegistrySource] = []
        all_errors: list[ErrorRecord] = []

        for file in sorted(directory.rglob("*")):
            if file.suffix.lower() in {".yaml", ".yml", ".json"}:
                entries, errs = cls.load(file)
                all_entries.extend(entries)
                all_errors.extend(errs)

        return all_entries, all_errors


    @staticmethod
    def _load_json(path: Path) -> list[dict[str, Any]]:
        """Load and decode JSON content."""
        with open(path, "rb") as f:
            raw: Any = msgspec.json.decode(f.read())

        data: list[dict[str, Any]] = []
        if isinstance(raw, list):
            raw_list = cast(list[Any], raw)
            for item in raw_list:
                if isinstance(item, dict):
                    d = cast(dict[str, Any], item)
                    data.append({str(k): v for k, v in d.items()})
        elif isinstance(raw, dict):
            d = cast(dict[str, Any], raw)
            data.append({str(k): v for k, v in d.items()})
        return data

    @staticmethod
    def _load_yaml(path: Path) -> list[dict[str, Any]]:
        """Load and decode YAML content."""
        with open(path, "r", encoding="utf-8") as f:
            raw: Any = yaml.safe_load(f)

        data: list[dict[str, Any]] = []
        if isinstance(raw, list):
            raw_list = cast(list[Any], raw)
            for item in raw_list:
                if isinstance(item, dict):
                    d = cast(dict[str, Any], item)
                    data.append({str(k): v for k, v in d.items()})
        elif isinstance(raw, dict):
            d = cast(dict[str, Any], raw)
            data.append({str(k): v for k, v in d.items()})
        return data