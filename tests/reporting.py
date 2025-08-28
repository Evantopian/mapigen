import yaml
from pathlib import Path
from collections import defaultdict
from typing import Any, Callable, List

from mapigen import Mapi, MapiError

# This dictionary is the single source of truth for which credentials
# are needed for each integration test.
REQUIRED_CREDS = {
    "discord": ["DISCORD_BOT_TOKEN", "TEST_CHANNEL_ID"],
    "github": ["GITHUB_TOKEN", "TEST_GITHUB_USER"],
    "pokeapi": [], # No specific credentials required for basic PokeAPI tests
}


def run_test_operation(
    client: Mapi,
    service_name: str,
    op_name: str,
    operations_checked: List[str],
    assertion_callback: Callable[[Any], None],
    success_message_template: str,
    **kwargs,
):
    """A helper function to run a single integration test operation.

    Args:
        client: The Mapi client.
        service_name: The name of the service being tested.
        op_name: The name of the operation being tested.
        operations_checked: A list to append the operation name to upon success.
        assertion_callback: A function that takes the response data and performs assertions.
        success_message_template: A message to print upon success. Can be a format string.
        **kwargs: Arguments to pass to client.execute().
    """
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


class TestReport:

    """A singleton class to collect and save integration test results."""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TestReport, cls).__new__(cls)
            cls._instance.results = defaultdict(dict)
            cls._instance.output_path = Path(__file__).resolve().parent.parent / "docs" / "integration_targets.yaml"
        return cls._instance

    def add_passed(self, service: str, checked: List[str], token_vars: List[str]):
        self.results["passed"][service] = {
            "checked": checked,
            "token_used": [f"${var}" for var in token_vars]
        }

    def add_failed(self, service: str, checked: List[str], error: MapiError):
        self.results["failed"][service] = {
            "checked": checked,
            "error": f"{error.http_status} {error.error_type}",
            "message": str(error)
        }

    def add_skipped(self, service: str):
        self.results["skipped"][service] = {
            "reason": "missing credentials",
            "creds_needed": REQUIRED_CREDS.get(service, [])
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
            )
        }
        final_yaml = {"info": header, "tests": dict(self.results)}

        with open(self.output_path, 'w') as f:
            yaml.dump(final_yaml, f, sort_keys=False, default_flow_style=False, indent=2)

        print(f"\nSuccessfully generated integration report at {self.output_path}")

# Singleton instance for use in tests
report = TestReport()
