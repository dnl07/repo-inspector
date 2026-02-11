from git import Repo, InvalidGitRepositoryError
import matplotlib.pyplot as plt
from pathlib import Path
from repo_inspector.cli import run_cli
from repo_inspector.repository import get_commits
import repo_inspector.utils as utils
from repo_inspector.analysis import ANALYZERS
from repo_inspector.plot import PLOTTERS, PLOT_OPTIONS

def main() -> None:
    args = run_cli()

    if not args.repo.exists():
        raise FileNotFoundError(f"The path {args.repo} does not exist")

    try:
        repo = Repo(args.repo)
    except InvalidGitRepositoryError:
        raise ValueError(f"{args.repo} is not a valid Git repository")

    # check if given date is valid
    utils.check_datetime(args.since)
    utils.check_datetime(args.until)

    if args.branches == "all":
        branches = [b.name for b in repo.branches]
    elif args.branches:
        branches = args.branches.replace(" ", "").split(",")
    else:
        branches = [repo.active_branch.name]

    commits = get_commits(repo, branches, args.since, args.until, args.authors)

    analyzer = ANALYZERS[args.metric]
    result = analyzer(commits)

    if args.plot:
        available = PLOT_OPTIONS[args.metric]

        if args.plot == "all":
            selected_plots = available
        else:
            selected_plots = args.plot.replace(" ", "").split(",")

        for p in selected_plots:
            if p not in available:
                raise ValueError(f"Plot '{p}' is not valid for metric '{args.metric}'. Valid plots: {', '.join(available)}")

            fig = PLOTTERS[args.metric][p](result)

            if args.save_dir and args.ext:
                output_path = Path(args.save_dir)
                output_path.mkdir(parents=True, exist_ok=True)

                filename = f"{args.metric}_{p}.{args.ext}"
                save_path = output_path / filename

                fig.savefig(save_path, bbox_inches="tight")    

        if not args.save_dir:
            plt.show()

if __name__ == "__main__":
    main()