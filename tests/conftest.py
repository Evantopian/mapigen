from .reporting import report

def pytest_sessionfinish(session):
    """Pytest hook that runs after the entire test session finishes."""
    report.save()
