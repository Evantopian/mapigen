from __future__ import annotations
from typing import List

import msgspec


class ServiceInfo(msgspec.Struct):
    """Represents the metadata for a single service in the registry."""
    operation_count: int
    auth_types: List[str]
    primary_auth: str
    popularity_rank: int