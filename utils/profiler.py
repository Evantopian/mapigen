import argparse
import pstats
import subprocess
import sys
import tempfile
from pathlib import Path
import os


def main():
    """Runs a script under cProfile as a subprocess and prints a filtered report."""
    parser = argparse.ArgumentParser(
        description="Profile a Python script with filtered output.",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        "--filter",
        default="",
        help="Filter results to only show items containing this string. Default: show all.",
    )
    parser.add_argument(
        "--sort",
        default="cumtime",
        choices=None,  # Let pstats handle validation
        help="The statistic to sort by. Default: 'cumtime'",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=25,
        help="Limit the output to the top N results. Default: 25",
    )

    args, script_args = parser.parse_known_args()

    if not script_args:
        print("Error: No script path provided to profile.")
        sys.exit(1)

    script_path = Path(script_args[0])
    if not script_path.exists():
        print(f"Error: Script not found at '{script_path}'")
        sys.exit(1)

    with tempfile.NamedTemporaryFile(suffix=".prof") as tmp_prof_file:
        profile_output_path = tmp_prof_file.name

        command = [
            sys.executable,
            "-m",
            "cProfile",
            "-o",
            profile_output_path,
        ] + script_args

        print("--- Profiling Command ---")
        print(" ".join(command))
        print()

        env = os.environ.copy()
        result = subprocess.run(command, capture_output=True, text=True, env=env)

        if result.stdout:
            print("--- Profiled Script STDOUT ---")
            print(result.stdout)
        if result.stderr:
            print("--- Profiled Script STDERR ---")
            print(result.stderr)

        if result.returncode != 0:
            print(f"\nProfiling failed: Script exited with code {result.returncode}")
            sys.exit(result.returncode)

        stats = pstats.Stats(profile_output_path)

    stats.strip_dirs().sort_stats(args.sort)

    # --- Manually print formatted output for full control ---
    print(
        f"\n--- Top {args.limit} results sorted by {args.sort} (filtered by '{args.filter or 'all'}') ---"
    )

    header = f"{'Function':<80} {'Calls':>10} {'Total Time (ms)':>18} {'Cumulative Time (ms)':>24}"
    print(header)
    print("-" * len(header))

    count = 0
    for func, (cc, nc, tt, ct, callers) in stats.stats.items():  # type: ignore
        if count >= args.limit:
            break

        file, line, name = func

        # Apply filter to both file and function name
        filter_str = args.filter.lower()
        if filter_str and not (filter_str in file.lower() or filter_str in name.lower()):
            continue

        if file == '~':
            func_display = name  # For built-in functions
        else:
            func_display = f"{Path(file).name}:{line} ({name})"

        row = (
            f"{func_display:<80} "
            f"{nc:>10} "
            f"{tt * 1000:>18.3f} "
            f"{ct * 1000:>24.3f}"
        )
        print(row)
        count += 1



if __name__ == "__main__":
    main()
