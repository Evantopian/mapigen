import yaml
import json
from pathlib import Path
from collections import defaultdict
from typing import Any, Callable, List
from dataclasses import asdict

from mapigen import Mapi, MapiError

# This dictionary is the single source of truth for which credentials
# are needed for each integration test.
REQUIRED_CREDS = {
    "discord": ["DISCORD_BOT_TOKEN", "TEST_CHANNEL_ID", "DISCORD_MESSAGE_ID"],
    "github": ["GITHUB_TOKEN", "TEST_GITHUB_USER"],
    "pokeapi": [],  # No specific credentials required for basic PokeAPI tests
}

# This dictionary controls which services will have their payloads saved to tmp/.
SAVE_PAYLOAD_TOGGLE = {
    "discord": True,
    "github": True,
    "pokeapi": True,
}


def _save_payload_if_enabled(service_name: str, op_name: str, response_wrapper: dict):
    """Checks the toggle and saves the full response payload if enabled."""
    if SAVE_PAYLOAD_TOGGLE.get(service_name, False):
        tmp_dir = Path(__file__).resolve().parent.parent / "tmp"
        tmp_dir.mkdir(exist_ok=True)

        # Sanitize op_name for filename
        safe_op_name = op_name.replace("/", "_")
        file_path = tmp_dir / f"{service_name}_{safe_op_name}_response.json"

        # Prepare data for serialization
        data_to_save = response_wrapper.copy()
        if "metadata" in data_to_save and hasattr(
            data_to_save["metadata"], "__dataclass_fields__"
        ):
            data_to_save["metadata"] = asdict(data_to_save["metadata"])

        with open(file_path, "w") as f:
            json.dump(data_to_save, f, indent=2)
        print(f"SUCCESS: Saved payload to {file_path}")


def run_test_operation(
    client: Mapi,
    service_name: str,
    op_name: str,
    operations_checked: List[str],
    assertion_callback: Callable[[Any], None],
    success_message_template: str,
    **kwargs,
):
    """A helper function to run a single integration test operation."""
    print(f"\n--- Testing: {service_name.capitalize()} {op_name} ---")
    response_wrapper = client.execute(service_name, op_name, **kwargs)
    data = response_wrapper.get("data")
    assert data is not None, f"Data was null for {op_name}"

    assertion_callback(data)

    operations_checked.append(op_name)

    if isinstance(data, dict):
        print(success_message_template.format(**data))
    else:
        print(success_message_template)

    # Save the payload if the service is toggled on
    _save_payload_if_enabled(service_name, op_name, response_wrapper)


class TestReport:
    """A singleton class to collect and save integration test results."""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TestReport, cls).__new__(cls)
            cls._instance.results = defaultdict(dict)
            cls._instance.output_path = (
                Path(__file__).resolve().parent.parent / "docs" / "integration_targets.yaml"
            )
        return cls._instance

    def add_passed(self, service: str, checked: List[str], token_vars: List[str]):
        self.results["passed"][service] = {
            "checked": checked,
            "token_used": [f"${var}" for var in token_vars],
        }

    def add_failed(self, service: str, checked: List[str], error: MapiError):
        self.results["failed"][service] = {
            "checked": checked,
            "error": f"{error.http_status} {error.error_type}",
            "message": str(error),
        }

    def add_skipped(self, service: str):
        self.results["skipped"][service] = {
            "reason": "missing credentials",
            "creds_needed": REQUIRED_CREDS.get(service, []),
        }

    def save(self):
        """Writes the collected results to the YAML file."""
        if not self.results:
            return

        header = {
            "title": "Integration Test Targets Status",
            "description": (
                "This file is an auto-generated report on the status of integration tests. "
                "Tests may be skipped due to missing credentials in your .env file."
            ),
        }
        final_yaml = {"info": header, "tests": dict(self.results)}

        with open(self.output_path, "w") as f:
            yaml.dump(final_yaml, f, sort_keys=False, default_flow_style=False, indent=2)

        print(f"\nSuccessfully generated integration report at {self.output_path}")


# Singleton instance for use in tests
report = TestReport()