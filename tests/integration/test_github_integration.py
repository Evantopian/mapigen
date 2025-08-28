import os
import pytest
from dotenv import load_dotenv

from mapigen import Mapi, Auth, MapiError
from ..reporting import report, REQUIRED_CREDS, run_test_operation

# Load environment variables from .env file
load_dotenv(override=True)

# --- Test Data ---
SERVICE_NAME = "github"
TOKEN = os.getenv("GITHUB_TOKEN")
TEST_USER = os.getenv("TEST_GITHUB_USER")

@pytest.fixture(scope="module")
def client() -> Mapi:
    """Pytest fixture to initialize the Mapi client with GitHub auth."""
    if not TOKEN:
        pytest.skip("GITHUB_TOKEN not found, skipping client fixture.")
    return Mapi(auth=Auth.BearerAuth(TOKEN))


def test_github_integration(client: Mapi):
    """Runs a series of integration tests for the GitHub service."""
    if not all([TOKEN, TEST_USER]):
        report.add_skipped(SERVICE_NAME)
        pytest.skip(f"Skipping {SERVICE_NAME} tests; missing required credentials.")
        return

    operations_checked = []
    try:
        # --- Test 1: Get User ---
        def assert_get_user(data):
            assert data.get("login") == TEST_USER

        run_test_operation(
            client=client,
            service_name=SERVICE_NAME,
            op_name="users/get-by-username",
            operations_checked=operations_checked,
            assertion_callback=assert_get_user,
            success_message_template="SUCCESS: Retrieved user '{name}'",
            username=TEST_USER,
        )

        # --- Add more tests here in the future ---

        # If all tests in the try block passed, report success
        report.add_passed(
            SERVICE_NAME, operations_checked, REQUIRED_CREDS[SERVICE_NAME]
        )

    except MapiError as e:
        print(f"--- CAUGHT EXPECTED ERROR for {SERVICE_NAME} ---")
        print(e)
        report.add_failed(SERVICE_NAME, operations_checked, e)
