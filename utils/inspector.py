import argparse
import json

from mapigen.discovery import DiscoveryClient
import msgspec

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

    # --- list-apis command ---
    subparsers.add_parser("list-apis", help="List all available API names.")

    # --- list-sources command ---
    list_sources_parser = subparsers.add_parser("list-sources", help="List all available sources for a specific API.")
    list_sources_parser.add_argument("api", help="The name of the API.")

    # --- get-service command ---
    get_service_parser = subparsers.add_parser("get-service", help="Get the detailed metadata for a specific service key.")
    get_service_parser.add_argument("service_key", help="The full service key (e.g., provider:api:source).")

    args = parser.parse_args()
    discovery = DiscoveryClient()

    if args.command == "list-apis":
        print_json(discovery.list_apis())
    
    elif args.command == "list-sources":
        print_json(discovery.list_sources_for_api(args.api))

    elif args.command == "get-service":
        print_json(msgspec.to_builtins(discovery.get_service_details(args.service_key)))

if __name__ == "__main__":
    main()
