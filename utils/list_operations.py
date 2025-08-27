import sys
from mapigen import Mapi

def list_operations(service_name: str):
    """Prints all available operations for a given service."""
    print(f"--- Finding operations for service: {service_name} ---")
    client = Mapi()
    
    if not client.discovery.service_exists(service_name):
        print(f"Error: Service '{service_name}' not found.")
        return

    # This part of the original code is not directly available through the public interface.
    # We will load the service data to get the operations.
    try:
        service_data = client._load_service_data(service_name)
        operations = service_data.get("operations", {}).keys()
        if not operations:
            print("No operations found for this service.")
        else:
            for op in sorted(operations):
                print(op)
    except FileNotFoundError:
        print(f"Could not load service data for '{service_name}'.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python utils/list_operations.py <service_name>")
    else:
        list_operations(sys.argv[1])
