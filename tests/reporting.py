from __future__ import annotations
import orjson as json
from pathlib import Path
from typing import Any, Callable, List
from dataclasses import asdict

from mapigen import Mapi, MapiError
from .helpers import ResultReporter, VALID_CALL_4XX

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


def _save_payload_if_enabled(service_name: str, op_name: str, response_wrapper: dict) -> str | None:
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

        with open(file_path, "wb") as f:
            f.write(json.dumps(data_to_save, option=json.OPT_INDENT_2))
        return str(file_path)
    return None

def run_test_operation(
    client: Mapi,
    service_name: str,
    op_name: str,
    report: "ResultReporter",
    operations_checked: List[str],
    assertion_callback: Callable[[Any], None],
    **kwargs,
):
    """
    A helper function to run a single integration test operation and report the result.
    It centralizes error handling and classification.
    """
    response_wrapper = None
    try:
        response_wrapper = client.execute(service_name, op_name, **kwargs)
        metadata = response_wrapper.get("metadata")
        data = response_wrapper.get("data")

        # Case 1: Non-exception errors (e.g., validation error from the SDK)
        if metadata and metadata.status == "error":
            error = MapiError(
                message=f"Operation failed with error type: {metadata.error_type}",
                service=service_name,
                operation=op_name,
                error_type=metadata.error_type or "unknown",
            )
            # http_status is not applicable for pre-flight validation errors
            report.add_failed(service_name, op_name, error)
            return response_wrapper

        # Case 2: Successful execution (2xx)
        assert data is not None, f"Data was null for a successful operation: {op_name}"
        assertion_callback(data)
        operations_checked.append(op_name)

        payload_path = _save_payload_if_enabled(service_name, op_name, response_wrapper)
        if metadata:
            report.add_passed(service_name, op_name, metadata.duration_ms, payload_path or "")

    except MapiError as e:
        # Case 3: Exception errors (e.g., HTTP 4xx/5xx from the server)
        status = getattr(e, 'http_status', None)
        if status and status in VALID_CALL_4XX:
            report.add_expected_client_error(service_name, op_name, e)
        else:
            report.add_failed(service_name, op_name, e)
        
        # Create a mock response wrapper for consistent return type
        if not response_wrapper:
             # This is a private method, but essential for consistent reporting
            metadata = client._create_metadata(service_name, op_name, 0, error=e)
            response_wrapper = {"data": None, "metadata": metadata}

    return response_wrapper