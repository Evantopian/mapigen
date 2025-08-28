from mapigen import Mapi, MapiError

def test_pokeapi_calls():
    """Tests various calls to the PokeAPI service."""
    print("--- Initializing mapi for PokeAPI test ---")
    client = Mapi()

    print("\n--- Making a call to pokeapi.api_v2_pokemon_retrieve(id='ditto') ---")
    try:
        response = client.pokeapi.api_v2_pokemon_retrieve(id="ditto")

        assert response is not None
        assert isinstance(response, dict)
        assert response.get('name') == 'ditto'
        print("\n--- API Response for Ditto ---")
        print(f"Name: {response.get('name')}")
        print(f"ID: {response.get('id')}")

        # Example with metadata
        print("\n--- Making a call with include_metadata=True ---")
        result_with_meta = client.pokeapi.api_v2_pokemon_retrieve(id="pikachu", include_metadata=True)
        
        assert result_with_meta is not None
        assert isinstance(result_with_meta, dict)
        assert "data" in result_with_meta and "metadata" in result_with_meta
        
        data = result_with_meta.get("data", {})
        metadata = result_with_meta.get("metadata")

        print("SUCCESS: Got data and metadata for Pikachu.")
        assert isinstance(data, dict)
        assert data.get('name') == 'pikachu'
        assert metadata is not None and metadata.status == 'success'
        print(f"Data: {data.get('name')}")
        print(f"Metadata Status: {metadata.status}")

    except MapiError as e:
        print("\n--- CAUGHT UNEXPECTED ERROR ---")
        print(f"Message: {e}")
        # This test should not fail, so we re-raise the exception
        raise e
