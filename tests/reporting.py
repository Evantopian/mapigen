from __future__ import annotations
import orjson as json
from pathlib import Path
from typing import Any, Callable, List, Dict
from dataclasses import asdict

from mapigen import Mapi, MapiError
from .helpers import result_reporter, VALID_CALL_4XX

# This dictionary is the single source of truth for which credentials
# are needed for each integration test.
REQUIRED_CREDS: Dict[str, List[str]] = {
    "discord": ["DISCORD_BOT_TOKEN", "TEST_CHANNEL_ID", "DISCORD_MESSAGE_ID"],
    "github": ["GITHUB_TOKEN", "TEST_GITHUB_USER"],
    "pokeapi": [],  # No specific credentials required for basic PokeAPI tests
}

# This dictionary controls which services will have their payloads saved to tmp/.
SAVE_PAYLOAD_TOGGLE: Dict[str, bool] = {
    "discord": True,
    "github": True,
    "pokeapi": True,
}

def _save_payload_if_enabled(provider_name: str, api_name: str, op_name: str, response_wrapper: Dict[str, Any]) -> str | None:
    """Checks the toggle and saves the full response payload if enabled."""
    if SAVE_PAYLOAD_TOGGLE.get(api_name, False):
        tmp_dir = Path(__file__).resolve().parent.parent / "tmp"
        tmp_dir.mkdir(exist_ok=True)

        # Sanitize op_name for filename
        safe_op_name = op_name.replace("/", "_")
        file_path = tmp_dir / f"{provider_name}_{api_name}_{safe_op_name}_response.json"

        # Prepare data for serialization
        data_to_save: Dict[str, Any] = response_wrapper.copy()
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
    provider_name: str,
    api_name: str,
    op_name: str,
    operations_checked: List[str],
    assertion_callback: Callable[[Any], None],
    **kwargs: Any,
):
    """A helper function to run a single integration test operation and report the result."""
    service_key = f"{provider_name}/{api_name}"
    try:
        provider_proxy = getattr(client, provider_name)
        api_proxy = getattr(provider_proxy, api_name)
        response_wrapper = api_proxy(op_name, **kwargs)
        metadata = response_wrapper.get("metadata")

        if metadata and metadata.status == "success":
            assertion_callback(response_wrapper.get("data"))
            result_reporter.add_passed(service_key, op_name, metadata.duration_ms)
        elif (metadata and metadata.http_status in VALID_CALL_4XX) or (metadata and metadata.error_type == "validation"):
            error = MapiError(
                f"Expected client error: {metadata.http_status or metadata.error_type}", 
                service=service_key, 
                operation=op_name, 
                error_type=metadata.error_type,
                http_status=metadata.http_status
            )
            result_reporter.add_http_validated_call(service_key, op_name, error)
        else:
            error = MapiError(
                f"Unexpected error: {metadata.error_type if metadata else 'Unknown'}", 
                service=service_key, 
                operation=op_name, 
                error_type=getattr(metadata, 'error_type', 'unknown')
            )
            result_reporter.add_failed(service_key, op_name, error)

    except MapiError as e:
        result_reporter.add_failed(service_key, op_name, e)
    except Exception as e:
        error = MapiError(f"Unhandled exception: {e}", service=service_key, operation=op_name, error_type="test_framework_error")
        result_reporter.add_failed(service_key, op_name, error)
    
    operations_checked.append(op_name)