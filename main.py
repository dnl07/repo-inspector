from git import Repo, InvalidGitRepositoryError
from repo_inspector.cli import run_cli
from repo_inspector.repository import get_commits
import repo_inspector.utils as utils
from repo_inspector.analysis import ANALYZERS
from repo_inspector.plot import PLOTTERS
import matplotlib.pyplot as plt
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
        plotter = PLOTTERS[args.metric]
        figs = plotter(result)

    

    plt.show()

if __name__ == "__main__":
    main()