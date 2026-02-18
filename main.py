from git import Repo, InvalidGitRepositoryError
import matplotlib.pyplot as plt
from pathlib import Path
from repo_inspector.cli import run_cli, print_available_plots
from repo_inspector.repository import get_commits
import repo_inspector.utils as utils
from repo_inspector.analysis import ANALYZERS
from repo_inspector.plot import PLOTTERS

def main() -> None:
    args = run_cli()

    # If --list flag is provided, display available options and exit
    if args.list:
        print_available_plots()
        return

    print(f"[INFO] Analyzing Repository: {args.repo}")

    if not args.repo.exists():
        raise FileNotFoundError(f"The path {args.repo} does not exist")

    try:
        repo = Repo(args.repo)
        print(f"[INFO] Repository successfully loaded: {repo.working_tree_dir}")
    except InvalidGitRepositoryError:
        raise ValueError(f"{args.repo} is not a valid Git repository")

    # check if given date is valid
    utils.check_datetime(args.since)
    utils.check_datetime(args.until)

    if args.branches == "all":
        branches = [b.name for b in repo.branches]
        print(f"[INFO] Analyzing all branches: {', '.join(branches)}")
    elif args.branches:
        branches = args.branches.replace(" ", "").split(",")
        print(f"[INFO] Analyzing branches: {', '.join(branches)}")
    else:
        branches = [repo.active_branch.name]
        print(f"[INFO] Analyzing current branch: {branches[0]}")

    print("[INFO] Loading commits...")
    commits = get_commits(repo, branches, args.since, args.until, args.authors)
    print(f"[INFO] Found {len(commits)} commits")

    # Analyze metric
    print(f"[INFO] Computing metric '{args.metric}'...")
    analyzer = ANALYZERS[args.metric]
    result = analyzer(commits)
    print("[INFO] Analysis complete")

    # Generate all plots for the metric
    if args.plot:
        print(f"[INFO] Generating plot for metric '{args.metric}'...")
        figs = PLOTTERS[args.metric](result)

        for i, (label, fig) in enumerate(figs):
            if args.output_dir and args.ext:
                output_path = Path(args.output_dir)
                output_path.mkdir(parents=True, exist_ok=True)

                filename = f"{label}.{args.ext}"
                save_path = output_path / filename

                fig.savefig(save_path, bbox_inches="tight")
                print(f"[INFO] Plot saved: {save_path}")
            else:
                plt.show()

if __name__ == "__main__":
    main()