from dataclasses import dataclass
from typing import Optional, Dict, Any, NamedTuple

@dataclass
class RequestOptions:
    timeout: float = 30.0
    include_metadata: bool = False
    verify_ssl: bool = True

class RequestConfig(NamedTuple):
    method: str
    url: str
    params: Dict[str, Any]
    headers: Dict[str, Any]
    json_body: Dict[str, Any]
    options: RequestOptions

@dataclass
class ResponseMetadata:
    service: str
    operation: str
    duration_ms: int
    status: str  # "success" | "error"
    http_status: Optional[int]
    timestamp: str
    error_type: Optional[str] = None
    error_category: Optional[str] = None
