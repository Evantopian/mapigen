import os
import pytest
from dotenv import load_dotenv

from mapigen import Mapi, Auth
from mapigen.client.exceptions import RequestError

# Load environment variables from .env file in the project root
load_dotenv()

# --- Credentials & Test Data ---
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
TEST_GITHUB_USER = os.getenv("TEST_GITHUB_USER")

# Pytest marker to skip tests if credentials are not provided
requires_github_creds = pytest.mark.skipif(
    not all([GITHUB_TOKEN, TEST_GITHUB_USER]),
    reason="Test requires GITHUB_TOKEN and TEST_GITHUB_USER in .env file"
)

@pytest.வதால்.fixture(scope="module")
def client() -> Mapi:
    """Pytest fixture to initialize the Mapi client with GitHub auth."""
    if not GITHUB_TOKEN:
        pytest.skip("GITHUB_TOKEN not found.")
    return Mapi(auth=Auth.BearerAuth(GITHUB_TOKEN))

@requires_github_creds
def test_sync_get_user(client: Mapi):
    """Tests getting a user synchronously."""
    print(f"\n--- Testing: GitHub Get User '{TEST_GITHUB_USER}' (Sync) ---")
    try:
        response_wrapper = client.execute("github", "users/get-by-username", username=TEST_GITHUB_USER)
        assert response_wrapper is not None
        response = response_wrapper.get('data')
        assert response is not None
        assert response.get('login') == TEST_GITHUB_USER
        print(f"Successfully retrieved user: {response.get('name')}")
    except RequestError as e:
        if e.http_status == 401:
            pytest.skip("Skipping test due to 401 Unauthorized. Is GITHUB_TOKEN valid?")
        raise e

@requires_github_creds
@pytest.mark.asyncio
async def test_async_get_user(client: Mapi):
    """Tests getting a user asynchronously."""
    print(f"\n--- Testing: GitHub Get User '{TEST_GITHUB_USER}' (Async) ---")
    try:
        response_wrapper = await client.aexecute("github", "users/get-by-username", username=TEST_GITHUB_USER)
        assert response_wrapper is not None
        response = response_wrapper.get('data')
        assert response is not None
        assert response.get('login') == TEST_GITHUB_USER
        print(f"Successfully retrieved user: {response.get('name')}")
    except RequestError as e:
        if e.http_status == 401:
            pytest.skip("Skipping test due to 401 Unauthorized. Is GITHUB_TOKEN valid?")
        raise e