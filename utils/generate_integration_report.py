import yaml
import re
from pathlib import Path
import xml.etree.ElementTree as ET
from collections import defaultdict
from typing import Dict, Any, List, Tuple
import sys

# Add src to path to allow importing mapigen
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from mapigen import Mapi

REPORT_PATH = Path(__file__).resolve().parent.parent / "pytest_report.xml"
OUTPUT_PATH = Path(__file__).resolve().parent.parent / "docs" / "integration_targets.yaml"

# This dictionary maps the API name to the required environment variables for auth
REQUIRED_CREDS = {
    "discord": ["DISCORD_BOT_TOKEN", "TEST_CHANNEL_ID"],
    "github": ["GITHUB_TOKEN"],
    "spotify": ["SPOTIFY_CLIENT_ID", "SPOTIFY_CLIENT_SECRET"], # Example for spotify
    "stripe": ["STRIPE_API_KEY"], # Example for stripe
}

def get_service_from_test_name(classname: str) -> Tuple[str, str]:
    """Extracts the provider and api name from the test's classname attribute."""
    filename = classname.split('.')[-1]
    
    # Match generated tests: test_provider_api_generated
    match_gen = re.match(r"test_([a-z0-9_]+)_([a-z0-9_]+)_generated", filename)
    if match_gen:
        return match_gen.group(1), match_gen.group(2) # (provider, api)

    # Match manual tests: test_api_integration
    match_manual = re.match(r"test_([a-z0-9_]+)_integration", filename)
    if match_manual:
        api = match_manual.group(1)
        # For manual tests, we assume provider and api name are the same
        return api, api
        
    return "general", "general"

def get_operation_from_test_name(test_name: str) -> str:
    return test_name.split('[')[0].replace("test_", "").replace("_", " ")

def main():
    if not REPORT_PATH.exists():
        print(f"Error: Report file not found at {REPORT_PATH}")
        return

    client = Mapi()
    tree = ET.parse(REPORT_PATH)
    root = tree.getroot()

    results: Dict[str, Dict[str, List[Dict[str, Any]]]] = defaultdict(lambda: defaultdict(list))

    for testcase in root.findall(".//testcase"):
        test_name = testcase.get("name", "")
        class_name = testcase.get("classname", "")
        provider, api = get_service_from_test_name(class_name)
        operation = get_operation_from_test_name(test_name)

        if provider == "general":
            continue

        service_key = f"{provider}/{api}"
        status = "passed"
        details: Dict[str, Any] = {"checked": [operation]}

        failure_node = testcase.find("failure")
        skipped_node = testcase.find("skipped")

        if failure_node is not None:
            status = "failed"
            message = failure_node.text or ""
            error_code = "Unknown Error"
            if "401" in message:
                error_code = "401 Unauthorized"
            elif "400" in message:
                error_code = "400 Bad Request"
            elif "404" in message:
                error_code = "404 Not Found"
            elif "500" in message:
                error_code = "500 Server Error"
            details["error"] = error_code
            details["auth_methods"] = client.discovery.get_api_info(provider, api).auth_types

        elif skipped_node is not None:
            status = "skipped"
            details = {
                "reason": "missing credentials",
                "creds_needed": REQUIRED_CREDS.get(api, []),
                "auth_methods": client.discovery.get_api_info(provider, api).auth_types
            }
        
        if status == "passed" and api in REQUIRED_CREDS:
            details["token_used"] = [f"${var}" for var in REQUIRED_CREDS[api]]

        # Aggregate operations under the same service key
        found = False
        for item in results[status].get(service_key, []):
            if "checked" in item:
                item["checked"].append(operation)
                found = True
                break
        if not found:
            if service_key not in results[status]:
                results[status][service_key] = []
            results[status][service_key].append(details)

    output_data = {k: dict(v) for k, v in results.items()}

    header = {
        "title": "Integration Test Targets Status",
        "description": (
            "This file is an auto-generated report on the status of integration tests. "
            "Skipped tests usually reference missing credentials to be implemented."
        )
    }
    final_yaml = {"info": header, "tests": output_data}

    with open(OUTPUT_PATH, 'w') as f:
        yaml.dump(final_yaml, f, sort_keys=False, default_flow_style=False, indent=2)

    print(f"Successfully generated integration report at {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
