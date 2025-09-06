from __future__ import annotations
import json
import logging
from datetime import datetime, timezone
from pathlib import Path

import msgspec

from mapigen.models import ServiceRegistry, ApiInfo, MetadataFile

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

class RegistryService:
    """A service for managing the service registry."""

    def __init__(self, data_dir: Path, registry_path: Path):
        self.data_dir = data_dir
        self.registry_path = registry_path

    def build_registry(self) -> ServiceRegistry:
        """Builds the hierarchical service registry from metadata files."""
        providers: dict[str, dict[str, ApiInfo]] = {}

        if not self.data_dir.exists():
            logging.warning(f"Data directory {self.data_dir} not found. Returning empty registry.")
            return ServiceRegistry(version="2.0", generated_at="", providers={})

        for provider_dir in self.data_dir.iterdir():
            if not provider_dir.is_dir():
                continue
            provider_name = provider_dir.name

            for source_dir in provider_dir.iterdir():
                if not source_dir.is_dir():
                    continue
                source_name = source_dir.name

                for api_dir in source_dir.iterdir():
                    if not api_dir.is_dir():
                        continue
                    api_name = api_dir.name

                    metadata_path = api_dir / "metadata.yml"
                    if not metadata_path.exists():
                        continue

                    try:
                        metadata = msgspec.yaml.decode(metadata_path.read_text(), type=MetadataFile)

                        if provider_name not in providers:
                            providers[provider_name] = {}
                        
                        if api_name not in providers[provider_name]:
                            providers[provider_name][api_name] = ApiInfo(
                                sources=[source_name],
                                operation_count=metadata.operation_count,
                                popularity_rank=metadata.popularity_rank,
                                auth_types=metadata.auth_types,
                                primary_auth=metadata.primary_auth,
                            )
                        else:
                            # Append source if API info already exists
                            existing_api_info = providers[provider_name][api_name]
                            if source_name not in existing_api_info.sources:
                                existing_api_info.sources.append(source_name)

                    except (msgspec.ValidationError, TypeError) as e:
                        logging.warning(f"Skipping {provider_name}/{source_name}/{api_name} due to invalid metadata: {e}")

        return ServiceRegistry(
            version="2.0",
            generated_at=datetime.now(timezone.utc).isoformat(),
            providers=providers
        )

    def save_registry(self, registry: ServiceRegistry):
        """Saves the service registry to a file."""
        if not registry.providers:
            logging.warning("Service registry is empty. Nothing to save.")
            return

        logging.info(f"Writing global service registry to {self.registry_path}...")
        
        builtins_registry = msgspec.to_builtins(registry)
        
        with open(self.registry_path, "w", encoding="utf-8") as f:
            json.dump(builtins_registry, f, indent=2)
            f.write("\n")