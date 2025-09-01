import pytest
from dotenv import load_dotenv

from mapigen import Mapi, MapiError
from ..helpers import report
from ..reporting import run_test_operation, REQUIRED_CREDS

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
    if SERVICE_NAME not in REQUIRED_CREDS:
        report.add_skipped(SERVICE_NAME, REQUIRED_CREDS[SERVICE_NAME])
        pytest.skip(f"Skipping {SERVICE_NAME} tests; service not configured in REQUIRED_CREDS.")

    operations_checked = []
    op_name = ""
    try:
        # --- Test 1: Get Ditto ---
        op_name = "api_v2_pokemon_retrieve"
        pokemon_id_ditto = "ditto"

        def assert_ditto_data(data):
            assert data.get("name") == pokemon_id_ditto

        run_test_operation(
            client=client,
            service_name=SERVICE_NAME,
            op_name=op_name,
            report=report,
            operations_checked=operations_checked,
            assertion_callback=assert_ditto_data,
            id=pokemon_id_ditto,
        )

        # --- Test 2: Get Pikachu ---
        op_name = "api_v2_pokemon_retrieve"
        pokemon_id_pikachu = "pikachu"

        def assert_pikachu_data(data):
            assert data.get("name") == pokemon_id_pikachu

        run_test_operation(
            client=client,
            service_name=SERVICE_NAME,
            op_name=op_name,
            report=report,
            operations_checked=operations_checked,
            assertion_callback=assert_pikachu_data,
            id=pokemon_id_pikachu,
        )

    except MapiError as e:
        print(f"--- CAUGHT EXPECTED ERROR for {SERVICE_NAME} ---")
        print(e)
        report.add_failed(SERVICE_NAME, op_name, e)
