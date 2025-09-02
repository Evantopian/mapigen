import os
import pytest
from dotenv import load_dotenv

from mapigen import Mapi, Auth
from ..helpers import result_reporter as report
from ..reporting import run_test_operation, REQUIRED_CREDS

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
        report.add_skipped(SERVICE_NAME, REQUIRED_CREDS[SERVICE_NAME])
        pytest.skip(f"Skipping {SERVICE_NAME} tests; missing required credentials.")

    operations_checked = []

    # --- Test 1: Get User ---
    op_name = "users/get-by-username"
    def assert_get_user(data):
        assert data.get("login") == TEST_USER

    run_test_operation(
        client=client,
        service_name=SERVICE_NAME,
        op_name=op_name,
        report=report,
        operations_checked=operations_checked,
        assertion_callback=assert_get_user,
        username=TEST_USER,
    )
