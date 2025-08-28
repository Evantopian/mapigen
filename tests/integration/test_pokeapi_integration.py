import json
from dataclasses import asdict
from mapigen import Mapi, MapiError

def test_pokeapi_and_save_output():
    """Tests PokeAPI and saves the output to the tmp/ directory for analysis."""
    print("--- Initializing mapi for PokeAPI test ---")
    client = Mapi()
    tmp_dir = "tmp"

    print("\n--- Making a call to pokeapi.api_v2_pokemon_retrieve(id='ditto') ---")
    try:
        # --- Ditto call ---
        result = client.pokeapi.api_v2_pokemon_retrieve(id="ditto")
        
        assert result is not None
        assert isinstance(result, dict)
        assert result.get('data') is not None
        assert result['data'].get('name') == 'ditto'
        
        ditto_path = f"{tmp_dir}/pokeapi_ditto_response.json"
        with open(ditto_path, 'w') as f:
            if result.get("metadata"):
                result["metadata"] = asdict(result["metadata"]) # type: ignore
            json.dump(result, f, indent=2)
        print(f"SUCCESS: Saved Ditto response to {ditto_path}")

        # --- Pikachu call ---
        print("\n--- Making another call for Pikachu ---")
        result_pikachu = client.pokeapi.api_v2_pokemon_retrieve(id="pikachu")
        
        assert result_pikachu is not None
        assert isinstance(result_pikachu, dict)
        assert result_pikachu.get('data') is not None
        assert result_pikachu['data'].get('name') == 'pikachu'
        print("SUCCESS: Got data for Pikachu.")

    except MapiError as e:
        error_path = f"{tmp_dir}/pokeapi_error.log"
        print(f"\n--- CAUGHT UNEXPECTED ERROR --- Saving to {error_path}")
        with open(error_path, 'w') as f:
            f.write(f"Message: {e}\n")
            if hasattr(e, 'service'):
                f.write(f"Service: {e.service}\n")
            if hasattr(e, 'operation'):
                f.write(f"Operation: {e.operation}\n")
        raise e
