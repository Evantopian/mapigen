from __future__ import annotations
import json
import logging
from pathlib import Path
from typing import Dict

import msgspec

from mapigen.models import ServiceInfo

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

class RegistryService:
    """A service for managing the service registry."""

    def __init__(self, data_dir: Path, registry_path: Path):
        self.data_dir = data_dir
        self.registry_path = registry_path

    def build_registry(self) -> Dict[str, ServiceInfo]:
        """Builds the service registry from metadata files."""
        service_registry: Dict[str, ServiceInfo] = {}
        for service_dir in self.data_dir.iterdir():
            if service_dir.is_dir():
                metadata_path = service_dir / "metadata.yml"
                if metadata_path.exists():
                    try:
                        metadata = msgspec.yaml.decode(metadata_path.read_text())
                        service_registry[service_dir.name] = ServiceInfo(
                            operation_count=metadata.get("operation_count", 0),
                            auth_types=metadata.get("auth_types", []),
                            primary_auth=metadata.get("primary_auth", "none"),
                            popularity_rank=metadata.get("popularity_rank", 999),
                        )
                    except msgspec.ValidationError as e:
                        logging.warning(f"Skipping {service_dir.name} due to invalid metadata: {e}")
        return service_registry

    def save_registry(self, service_registry: Dict[str, ServiceInfo]):
        """Saves the service registry to a file."""
        if not service_registry:
            logging.warning("Service registry is empty. Nothing to save.")
            return

        logging.info(f"Writing global service registry to {self.registry_path}...")
        # Convert msgspec.Structs to built-in types for pretty-printing
        builtins_registry = msgspec.to_builtins(service_registry)
        
        # Use standard json library for pretty-printing
        with open(self.registry_path, "w", encoding="utf-8") as f:
            json.dump(builtins_registry, f, indent=2)
            f.write("\n")
