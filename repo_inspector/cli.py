import argparse
from pathlib import Path

def run_cli() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Analyze a local git repository and generate metrics or plots"
    )
    # Repository path
    parser.add_argument(
        "-r", "--repo",
        required=True,
        type=Path,
        help="Path to a repository"
    )
    # Which metric to compute
    parser.add_argument(
        "-m", "--metric",
        choices=["commits", "lines", "authors", "files", "rhythm", "messages"],
        default="commits",
        help="Metric to analyze"
    )
    # Date ranges
    parser.add_argument(
        "--since",
        type=str,
        help="Start date (YYYY-MM-DD)"
    )
    parser.add_argument(
        "--until",
        type=str,
        help="End date (YYYY-MM-DD)"
    )
    # Filter by authors
    parser.add_argument(
        "-a", "--authors",
        type=str,
        help="Comma-separated list of authors"
    )
    # Filter by branches
    parser.add_argument(
        "-b", "--branches",
        type=str,
        help="Comma-separated list of branches to analyze, or 'all' for all branches"
    )
    # Plotting output
    parser.add_argument(
        "-p", "--plot",
        type=str,
        default=None,
        help="Which plot to generate (bar, pie, timeline, heatmap, weekly, hourly, all)"
    )
    # Save output in a directory
    parser.add_argument(
        "--output-dir",
        type=Path,
        help="Directory to save generated plots"
    )
    # Output extension
    parser.add_argument(
        "--ext",
        type=str,
        default="png",
        choices=["png", "svg", "pdf"],
        help="Output file format for saved plots"
    )
    return parser.parse_args()