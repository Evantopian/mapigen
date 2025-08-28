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
        report.add_skipped(SERVICE_NAME)
        pytest.skip(f"Skipping {SERVICE_NAME} tests; missing required credentials.")
        return

    operations_checked = []
    try:
        # --- Test 1: Create Message ---
        content = "Mapi Client test..."
        created_message_id = None # Declare variable to store the created message ID

        def assert_create_message(data):
            nonlocal created_message_id # Use nonlocal to modify the outer variable
            created_message_id = data.get("id")
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

        # --- Test 3: List Messages ---
        def assert_list_messages(data):
            assert isinstance(data, list)
            assert len(data) <= 5

        run_test_operation(
            client=client,
            service_name=SERVICE_NAME,
            op_name="list_messages",
            operations_checked=operations_checked,
            assertion_callback=assert_list_messages,
            success_message_template="SUCCESS: Retrieved recent messages.",
            channel_id=CHANNEL_ID,
            limit=5,
        )
        
        def assert_get_messages(data):
            # Removed content assertion as MESSAGE_ID is hardcoded and content may vary.
            # If you want to assert on content, update this line with the expected content
            # for the message referred to by MESSAGE_ID.
            assert data.get("id") == MESSAGE_ID # Assert that the retrieved message ID matches the requested ID   
        
        run_test_operation(
            client=client,
            service_name=SERVICE_NAME,
            op_name="get_message",
            operations_checked=operations_checked,
            assertion_callback=assert_get_messages,
            success_message_template="SUCCESS: Retrieved message '{content}' with ID: {id}", # Updated message
            channel_id=CHANNEL_ID,
            message_id=MESSAGE_ID, # Use the hardcoded MESSAGE_ID
        )

        # If all tests passed, report success
        report.add_passed(
            SERVICE_NAME, operations_checked, REQUIRED_CREDS[SERVICE_NAME]
        )

    except MapiError as e:
        print(f"--- CAUGHT EXPECTED ERROR for {SERVICE_NAME} ---")
        print(e)
        report.add_failed(SERVICE_NAME, operations_checked, e)
