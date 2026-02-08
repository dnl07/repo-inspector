import argparse
from pathlib import Path

def run_cli() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Analyze a local git repository and generate metrics or plots"
    )
    # Repository path
    parser.add_argument(
        "-r", "--repo",
        type=Path,
        help="Path to a repository"
    )
    # Which metric to compute
    parser.add_argument(
        "-m", "--metric",
        choices=["commits", "lines", "authors", "files"],
        default="commits",
        help="Metric to analyze"
    )
    # Date ranges
    parser.add_argument(
        "--since",
        type=str,
        help="Start date (YYYY-MM_DD)"
    )
    parser.add_argument(
        "--until",
        type=str,
        help="End date (YYYY-MM_DD)"
    )
    # Filter by authors
    parser.add_argument(
        "-a", "--author",
        type=str,
        help="Comma-separated list of authors"
    )
    # Plotting output
    parser.add_argument(
        "-p", "--plot",
        action="store_true",
        help="Generate aa plot of the selected metric"
    )
    # Save output to a file
    parser.add_argument(
        "--save",
        type=Path,
        help="Saave plot or metrics to a file (e.g., output.png or data.json)"
    )

    return parser.parse_args()