from __future__ import annotations
import json
import logging
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict

import msgspec

from mapigen.models import ServiceMetadata, ServiceRegistry

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

class RegistryService:
    """A service for managing the service registry."""

    def __init__(self, data_dir: Path, registry_path: Path):
        self.data_dir = data_dir
        self.registry_path = registry_path

    def build_registry(self) -> ServiceRegistry:
        """Builds the service registry from metadata files found in the data directory."""
        service_metadata: Dict[str, ServiceMetadata] = {}
        
        for metadata_path in self.data_dir.glob("**/*/metadata.yml"):
            try:
                metadata = msgspec.yaml.decode(metadata_path.read_text())
                provider = metadata.get("provider")
                api = metadata.get("api")
                source = metadata.get("source")

                if not all([provider, api, source]):
                    logging.warning(f"Skipping {metadata_path} due to missing provider, api, or source.")
                    continue

                service_key = f"{provider}:{api}:{source}"
                
                # For now, 'tested' is hardcoded. This can be enhanced later.
                service_metadata[service_key] = ServiceMetadata(
                    resolvable=True,
                    tested=False, # Placeholder
                    last_updated=metadata.get("updated_at", datetime.now(timezone.utc).isoformat())
                )
            except (msgspec.ValidationError, TypeError, KeyError) as e:
                logging.warning(f"Skipping {metadata_path} due to invalid metadata: {e}")
        
        return ServiceRegistry(
            version="2.0", # Bump version for new structure
            generated_at=datetime.now(timezone.utc).isoformat(),
            services=service_metadata
        )

    def save_registry(self, registry: ServiceRegistry):
        """Saves the service registry to a file using msgspec for performance."""
        if not registry.services:
            logging.warning("Service registry is empty. Nothing to save.")
            return

        logging.info(f"Writing global service registry with {len(registry.services)} entries to {self.registry_path}...")
        
        # Use msgspec to encode the registry for performance and correctness
        encoded_registry = msgspec.json.encode(registry)
        
        # Pretty-print using standard json for readability
        pretty_registry = json.loads(encoded_registry)
        with open(self.registry_path, "w", encoding="utf-8") as f:
            json.dump(pretty_registry, f, indent=2)
            f.write("\n")
