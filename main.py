from gitinspector.cli import run_cli
from gitinspector.analyzer import analyze_repository
import gitinspector.utils as utils
import gitinspector.plotting as plot
from git import Repo, InvalidGitRepositoryError

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

    analyzed = analyze_repository(repo, args.metric, args.since, args.until, args.authors)

    if (args.plot):
        if (args.metric == "commits"):
            plot.plot_commit_timeline(analyzed, args.save)
        if (args.metric == "lines"):
            plot.plot_lines_timeline(analyzed, args.save)

if __name__ == "__main__":
    main()