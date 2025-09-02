"""Unit tests for the test helper modules."""
import pytest
from unittest.mock import patch

from ..helpers import TestReport
from mapigen.client.exceptions import MapiError

# As TestReport is a singleton, we use a fixture to reset its state for each test,
# ensuring test isolation.
@pytest.fixture
def report_instance() -> TestReport:
    """Returns a clean TestReport instance for each test."""
    # Create a new instance for testing purposes to avoid polluting the global one
    report = TestReport()
    report.results.clear()
    return report


def test_add_expected_client_error(report_instance: TestReport):
    """
    Tests that add_expected_client_error correctly adds a result
    to the 'expected_client_errors' category. This test will fail until
    the method and required dictionary are implemented.
    """
    service = "test_service"
    op_name = "test_op"
    error = MapiError(
        "Client Error",
        service=service,
        operation=op_name,
        error_type="client"
    )
    error.http_status = 404

    # This method doesn't exist yet, which is the point of TDD.
    report_instance.add_expected_client_error(service, op_name, error)

    assert service in report_instance.results
    assert "expected_client_errors" in report_instance.results[service]
    assert len(report_instance.results[service]["expected_client_errors"]) == 1

    entry = report_instance.results[service]["expected_client_errors"][0]
    assert entry["operation"] == op_name
    assert entry["status"] == 404
    assert "Not Found" in entry["details"]
    assert str(error) in entry["message"]


@patch("builtins.open")
@patch("yaml.dump")
def test_save_report_includes_expected_client_errors(mock_yaml_dump, mock_open, report_instance: TestReport):
    """
    Tests that the save method correctly includes the 'expected_client_errors'
    category in the final YAML output.
    """
    service = "service_alpha"
    op_name = "op_bravo"
    error = MapiError("Forbidden", service=service, operation=op_name)
    error.http_status = 403

    report_instance.add_expected_client_error(service, op_name, error)
    report_instance.save()

    # Verify that yaml.dump was called and grab the data it was called with
    assert mock_yaml_dump.called
    args, _ = mock_yaml_dump.call_args
    final_yaml_data = args[0]

    # Check the structure of the dumped data
    assert "tests" in final_yaml_data
    assert service in final_yaml_data["tests"]
    assert "expected_client_errors" in final_yaml_data["tests"][service]
    
    entry = final_yaml_data["tests"][service]["expected_client_errors"][0]
    assert entry["operation"] == op_name
    assert entry["status"] == 403
