import argparse
from pathlib import Path

def run_cli() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Analyze a local git repository and generate metrics or plots"
    )
    # List available metrics and plots
    parser.add_argument(
        "--list",
        action="store_true",
        help="List all available metric and plot combinations"
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
        choices=["all", "commits", "lines", "authors", "files", "rhythm", "messages"],
        default="all",
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
        action="store_true",
        help="Generate plots for the selected metric"
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
    
    args = parser.parse_args()
    
    # Validate that --repo is provided when not listing
    if not args.list and not args.repo:
        parser.error("the following arguments are required: -r/--repo (or use --list to see available options)")
    
    return args


def print_available_plots():
    pass