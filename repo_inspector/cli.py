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
        type=str,
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
    return args

# Display some examples
def print_examples():    
    print("\n" + "="*25)
    print("USAGE")
    print("="*25 + "\n")

    print(f"Plot all metrics with: python main.py -r <repo> -m all -p\n")
    
    print("="*70)
    print("Example metrics:")
    print("  python main.py -r . -m commits -p")
    print("  python main.py -r . -m authors -p")
    print("  python main.py -r . -m lines -p")
    print("="*70 + "\n")
    print("Save the plots with:")
    print("  python main.py -r . -m commits -p --output-dir 'output/' --ext png\n")