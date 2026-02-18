from git import Repo, InvalidGitRepositoryError
import matplotlib.pyplot as plt
from pathlib import Path
from repo_inspector.cli import run_cli, print_examples
from repo_inspector.repository import get_commits
import repo_inspector.utils as utils
from repo_inspector.analysis import ANALYZERS
from repo_inspector.plot import PLOTTERS
import sys
import repo_inspector.print as printer

def main() -> None:
    args = run_cli()

    # Validate that --repo is provided when not listing
    if not args.list and not args.repo:
        printer.error("The following arguments are required: -r/--repo (or use --list to see available options)")
        sys.exit(1)
    
    # If --list flag is provided, display available options and exit
    if args.list:
        print_examples()
        return

    printer.info(f"Analyzing Repository: {args.repo}")

    if not args.repo.exists():
        printer.error("The specified repository path does not exist.")
        sys.exit(1)

    try:
        repo = Repo(args.repo)
        printer.info(f"Repository successfully loaded: {repo.working_tree_dir}")
    except InvalidGitRepositoryError:
        printer.error(f"The path {args.repo} is not a valid Git repository.")
        sys.exit(1)

    # check if given date is valid
    utils.check_datetime(args.since)
    utils.check_datetime(args.until)

    # branches
    if args.branches == "all":
        branches = [b.name for b in repo.branches]
        printer.info(f"Analyzing all branches: {', '.join(branches)}")
    elif args.branches:
        branches = args.branches.replace(" ", "").split(",")
        printer.info(f"Analyzing branches: {', '.join(branches)}")
    else:
        branches = [repo.active_branch.name]
        printer.info(f"Analyzing current branch: {branches[0]}")

    # commits
    printer.info("Loading commits...")
    branch_commits = get_commits(repo, branches, args.since, args.until, args.authors)

    for entry in branch_commits:
        branch = entry["branch"]
        commits = entry["commits"]

        printer.success(f"Found {len(commits)} commits in branch '{branch}'")

        # Analyze metric
        printer.info(f"Computing metric '{args.metric}'...")
        analyzer = ANALYZERS[args.metric]
        result = analyzer(commits)
        printer.success("Analysis complete")

        # Generate all plots for the metric
        if args.plot:
            printer.info(f"Generating plot for metric '{args.metric}'...")
            figs = PLOTTERS[args.metric](result)

            if not isinstance(figs, list):
                figs = [figs]

            for (label, fig) in figs:
                if args.output_dir and args.ext:
                    output_path = Path(args.output_dir)
                    output_path.mkdir(parents=True, exist_ok=True)

                    filename = f"{label}_{branch}.{args.ext}"
                    save_path = output_path / filename

                    fig.savefig(save_path, bbox_inches="tight")
                    printer.success(f"Plot saved: {save_path}")
                    plt.close(fig)
                else:
                    printer.info("Displaying plots...")
                    plt.show()
                    plt.close(fig)

if __name__ == "__main__":
    main()