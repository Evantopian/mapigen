from __future__ import annotations
from typing import Optional
import msgspec
from mapigen.types import PathLike
from enum import StrEnum

class RegistrySource(msgspec.Struct, frozen=True):
    provider: str
    api: str
    url: str
    enabled: bool = True


class OperatorSchema(msgspec.Struct, frozen=True):
    operation_id: str
    method: str
    path: str
    parameters: dict[str, str]
    request_body: Optional[dict[str, str]] = None
    responses: dict[str, str] = {}
    auth_type: Optional[str] = None


class ServiceModel(msgspec.Struct, frozen=True):
    provider: str
    api: str
    operations: dict[str, OperatorSchema]
    metadata: dict[str, str]

class BundleMetadata(msgspec.Struct, frozen=True):
    service: str
    version: str
    hash: str
    files: dict[str, str]
    size_bytes: int
    build_time: str


class BuildContext(msgspec.Struct, frozen=True):
    service: str
    source: RegistrySource
    model: Optional[ServiceModel] = None
    output_dir: PathLike = "/tmp/mapigen"



class ErrorStage(StrEnum):
    LOAD = "load"
    PARSE = "parse"
    VALIDATE = "validate"
    EXPORT = "export"
    UNKNOWN = "unknown"
    
    

class ErrorRecord(msgspec.Struct, frozen=True, kw_only=True):
    stage: ErrorStage
    message: str 
    detail: Optional[str] = None
    file: Optional[str] = None
    provider: Optional[str] = None
    api: Optional[str] = None
