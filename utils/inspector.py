import argparse
import json
from mapigen import Mapi
from mapigen.cache.storage import load_service_from_disk
import msgspec
from mapigen.models import ParameterRef
from mapigen.utils.compression_utils import decompress_zstd
from pathlib import Path

from typing import Any

def print_json(data: Any):
    """Prints data in a nicely formatted JSON."""
    # Use msgspec for encoding to handle custom types gracefully
    print(json.dumps(msgspec.to_builtins(data), indent=2))

def main():
    """Main function for the inspection utility."""
    parser = argparse.ArgumentParser(
        description="A command-line utility to inspect the Mapigen SDK's available services and operations."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # --- list-providers command ---
    subparsers.add_parser("list-providers", help="List all available provider names.")

    # --- list-apis command ---
    list_apis_parser = subparsers.add_parser("list-apis", help="List all APIs for a specific provider.")
    list_apis_parser.add_argument("provider", help="The name of the provider.")

    # --- list-ops command ---
    list_ops_parser = subparsers.add_parser("list-ops", help="List all operations for a specific API.")
    list_ops_parser.add_argument("provider", help="The name of the provider.")
    list_ops_parser.add_argument("api", help="The name of the API.")

    # --- get-op command ---
    get_op_parser = subparsers.add_parser("get-op", help="Get the detailed schema for a specific operation.")
    get_op_parser.add_argument("provider", help="The name of the provider.")
    get_op_parser.add_argument("api", help="The name of the API.")
    get_op_parser.add_argument("operation", help="The name of the operation.")

    # --- get-auth command ---
    get_auth_parser = subparsers.add_parser("get-auth", help="Get the authentication details for a specific API.")
    get_auth_parser.add_argument("provider", help="The name of the provider.")
    get_auth_parser.add_argument("api", help="The name of the API.")

    # --- decompress command ---
    decompress_parser = subparsers.add_parser("decompress", help="Decompress a zstd file.")
    decompress_parser.add_argument("file_path", help="The path to the file to decompress.")

    args = parser.parse_args()
    client = Mapi()

    if args.command == "list-providers":
        print_json(client.discovery.list_providers())
    
    elif args.command == "list-apis":
        print_json(client.discovery.list_apis(args.provider))

    elif args.command == "list-ops":
        print_json(client.discovery.list_operations(args.provider, args.api))

    elif args.command == "get-auth":
        api_info = client.discovery.get_api_info(args.provider, args.api)
        print_json(api_info)

    elif args.command == "get-op":
        api_info = client.discovery.get_api_info(args.provider, args.api)
        if not api_info.sources:
            print(f"Error: No sources found for API '{args.api}' in provider '{args.provider}'.")
            return
        source = api_info.sources[0] # Use default source

        operation_data = client.discovery.get_operation(args.provider, args.api, args.operation, source)
        if operation_data:
            full_service_data = load_service_from_disk(args.provider, args.api, source)
            resolved_params = []
            for param in operation_data.parameters:
                if isinstance(param, ParameterRef):
                    component_name = param.component_name
                    param_details = full_service_data.components.parameters.get(component_name)
                    if param_details:
                        resolved_params.append(param_details)
                else:
                    resolved_params.append(param)
            
            operation_data_dict = msgspec.to_builtins(operation_data)
            operation_data_dict["parameters"] = msgspec.to_builtins(resolved_params)
            print_json(operation_data_dict)
        else:
            print(f"Error: Operation '{args.operation}' not found in API '{args.api}'.")

    elif args.command == "decompress":
        file_path = Path(args.file_path)
        if not file_path.exists():
            print(f"Error: File not found at {file_path}")
            return

        decompressed_data = decompress_zstd(file_path.read_bytes())
        
        output_path = file_path.with_suffix('')
        output_path.write_bytes(decompressed_data)
        print(f"File decompressed to: {output_path}")

if __name__ == "__main__":
    main()
