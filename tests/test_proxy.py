import sys
from pathlib import Path
# Add src to path to allow importing mapigen
sys.path.append(str(Path(__file__).resolve().parent.parent / 'src'))

from mapigen import Mapi

def run_test():
    print("Initializing Mapi client...")
    client = Mapi()

    print("Testing dynamic proxy for PokeAPI...")
    try:
        # PokeAPI does not require auth. This operation ID was found by inspecting the spec.
        result = client.pokeapi.api_v2_pokemon_retrieve(id='ditto')
        if result and 'name' in result and result['name'] == 'ditto':
            print("Proxy test successful! Received data for Ditto.")
        else:
            print(f"Proxy test may have failed. Unexpected result: {result}")

    except Exception as e:
        print(f"Proxy test failed with an unexpected exception: {e}")


    print("\nTesting a service that doesn\'t exist...")
    try:
        # This should fail with an AttributeError because the service is not in services.json
        client.non_existent_service.foo.bar()
    except AttributeError as e:
        print("Successfully caught expected AttributeError for non-existent service.")
    except Exception as e:
        print(f"Caught unexpected exception for non-existent service: {e}")


if __name__ == "__main__":
    run_test()
