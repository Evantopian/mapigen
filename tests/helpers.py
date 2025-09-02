from __future__ import annotations

from typing import Any
from pathlib import Path
import yaml
from collections import defaultdict

from mapigen.client.exceptions import MapiError

# This dictionary defines the set of 4xx status codes that are considered
# "valid" for the purpose of testing. They indicate the server understood
# the request, even if it was denied.
VALID_CALL_4XX = {
    401: "Unauthorized (expected if no auth provided)",
    403: "Forbidden (server understood request, access denied)",
    404: "Not Found (endpoint exists, resource may be missing)",
    405: "Method Not Allowed (endpoint exists, wrong HTTP method)",
    406: "Not Acceptable (headers mismatch, server understood request)",
    422: "Unprocessable Entity (request structure correct, semantic issue)",
    429: "Too Many Requests (rate limiting, server understood request)",
}




def create_unsupported_file(tmp_path: Path, extension: str) -> Path:
    """Creates a temporary file with an unsupported extension."""
    unsupported_file = tmp_path / f"test.{extension}"
    unsupported_file.write_text("test content")
    return unsupported_file

def create_mock_spec_with_broken_ref() -> dict[str, Any]:
    """Creates a mock spec with a broken $ref."""
    return {"components": {"parameters": {"param1": {"name": "param1"}}}}

class ResultReporter:
    """A singleton class to collect and save integration test results."""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ResultReporter, cls).__new__(cls)
            cls._instance.results = defaultdict(lambda: defaultdict(list))
            cls._instance.output_path = Path(__file__).resolve().parent.parent / "docs" / "integration_targets.yaml"
        return cls._instance

    def add_passed(self, service: str, op_name: str, duration_ms: int, payload_path: str):
        self.results[service]["passed"].append(
            {
                "operation": op_name,
                "duration_ms": duration_ms,
                "payload_path": payload_path,
            }
        )

    def add_failed(self, service: str, op_name: str, error: MapiError):
        self.results[service]["failed"].append(
            {
                "operation": op_name,
                "error": f"{getattr(error, 'http_status', 'N/A')} {error.error_type}",
                "message": str(error),
            }
        )

    def add_expected_client_error(self, service: str, op_name: str, error: MapiError):
        """Adds a result for a call that received an expected 4xx error."""
        status = getattr(error, 'http_status', 0)
        self.results[service]["expected_client_errors"].append(
            {
                "operation": op_name,
                "status": status,
                "details": VALID_CALL_4XX.get(status, "Unknown Expected Error"),
                "message": str(error),
            }
        )

    def add_skipped(self, service: str, creds_needed: list[str]):
        self.results[service]["skipped"] = {
            "reason": "missing credentials",
            "creds_needed": creds_needed,
        }

    def save(self):
        """Writes the collected results to the YAML file and prints a summary."""
        if not self.results:
            return

        header = {
            "title": "Integration Test Targets Status",
            "description": (
                "This file is an auto-generated report on the status of integration tests. "
                "Tests may be skipped due to missing credentials in your .env file. "
                "Expected client errors (4xx) are considered successful API calls."
            ),
        }
        final_yaml = {"info": header, "tests": dict(self.results)}

        with open(self.output_path, "w") as f:
            yaml.dump(final_yaml, f, sort_keys=False, default_flow_style=False, indent=2)

        print(f"\nIntegration test report successfully generated at {self.output_path}")


# Singleton instance for use in tests
result_reporter = ResultReporter()