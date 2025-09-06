from __future__ import annotations

from typing import Any, Dict
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
    407: "Proxy Authentication Required (proxy auth missing/invalid)",
    409: "Conflict (valid request, but resource state conflict)",
    410: "Gone (resource used to exist, no longer available)",
    415: "Unsupported Media Type (request format not supported)",
    417: "Expectation Failed (server understood, can't meet Expect header)",
    422: "Unprocessable Entity (request structure correct, semantic issue)",
    428: "Precondition Required (missing conditional headers)",
    429: "Too Many Requests (rate limiting, server understood request)",
    431: "Request Header Fields Too Large (headers exceed server limits)",
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

    _instance: 'ResultReporter | None' = None
    results: Dict[str, Dict[str, Any]]
    output_path: Path

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ResultReporter, cls).__new__(cls)
            cls._instance.results = defaultdict(lambda: defaultdict(list))
            cls._instance.output_path = Path(__file__).resolve().parent.parent / "docs" / "integration_targets.yaml"
        return cls._instance

    def add_passed(self, service: str, op_name: str, duration_ms: int):
        self.results[service]["passed"].append(op_name)

    def add_failed(self, service: str, op_name: str, error: MapiError):
        error_code = getattr(error, 'http_status', 'N/A')
        error_type = error.error_type or "unknown"
        self.results[service]["failed"].append(f"{op_name} ({error_code}: {error_type})")

    def add_http_validated_call(self, service: str, op_name: str, error: MapiError):
        """Adds a result for a call that received an expected 4xx or validation error."""
        status = getattr(error, 'http_status', 'N/A')
        if status in VALID_CALL_4XX:
            details = VALID_CALL_4XX[status]
            self.results[service]["http_validated"].append(f"{op_name} ({status}: {details})")
        else:
            error_type = error.error_type or "validation"
            self.results[service]["http_validated"].append(f"{op_name} (validation: {error_type})")

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
                "It uses a 5-point sampling method to select a representative subset of operations. "
                "Calls that are successfully sent and receive an expected error (e.g., 4xx) are listed under http_validated."
            ),
        }
        final_yaml = {"info": header, "tests": dict(self.results)}

        with open(self.output_path, "w") as f:
            yaml.dump(final_yaml, f, sort_keys=False, default_flow_style=False, indent=2)

        print(f"\nIntegration test report successfully generated at {self.output_path}")


# Singleton instance for use in tests
result_reporter = ResultReporter()
