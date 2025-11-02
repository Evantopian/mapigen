"""
Mapigen – API Contract Bundler and Registry Engine
==================================================

Core compiler and packager for the MAPI ecosystem.

Responsibilities:
- Fetch and normalize API specifications from registry sources
- Compile msgspec-based bundles
- Compress and export portable `.tar.zst` bundles for Mapispec distribution
"""

from __future__ import annotations
import os

from mapigen.config import MapigenConfig
from mapigen.logging import setup_logging
from mapigen.models import (
    RegistrySource,
    OperatorSchema,
    ServiceModel,
    BundleMetadata,
    BuildContext,
    ErrorRecord,
)
from mapigen.types import defaults




try:
    if any(k.startswith("MAPIGEN_") for k in os.environ):
        setup_logging(MapigenConfig.from_env())
except Exception:
    pass

__all__ = [
    "MapigenConfig",
    "setup_logging",
    "defaults",
    "RegistrySource",
    "OperatorSchema",
    "ServiceModel",
    "BundleMetadata",
    "BuildContext",
    "ErrorRecord",
]

__version__ = "1.0.0"
