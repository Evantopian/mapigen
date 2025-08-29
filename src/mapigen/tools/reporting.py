from __future__ import annotations
from pathlib import Path
from typing import Any, Dict, List

# Define paths relative to this module
SRC_DIR = Path(__file__).resolve().parent.parent
REGISTRY_DIR = SRC_DIR / "registry"
AUTH_NOTICE_PATH = REGISTRY_DIR / "AUTH_NOTICE.md"

def generate_auth_notice(services_requiring_fix: list[str], services_with_override: list[str]):
    """Generates the AUTH_NOTICE.md file with details on overrides."""
    content = """# Authentication Override Notice

This document tracks which API specifications have had their authentication information manually overridden.
"""

    content += "\n## Services with Active Overrides\n\n"
    if services_with_override:
        content += "The following services are using authentication details from `overrides.json`:\n"
        for service in sorted(services_with_override):
            content += f"- `{service}`\n"
    else:
        content += "No services are currently using an authentication override.\n"

    content += "\n## Services Requiring Attention\n\n"
    if services_requiring_fix:
        content += "The following services have no declared authentication types after processing and may require an override to be added to `overrides.json`:\n"
        for service in sorted(services_requiring_fix):
            content += f"- `{service}`\n"
    else:
        content += "No services appear to require an authentication override at this time.\n"

    AUTH_NOTICE_PATH.write_text(content)

def generate_performance_report(download_results: List[Dict[str, Any]], processing_results: List[Dict[str, Any]], total_duration: float):
    """Generates and prints a performance report from the collected metrics."""
    successful_downloads = [r for r in download_results if r["status"] == "success"]
    successful_processing = [r for r in processing_results if r["status"] == "success"]
    
    print("\n--- Performance Report ---")
    print(f"Total execution time: {total_duration:.2f}s")
    
    if download_results:
        print(f"\nDownload Phase: {len(download_results)} services")
        if successful_downloads:
            download_times = [r["download_duration"] for r in successful_downloads]
            print(f"  Success: {len(successful_downloads)}, Failures: {len(download_results) - len(successful_downloads)}")
            print(f"  Total time: {sum(download_times):.2f}s")
            if download_times:
                print(f"  Avg time: {sum(download_times)/len(download_times):.2f}s")

    if processing_results:
        print(f"\nProcessing Phase: {len(processing_results)} services")
        if successful_processing:
            parse_times = [r["parse_duration"] for r in successful_processing]
            extract_times = [r["extract_duration"] for r in successful_processing]
            processing_times = [r["parse_duration"] + r["extract_duration"] for r in successful_processing]
            total_processing_time = sum(processing_times)
            
            print(f"  Success: {len(successful_processing)}, Failures: {len(processing_results) - len(successful_processing)}")
            if successful_processing:
                print(f"  Total processing time: {total_processing_time:.2f}s")
                print(f"  Avg processing time per service: {total_processing_time / len(successful_processing):.2f}s")
                avg_parse_time = sum(parse_times) / len(parse_times)
                avg_extract_time = sum(extract_times) / len(extract_times)
                print(f"  Total parse time: {sum(parse_times):.2f}s (Avg: {avg_parse_time:.2f}s)")
                print(f"  Total extract time: {sum(extract_times):.2f}s (Avg: {avg_extract_time:.2f}s)")

    print("-------------------------")
