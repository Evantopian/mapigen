import pytest
import sys

if __name__ == "__main__":
    # This script is an entrypoint for the profiler.
    # It simply passes all command-line arguments it receives to pytest.
    sys.exit(pytest.main(sys.argv[1:]))