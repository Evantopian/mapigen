import yaml
import re
from pathlib import Path
import xml.etree.ElementTree as ET
from collections import defaultdict
from typing import Dict, Any, List



REPORT_PATH = Path(__file__).resolve().parent.parent / "pytest_report.xml"
OUTPUT_PATH = Path(__file__).resolve().parent.parent / "docs" / "integration_targets.yaml"

REQUIRED_CREDS = {
    "discord": ["DISCORD_BOT_TOKEN", "TEST_CHANNEL_ID"],
    "github": ["GITHUB_TOKEN"],
}

def get_service_from_test_name(classname: str) -> str:
    """Extracts the service name from the test's classname attribute based on its filename."""
    # e.g., tests.integration.test_github_integration -> test_github_integration
    filename = classname.split('.')[-1]
    
    # Use regex to match the pattern test_<service>_integration
    match = re.match(r"test_([a-z0-9_]+)_integration", filename)
    if match:
        return match.group(1)  # Return the captured group (the service name)
        
    return "general"

def get_operation_from_test_name(test_name: str) -> str:
    return test_name.replace("test_", "").replace("_", " ")

def main():
    if not REPORT_PATH.exists():
        print(f"Error: Report file not found at {REPORT_PATH}")
        return

    tree = ET.parse(REPORT_PATH)
    root = tree.getroot()

    results: Dict[str, Dict[str, List[Dict[str, Any]]]] = defaultdict(lambda: defaultdict(list))

    for testcase in root.findall(".//testcase"):
        test_name = testcase.get("name", "")
        class_name = testcase.get("classname", "")
        service = get_service_from_test_name(class_name)
        operation = get_operation_from_test_name(test_name)

        if service == "general":
            continue

        status = "passed"
        details: Dict[str, Any] = {"checked": [operation]}

        failure_node = testcase.find("failure")
        skipped_node = testcase.find("skipped")

        if failure_node is not None:
            status = "failed"
            # if "401" in message:
            #     error_code = "401 Unauthorized"
            # elif "400" in message:
            #     error_code = "400 Bad Request"
            # elif "500" in message:
            #     error_code = "500 Server Error"
            # details["error"] = error_code
            # details["auth_methods"] = client.discovery.get_auth_types(service)

        elif skipped_node is not None:
            status = "skipped"
            details = {
                "reason": "missing credentials",
                "creds_needed": REQUIRED_CREDS.get(service, []),
                # "auth_methods": client.discovery.get_auth_types(service)
            }
        
        if status == "passed" and service in REQUIRED_CREDS:
            details["token_used"] = [f"${var}" for var in REQUIRED_CREDS[service]]

        if service in results[status]:
            for item in results[status][service]:
                if "checked" in item and operation not in item["checked"]:
                    item["checked"].append(operation)
        else:
            results[status][service].append(details)

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
