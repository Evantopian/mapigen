import os
import pytest
from dotenv import load_dotenv
from typing import Any, List, Dict

from mapigen import Mapi, Auth, MapiError
from ..helpers import result_reporter
from ..reporting import run_test_operation, REQUIRED_CREDS

# Load environment variables from .env file
load_dotenv()

# --- Test Data ---
SERVICE_NAME = "discord"
TOKEN = os.getenv("DISCORD_BOT_TOKEN")
CHANNEL_ID = os.getenv("TEST_CHANNEL_ID")
MESSAGE_ID = os.getenv("DISCORD_MESSAGE_ID")


@pytest.fixture(scope="module")
def client() -> Mapi:
    """Pytest fixture to initialize the Mapi client with Discord auth."""
    if not TOKEN:
        pytest.skip("DISCORD_BOT_TOKEN not found, skipping client fixture.")
    # Discord requires a special "Bot" scheme for its token.
    return Mapi(auth=Auth.BearerAuth(TOKEN, scheme="Bot"))


def test_discord_integration(client: Mapi):
    """Runs a series of integration tests for the Discord service."""
    if not all([TOKEN, CHANNEL_ID]):
        result_reporter.add_skipped(f"{SERVICE_NAME}/{SERVICE_NAME}", REQUIRED_CREDS[SERVICE_NAME])
        pytest.skip(f"Skipping {SERVICE_NAME} tests; missing required credentials.")

    operations_checked: List[str] = []
    op_name = ""
    try:
        # --- Test 1: Create Message ---
        op_name = "create_message"
        content = "Mapi Client test..."

        def assert_create_message(data: Dict[str, Any]):
            assert data.get("content") == content

        run_test_operation(
            client=client,
            provider_name=SERVICE_NAME,
            api_name=SERVICE_NAME,
            op_name=op_name,
            operations_checked=operations_checked,
            assertion_callback=assert_create_message,
            channel_id=CHANNEL_ID,
            content=content,
        )

        # --- Test 2: Get Channel ---
        op_name = "get_channel"
        def assert_get_channel(data: Dict[str, Any]):
            assert data.get("id") == CHANNEL_ID

        run_test_operation(
            client=client,
            provider_name=SERVICE_NAME,
            api_name=SERVICE_NAME,
            op_name=op_name,
            operations_checked=operations_checked,
            assertion_callback=assert_get_channel,
            channel_id=CHANNEL_ID,
        )

        # --- Test 3: List Messages ---
        op_name = "list_messages"
        def assert_list_messages(data: List[Dict[str, Any]]):
            assert isinstance(data, list)
            assert len(data) <= 5

        run_test_operation(
            client=client,
            provider_name=SERVICE_NAME,
            api_name=SERVICE_NAME,
            op_name=op_name,
            operations_checked=operations_checked,
            assertion_callback=assert_list_messages,
            channel_id=CHANNEL_ID,
            limit=5,
        )
        
        # --- Test 4: Get Message ---
        op_name = "get_message"
        def assert_get_messages(data: Dict[str, Any]):
            assert data.get("id") == MESSAGE_ID
        
        run_test_operation(
            client=client,
            provider_name=SERVICE_NAME,
            api_name=SERVICE_NAME,
            op_name=op_name,
            operations_checked=operations_checked,
            assertion_callback=assert_get_messages,
            channel_id=CHANNEL_ID,
            message_id=MESSAGE_ID,
        )

    except MapiError as e:
        print(f"--- CAUGHT UNEXPECTED ERROR for {SERVICE_NAME} ---")
        print(e)
        result_reporter.add_failed(f"{SERVICE_NAME}/{SERVICE_NAME}", op_name, e)
