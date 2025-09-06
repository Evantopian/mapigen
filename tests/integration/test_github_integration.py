import os
import pytest
from dotenv import load_dotenv
from typing import Any, List, Dict

from mapigen import Mapi, Auth, MapiError
from ..helpers import result_reporter
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
        result_reporter.add_skipped(f"{SERVICE_NAME}/{SERVICE_NAME}", REQUIRED_CREDS[SERVICE_NAME])
        pytest.skip(f"Skipping {SERVICE_NAME} tests; missing required credentials.")

    operations_checked: List[str] = []
    op_name = ""
    try:
        # --- Test 1: Get User ---
        op_name = "users/get-by-username"
        def assert_get_user(data: Dict[str, Any]):
            assert data.get("login") == TEST_USER

        run_test_operation(
            client=client,
            provider_name=SERVICE_NAME,
            api_name=SERVICE_NAME,
            op_name=op_name,
            operations_checked=operations_checked,
            assertion_callback=assert_get_user,
            username=TEST_USER,
        )

    except MapiError as e:
        print(f"--- CAUGHT UNEXPECTED ERROR for {SERVICE_NAME} ---")
        print(e)
        result_reporter.add_failed(f"{SERVICE_NAME}/{SERVICE_NAME}", op_name, e)
