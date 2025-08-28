import os
import pytest
from dotenv import load_dotenv

from mapigen import Mapi, Auth

# Load environment variables from .env file in the project root
load_dotenv()

# --- Credentials ---
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
TEST_GITHUB_USER = "Evantopian"  # Linus Torvalds, a stable target

# Pytest marker to skip tests if credentials are not provided
requires_github_creds = pytest.mark.skipif(
    not GITHUB_TOKEN,
    reason="Test requires GITHUB_TOKEN in .env file"
)

@pytest.fixture(scope="module")
def client() -> Mapi:
    """Pytest fixture to initialize the Mapi client with GitHub auth."""
    if not GITHUB_TOKEN:
        pytest.skip("GITHUB_TOKEN not found in .env")
    return Mapi(auth=Auth.BearerAuth(GITHUB_TOKEN))

@requires_github_creds
def test_sync_get_user(client: Mapi):
    """Tests getting a user synchronously."""
    print(f"\n--- Testing: GitHub Get User '{TEST_GITHUB_USER}' (Sync) ---")
    response = client.execute("github", "users/get-by-username", username=TEST_GITHUB_USER)
    
    assert response is not None
    assert response.get('login') == TEST_GITHUB_USER
    print(f"Successfully retrieved user: {response.get('name')}")

@requires_github_creds
@pytest.mark.asyncio
async def test_async_get_user(client: Mapi):
    """Tests getting a user asynchronously."""
    print(f"\n--- Testing: GitHub Get User '{TEST_GITHUB_USER}' (Async) ---")
    response = await client.aexecute("github", "users/get-by-username", username=TEST_GITHUB_USER)
    
    assert response is not None
    assert response.get('login') == TEST_GITHUB_USER
    print(f"Successfully retrieved user: {response.get('name')}")
