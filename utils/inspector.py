import argparse
import json
from mapigen import Mapi

from typing import Any

def print_json(data: Any):
    """Prints data in a nicely formatted JSON."""
    print(json.dumps(data, indent=2))

def main():
    """Main function for the inspection utility."""
    parser = argparse.ArgumentParser(
        description="A command-line utility to inspect the Mapigen SDK's available services and operations."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # --- list-services command ---
    subparsers.add_parser("list-services", help="List all available service names.")

    # --- list-ops command ---
    list_ops_parser = subparsers.add_parser("list-ops", help="List all operations for a specific service.")
    list_ops_parser.add_argument("service", help="The name of the service.")

    # --- get-op command ---
    get_op_parser = subparsers.add_parser("get-op", help="Get the detailed schema for a specific operation.")
    get_op_parser.add_argument("service", help="The name of the service.")
    get_op_parser.add_argument("operation", help="The name of the operation.")

    # --- get-auth command ---
    get_auth_parser = subparsers.add_parser("get-auth", help="Get the authentication details for a specific service.")
    get_auth_parser.add_argument("service", help="The name of the service.")

    args = parser.parse_args()
    client = Mapi()

    if args.command == "list-services":
        print_json(client.discovery.list_services())
    
    elif args.command == "list-ops":
        print_json(client.discovery.list_operations(args.service))

    elif args.command == "get-auth":
        auth_info = {
            "auth_types": client.discovery.get_auth_types(args.service),
            "primary_auth": client.discovery.get_primary_auth(args.service)
        }
        print_json(auth_info)

    elif args.command == "get-op":
        operation_data = client.discovery.get_operation(args.service, args.operation)
        if operation_data:
            print_json(operation_data)
        else:
            print(f"Error: Operation '{args.operation}' not found in service '{args.service}'.")

if __name__ == "__main__":
    main()
