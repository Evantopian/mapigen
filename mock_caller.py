from mapigen import Mapi

def main():
    """Demonstrates how to use the mapi."""
    print("--- Initializing mapi ---")
    client = Mapi()

    print("\n--- Making a call to pokeapi.api_v2_pokemon_retrieve(id=25) ---")
    response = client.execute("pokeapi", "api_v2_pokemon_retrieve", id=320)

    if response:
        print("\n--- API Response ---")
        # Print a subset of the response for brevity
        print(f"Name: {response.get('name')}")
        print(f"ID: {response.get('id')}")
        print(f"Base Experience: {response.get('base_experience')}")
        types = [t['type']['name'] for t in response.get('types', [])]
        print(f"Types: {types}")

if __name__ == "__main__":
    main()
