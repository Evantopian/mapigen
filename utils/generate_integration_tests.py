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
from typing import Any, List
from jinja2 import Environment, FileSystemLoader

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

def get_all_service_keys() -> set[str]:
    """Gets all available service keys from the DiscoveryClient."""
    try:
        # This should be updated to get all service keys
        # For now, we will just get all apis and assume a default source
        return set(DiscoveryClient().list_apis())
    except Exception as e:
        logging.error("Failed to discover services: %s", e)
        return set()

def get_existing_integration_tests(output_dir: Path) -> set[str]:
    """Finds existing integration tests and extracts the service names."""
    if not output_dir.is_dir():
        return set()
    existing_tests = set()
    for f in output_dir.glob("test_*_integration.py"):
        service_name = f.name.replace("test_", "").replace("_integration.py", "")
        existing_tests.add(service_name)
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
    """
    Selects 5 representative GET/POST operations and creates min/max param test cases for them.
    """
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
                    ref_name = param.ref.split('/')[-1]
                    if ref_name in service_data.components.parameters:
                        all_params.append(service_data.components.parameters[ref_name])
                else:
                    all_params.append(param)

        required_params = [p for p in all_params if getattr(p, 'required', False)]
        optional_params = [p for p in all_params if not getattr(p, 'required', False)]

        min_params_dict = {p.name: generate_dummy_data(p) for p in required_params}
        test_cases.append({"op_name": op_name, "params_dict": min_params_dict, "case_name": f"{op_name} (min_params)"})

        if optional_params:
            max_params_dict = min_params_dict.copy()
            for p in optional_params:
                max_params_dict[p.name] = generate_dummy_data(p)
            test_cases.append({"op_name": op_name, "params_dict": max_params_dict, "case_name": f"{op_name} (max_params)"})

    return test_cases

def parse_arguments() -> argparse.Namespace:
    """Parses command-line arguments."""
    parser = argparse.ArgumentParser(description="Generate integration test files for services.")
    parser.add_argument("--service", type=str, nargs="+", help="The name of the service(s) to generate tests for.")
    parser.add_argument("--output-dir", type=Path, default=Path(__file__).resolve().parent.parent / "tests" / "integration", help="The directory to output the generated test files.")
    parser.add_argument("--dry-run", action="store_true", help="Perform a dry run without creating any files.")
    parser.add_argument("--force", action="store_true", help="Force overwrite of existing test files.")
    return parser.parse_args()

def main():
    """Main function to orchestrate the test generation."""
    args = parse_arguments()
    logging.info("Starting test generation script with arguments: %s", args)

    template_dir = Path(__file__).resolve().parent
    env = Environment(loader=FileSystemLoader(template_dir), trim_blocks=True, lstrip_blocks=True)
    template = env.get_template("integration_test.py.j2")

    all_services = DiscoveryClient().list_apis()
    if not all_services:
        logging.error("No services found. Aborting.")
        return

    existing_tests = get_existing_integration_tests(args.output_dir)
    services_to_generate = set(all_services) - existing_tests
    if args.service:
        services_to_generate = set(args.service) & set(all_services)

    if not services_to_generate:
        logging.info("No new test files need to be generated.")
        return

    logging.info("Services to generate tests for: %s", sorted(list(services_to_generate)))

    for service_name in sorted(list(services_to_generate)):
        output_file = args.output_dir / f"test_{service_name}_integration.py"
        if output_file.exists() and not args.force:
            logging.warning("Skipping existing file: %s (use --force to overwrite)", output_file)
            continue

        logging.info("Preparing to generate test for '%s' at %s", service_name, output_file)
        try:
            discovery = DiscoveryClient()
            provider, api, source = discovery.parse_service_key(service_name) # service_name is actually a service_key here
            service_path = discovery.get_service_path(provider, source, api)
            service_data = load_service_from_disk(service_path)
            test_cases = create_sampled_test_cases(service_data)
            if not test_cases:
                logging.warning("No GET or POST operations found for service %s, skipping.", service_name)
                continue

            rendered_content = template.render(service_name=service_name, test_cases=test_cases)

            if args.dry_run:
                logging.info("DRY RUN: Would write %d bytes to %s", len(rendered_content), output_file)
                continue

            output_file.parent.mkdir(parents=True, exist_ok=True)
            with open(output_file, "w") as f:
                f.write(rendered_content)
            logging.info("Successfully wrote test file: %s", output_file)

            py_compile.compile(output_file, doraise=True)
            logging.info("Successfully validated syntax of %s", output_file)

        except py_compile.PyCompileError as e:
            logging.critical("SYNTAX ERROR in generated file %s. Deleting it. Error: %s", output_file, e)
            output_file.unlink()
        except Exception as e:
            logging.error("Failed to generate or validate file for service %s: %s", service_name, e)
            if 'output_file' in locals() and output_file.exists():
                output_file.unlink()

    logging.info("Test generation script finished.")

if __name__ == "__main__":
    main()