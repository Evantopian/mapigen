"""
A script to automatically generate functional, data-driven integration tests for services
using a 5-point sampling method for operations.
"""
import argparse
import logging
from pathlib import Path
import sys
import py_compile
import random
import re
from typing import Any, List
from jinja2 import Environment, FileSystemLoader
from concurrent.futures import ThreadPoolExecutor, as_completed

# Add src to path to allow importing mapigen
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from mapigen.discovery import DiscoveryClient
from mapigen.models import ServiceData, Parameter, ParameterRef
from mapigen.cache.storage import load_service_from_disk

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def get_all_provider_apis() -> set[tuple[str, str]]:
    """Gets all available (provider, api) tuples from the DiscoveryClient."""
    try:
        client = DiscoveryClient()
        provider_apis = set()
        for provider in client.list_providers():
            for api in client.list_apis(provider):
                provider_apis.add((provider, api))
        return provider_apis
    except Exception as e:
        logging.error("Failed to discover services: %s", e)
        return set()

def get_existing_integration_tests(output_dir: Path) -> set[tuple[str, str]]:
    """Finds existing generated integration tests and extracts the (provider, api) tuples."""
    if not output_dir.is_dir():
        return set()
    existing_tests = set()
    for f in output_dir.glob("test_*_*_generated.py"):
        match = re.match(r"test_([a-z0-9_]+)_([a-z0-9_A-Z]+)_generated.py", f.name)
        if match:
            provider, api = match.groups()
            existing_tests.add((provider, api))
    return existing_tests

def generate_dummy_data(param: Parameter) -> Any:
    """Generates plausible dummy data based on a parameter's JSON schema."""
    schema = param.schema_
    param_type = schema.get("type")
    if "default" in schema:
        return schema["default"]
    if "enum" in schema and schema["enum"]:
        return random.choice(schema["enum"])

    if param_type == "string":
        return f"test_{param.name}"
    elif param_type == "integer":
        return 1
    elif param_type == "number":
        return 1.1
    elif param_type == "boolean":
        return True
    elif param_type == "array":
        return []
    elif param_type == "object":
        return {}
    return "unknown_type"

def create_sampled_test_cases(service_data: ServiceData) -> List[dict]:
    """Selects 5 representative GET/POST operations and creates test cases for them."""
    test_cases = []
    get_post_ops = {
        op_name: op_details
        for op_name, op_details in service_data.operations.items()
        if op_details.method.upper() in ["GET", "POST"]
    }
    if not get_post_ops:
        return []

    sorted_op_names = sorted(get_post_ops.keys())
    op_count = len(sorted_op_names)

    indices_to_sample = sorted(list(set([
        0, # Min
        op_count // 4, # Min-Med
        op_count // 2, # Med
        (op_count * 3) // 4, # Max-Med
        op_count - 1, # Max
    ])))

    sampled_op_names = [sorted_op_names[i] for i in indices_to_sample]
    logging.info("Sampled operations for %s: %s", service_data.service_name, sampled_op_names)

    for op_name in sampled_op_names:
        op_details = get_post_ops[op_name]
        all_params = []
        if op_details.parameters:
            for param in op_details.parameters:
                if isinstance(param, ParameterRef):
                    ref_name = param.component_name
                    if ref_name in service_data.components.parameters:
                        all_params.append(service_data.components.parameters[ref_name])
                else:
                    all_params.append(param)

        # Path parameters are always required, even if not explicitly marked
        required_params = [p for p in all_params if getattr(p, 'required', False) or p.in_ == "path"]
        optional_params = [p for p in all_params if not getattr(p, 'required', False) and p.in_ != "path"]

        max_params_dict = {p.name: generate_dummy_data(p) for p in required_params}
        for p in optional_params:
            max_params_dict[p.name] = generate_dummy_data(p)
        test_cases.append({"op_name": op_name, "params_dict": max_params_dict, "case_name": f"{op_name}"})

    return test_cases

def parse_arguments() -> argparse.Namespace:
    """Parses command-line arguments."""
    parser = argparse.ArgumentParser(description="Generate integration test files for services.")
    parser.add_argument("--provider", type=str, help="The name of the provider to generate tests for.")
    parser.add_argument("--api", type=str, help="The name of the API to generate tests for.")
    parser.add_argument("--output-dir", type=Path, default=Path(__file__).resolve().parent.parent / "tests" / "integration", help="The directory to output the generated test files.")
    parser.add_argument("--dry-run", action="store_true", help="Perform a dry run without creating any files.")
    parser.add_argument("--force", action="store_true", help="Force overwrite of existing test files.")
    parser.add_argument("--workers", type=int, default=4, help="Number of parallel workers for test generation.")
    return parser.parse_args()

def generate_for_service(provider: str, api: str, args: argparse.Namespace, env: Environment):
    """Generates a single test file for a given provider/api pair."""
    output_file = args.output_dir / f"test_{provider}_{api}_generated.py"
    if output_file.exists() and not args.force:
        logging.warning("Skipping existing file: %s (use --force to overwrite)", output_file)
        return

    logging.info("Preparing to generate test for '%s/%s' at %s", provider, api, output_file)
    try:
        client = DiscoveryClient()
        api_info = client.get_api_info(provider, api)
        if not api_info.sources:
            logging.warning("No sources found for %s/%s, skipping.", provider, api)
            return
        source = api_info.sources[0] # Use default source

        service_data = load_service_from_disk(provider, api, source)
        test_cases = create_sampled_test_cases(service_data)
        if not test_cases:
            logging.warning("No GET or POST operations found for service %s/%s, skipping.", provider, api)
            return

        template = env.get_template("integration_test.py.j2")
        rendered_content = template.render(provider_name=provider, api_name=api, test_cases=test_cases)

        if args.dry_run:
            logging.info("DRY RUN: Would write %d bytes to %s", len(rendered_content), output_file)
            return

        output_file.parent.mkdir(parents=True, exist_ok=True)
        with open(output_file, "w") as f:
            f.write(rendered_content)
        logging.info("Successfully wrote test file: %s", output_file)

        py_compile.compile(str(output_file), doraise=True)
        logging.info("Successfully validated syntax of %s", output_file)

    except py_compile.PyCompileError as e:
        logging.critical("SYNTAX ERROR in generated file %s. Deleting it. Error: %s", output_file, e)
        output_file.unlink()
    except Exception as e:
        logging.error("Failed to generate or validate file for service %s/%s: %s", provider, api, e)
        if 'output_file' in locals() and output_file.exists():
            output_file.unlink()

def main():
    """Main function to orchestrate the test generation."""
    args = parse_arguments()
    logging.info("Starting test generation script with arguments: %s", args)

    template_dir = Path(__file__).resolve().parent / "templates"
    env = Environment(loader=FileSystemLoader(template_dir), trim_blocks=True, lstrip_blocks=True)

    all_provider_apis = get_all_provider_apis()
    if not all_provider_apis:
        logging.error("No services found. Aborting.")
        return

    existing_tests = get_existing_integration_tests(args.output_dir)
    
    if args.provider and args.api:
        services_to_generate = {(args.provider, args.api)} & all_provider_apis
    elif args.provider:
        services_to_generate = {s for s in all_provider_apis if s[0] == args.provider}
    else:
        services_to_generate = all_provider_apis - existing_tests

    if not services_to_generate:
        logging.info("No new test files need to be generated.")
        return

    logging.info("Services to generate tests for: %s", sorted(list(services_to_generate)))
    
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = [executor.submit(generate_for_service, provider, api, args, env) for provider, api in sorted(list(services_to_generate))]
        for future in as_completed(futures):
            future.result() # Raise exceptions if any occurred

    logging.info("Test generation script finished.")

if __name__ == "__main__":
    main()