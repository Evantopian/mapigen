from __future__ import annotations
from pathlib import Path
from typing import Any, cast 
import msgspec 

from mapigen.models import RegistrySource, ErrorRecord, ErrorStage
from mapigen.utils.file import read_file_auto 
from mapigen.types import InputFileType


class RegistryReader:
    """Auto-detects and reads registry source files (YAML or JSON)."""

    @classmethod
    def load(cls, path: Path) -> tuple[list[RegistrySource], list[ErrorRecord]]:
        """
        Load a single registry file and collect parsing errors.
        
        This method uses `read_file_auto` for file I/O and initial decoding, 
        and then converts raw data entries into RegistrySource structs.
        """
        entries: list[RegistrySource] = []
        errors: list[ErrorRecord] = []

        try:
            raw_data: Any = read_file_auto(path) 
            
            if not isinstance(raw_data, list):
                raw_data = [raw_data] if isinstance(raw_data, dict) else []
            
            raw_data = [d for d in raw_data if isinstance(d, dict)] # type: ignore

            for entry in raw_data:
                try:
                    entry_dict = cast(dict[str, Any], entry)
                    src = msgspec.convert(entry_dict, type=RegistrySource)
                    entries.append(src)
                except Exception as exc:
                    errors.append(
                        ErrorRecord(
                            stage=ErrorStage.PARSE,
                            message=str(exc),
                            file=str(path),
                        )
                    )

        except ValueError as exc:

            if isinstance(exc.args[0], ErrorRecord):
                errors.append(exc.args[0])
            else:
                 errors.append(
                    ErrorRecord(
                        stage=ErrorStage.LOAD,
                        message="Unexpected loading error",
                        detail=str(exc),
                        file=str(path),
                    )
                )

        return entries, errors

    @classmethod
    def load_all(cls, directory: Path) -> tuple[list[RegistrySource], list[ErrorRecord]]:
        """
        Recursively load all registry source files (YAML/JSON) in a directory.
        
        It aggregates results and errors from all successfully read files.
        """
        all_entries: list[RegistrySource] = []
        all_errors: list[ErrorRecord] = []
        
        for file in sorted(directory.rglob("*")):
            if file.suffix.lower() in InputFileType:
                entries, errs = cls.load(file)
                all_entries.extend(entries)
                all_errors.extend(errs)

        return all_entries, all_errors