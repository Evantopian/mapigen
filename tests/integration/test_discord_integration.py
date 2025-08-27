import os
import pytest
from dotenv import load_dotenv

from typing import Any

from mapigen import Mapi
from niquests.auth import AuthBase
from niquests.models import PreparedRequest

# Load environment variables from .env file in the project root
load_dotenv()

# --- Credentials ---
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
TEST_CHANNEL_ID = os.getenv("TEST_CHANNEL_ID")

# --- Auth Helper for Discord Bot Tokens ---
class BotTokenAuth(AuthBase):
    """Injects the 'Bot' token into the Authorization header."""
    def __init__(self, token: Any):
        self.token = token

    def __call__(self, r: PreparedRequest) -> PreparedRequest:
        if r.headers is not None:
            r.headers['Authorization'] = f'Bot {self.token}'
        return r

# Pytest marker to skip tests if credentials are not provided
requires_discord_creds = pytest.mark.skipif(
    not all([DISCORD_BOT_TOKEN, TEST_CHANNEL_ID]),
    reason="Test requires DISCORD_BOT_TOKEN and TEST_CHANNEL_ID in .env file"
)

@pytest.fixture(scope="module")
def client() -> Mapi:
    """Pytest fixture to initialize the Mapi client with Discord auth."""
    if not DISCORD_BOT_TOKEN:
        pytest.skip("DISCORD_BOT_TOKEN not found in .env")
    return Mapi(auth=BotTokenAuth(DISCORD_BOT_TOKEN))

@requires_discord_creds
def test_sync_create_and_list_messages(client: Mapi):
    """Tests creating a message and then listing it, synchronously."""
    print("--- Testing: Push Message (Sync) ---")
    content = "Hello from the Mapigen SDK! (Sync Integration Test)"
    response = client.discord.create_message(channel_id=TEST_CHANNEL_ID, content=content)
    
    assert response is not None
    assert response.get('content') == content
    print(f"Message sent! ID: {response.get('id')}")

    print("\n--- Testing: Read Messages (Sync) ---")
    messages = client.discord.list_messages(channel_id=TEST_CHANNEL_ID)
    
    assert messages is not None
    assert len(messages) > 0
    assert messages[0].get('content') == content
    print(f"Successfully retrieved {len(messages)} messages.")

@requires_discord_creds
@pytest.mark.asyncio
async def test_async_create_and_list_messages(client: Mapi):
    """Tests creating a message and then listing it, asynchronously."""
    print("\n--- Testing: Push Message (Async) ---")
    content = "Hello from the Mapigen SDK! (Async Integration Test)"
    response = await client.discord.create_message.aexecute(channel_id=TEST_CHANNEL_ID, content=content)
    
    assert response is not None
    assert response.get('content') == content
    print(f"Message sent! ID: {response.get('id')}")

    print("\n--- Testing: Read Messages (Async) ---")
    messages = await client.discord.list_messages.aexecute(channel_id=TEST_CHANNEL_ID)
    
    assert messages is not None
    assert len(messages) > 0
    assert messages[0].get('content') == content
    print(f"Successfully retrieved {len(messages)} messages.")
