import os
import pytest
from dotenv import load_dotenv

from mapigen import Mapi, Auth, MapiError
from ..reporting import report, REQUIRED_CREDS, run_test_operation

# Load environment variables from .env file
load_dotenv()

# --- Test Data ---
SERVICE_NAME = "discord"
TOKEN = os.getenv("DISCORD_BOT_TOKEN")
CHANNEL_ID = os.getenv("TEST_CHANNEL_ID")


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
        report.add_skipped(SERVICE_NAME)
        pytest.skip(f"Skipping {SERVICE_NAME} tests; missing required credentials.")
        return

    operations_checked = []
    try:
        # --- Test 1: Create Message ---
        content = "Hello from a Mapigen integration test!"

        def assert_create_message(data):
            assert data.get("content") == content

        run_test_operation(
            client=client,
            service_name=SERVICE_NAME,
            op_name="create_message",
            operations_checked=operations_checked,
            assertion_callback=assert_create_message,
            success_message_template="SUCCESS: Message sent with ID: {id}",
            channel_id=CHANNEL_ID,
            content=content,
        )

        # --- Test 2: Get Channel ---
        def assert_get_channel(data):
            assert data.get("id") == CHANNEL_ID

        run_test_operation(
            client=client,
            service_name=SERVICE_NAME,
            op_name="get_channel",
            operations_checked=operations_checked,
            assertion_callback=assert_get_channel,
            success_message_template="SUCCESS: Retrieved channel '{name}'",
            channel_id=CHANNEL_ID,
        )

        # If all tests passed, report success
        report.add_passed(
            SERVICE_NAME, operations_checked, REQUIRED_CREDS[SERVICE_NAME]
        )

    except MapiError as e:
        print(f"--- CAUGHT EXPECTED ERROR for {SERVICE_NAME} ---")
        print(e)
        report.add_failed(SERVICE_NAME, operations_checked, e)