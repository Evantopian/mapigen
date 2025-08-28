
import pytest
from dotenv import load_dotenv

from mapigen import Mapi, MapiError
from ..reporting import report, REQUIRED_CREDS, run_test_operation

# Load environment variables from .env file
load_dotenv()

# --- Test Data ---
SERVICE_NAME = "pokeapi"


@pytest.fixture(scope="module")
def client() -> Mapi:
    """Pytest fixture to initialize the Mapi client for PokeAPI."""
    return Mapi()


def test_pokeapi_integration(client: Mapi):
    """Runs a series of integration tests for the PokeAPI service."""
    # PokeAPI does not require specific credentials for these basic calls.
    # We ensure that the service is recognized by the reporting system.
    if SERVICE_NAME not in REQUIRED_CREDS:
        report.add_skipped(SERVICE_NAME)
        pytest.skip(f"Skipping {SERVICE_NAME} tests; service not configured in REQUIRED_CREDS.")
        return

    operations_checked = []
    try:
        # --- Test 1: Get Ditto ---
        pokemon_id_ditto = "ditto"

        def assert_ditto_data(data):
            assert data.get("name") == pokemon_id_ditto

        run_test_operation(
            client=client,
            service_name=SERVICE_NAME,
            op_name="api_v2_pokemon_retrieve",
            operations_checked=operations_checked,
            assertion_callback=assert_ditto_data,
            success_message_template="SUCCESS: Retrieved {name} data.",
            id=pokemon_id_ditto,
        )

        # --- Test 2: Get Pikachu ---
        pokemon_id_pikachu = "pikachu"

        def assert_pikachu_data(data):
            assert data.get("name") == pokemon_id_pikachu

        run_test_operation(
            client=client,
            service_name=SERVICE_NAME,
            op_name="api_v2_pokemon_retrieve",
            operations_checked=operations_checked,
            assertion_callback=assert_pikachu_data,
            success_message_template="SUCCESS: Retrieved {name} data.",
            id=pokemon_id_pikachu,
        )

        # If all tests passed, report success
        report.add_passed(
            SERVICE_NAME, operations_checked, REQUIRED_CREDS[SERVICE_NAME]
        )

    except MapiError as e:
        print(f"--- CAUGHT EXPECTED ERROR for {SERVICE_NAME} ---")
        print(e)
        report.add_failed(SERVICE_NAME, operations_checked, e)
