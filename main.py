from git import Repo, InvalidGitRepositoryError
from repo_inspector.cli import run_cli
from repo_inspector.repository import get_commits
import repo_inspector.analysis as analysis
import repo_inspector.plot as plot
import repo_inspector.utils as utils

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

    commits = get_commits(repo, args.since, args.until, args.authors)

    if (args.plot):
        if (args.metric == "commits"):
            dates, count = analysis.commits_per_day(commits)
            plot.plot_commit_timeline(dates, count, args.save)
        elif (args.metric == "lines"):
            dates, insertions, deletions, total_lines = analysis.lines_per_day(commits)
            plot.plot_lines_timeline(dates, insertions, deletions, total_lines, args.save)
        elif (args.metric == "authors"):
            author_stats = analysis.lines_per_author(commits)
            plot.plot_author_pie(author_stats, args.save)

if __name__ == "__main__":
    main()