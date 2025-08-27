from mapigen import Mapi, RequestError

def main():
    """Demonstrates how to use the mapi."""
    print("--- Initializing mapi ---")
    client = Mapi()

    print("\n--- Making a call to pokeapi.api_v2_pokemon_retrieve(id='ditto') ---")
    try:
        response = client.pokeapi.api_v2_pokemon_retrieve(id="ditto")

        if response and isinstance(response, dict):
            print("\n--- API Response ---")
            # Print a subset of the response for brevity
            print(f"Name: {response.get('name')}")
            print(f"ID: {response.get('id')}")
            print(f"Base Experience: {response.get('base_experience')}")
            types_data = response.get('types', [])
            types = [t['type']['name'] for t in types_data] if isinstance(types_data, list) else []
            print(f"Types: {types}")

        # Example with metadata
        print("\n--- Making a call with include_metadata=True ---")
        result_with_meta = client.pokeapi.api_v2_pokemon_retrieve(id="pikachu", include_metadata=True)
        if result_with_meta and isinstance(result_with_meta, dict) and result_with_meta.get("data"):
            data = result_with_meta.get("data", {})
            metadata = result_with_meta.get("metadata")
            print("SUCCESS: Got data and metadata.")
            print(f"Data: {data.get('name')}")
            print(f"Metadata: {metadata}")

    except RequestError as e:
        print(f"\n--- CAUGHT EXPECTED ERROR ---")
        print(f"Error Type: {e.error_type}")
        print(f"Error Category: {e.error_category}")
        print(f"HTTP Status: {e.http_status}")
        print(f"Message: {e}")


if __name__ == "__main__":
    main()
