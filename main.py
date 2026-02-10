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

    if args.branches == "all":
        branches = [b.name for b in repo.branches]
    elif args.branches:
        branches = args.branches.replace(" ", "").split(",")
    else:
        branches = [repo.active_branch.name]

    commits = get_commits(repo, branches, args.since, args.until, args.authors)

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
            plot.plot_author_bar(author_stats, args.save)
        elif (args.metric == "files"):
            author_stats = analysis.changes_per_files(commits)
            plot.plot_files_lines_bar(author_stats, args.save)
            plot.plot_files_changes_bar(author_stats, args.save)
        elif (args.metric == "rhythm"):
            weekdays = analysis.commits_per_weekday(commits)
            hours = analysis.commits_per_hour(commits)
            heat_matrix = analysis.commits_heatmap(commits)
            plot.plot_weekday_rhythm(weekdays, args.save)
            plot.plot_hours_rhythm(hours, args.save)
            plot.plot_heatmap_rhythm(heat_matrix, args.save)
if __name__ == "__main__":
    main()