[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/nkxJlVK3)

# Git Repository Inspector
---

## What is this project about?
---
This project provides a command-line tool to analyze a local Git repository.  It extracts information such as:

- Commit activity
- Lines added/removed
- Changed files
- Commit rhythm (weekly/hourly patterns)
- Message statistics

You can generate plots (bar charts, heatmaps, timelines, etc.) to visualize the extracted metrics.

## Installation
---
### Without docker

- Requirements:

  - Python 3.11+
  - Git installed on the system
  - pip packages (see below)

- Install dependencies:
```pip install -r requirements.txt```

- Run locally:
```python main.py --repo "path/to/repository"```

### With docker
- Build the image with the already contained dockerfile:
```docker build -t repo-inspector .```
- Run the container:
```docker run -v "path/to/repository:/repo"  -v "path/to/output:/output" repo-inspector python main.py --repo /repo --save-dir /output```
You need to mount these directories because Docker has no access to your host filesystem by default. Both paths must be passed using ```-v```.

## How to use
---

### CLI-Arguments

The tool is controlled through command-line arguments.
Below is an overview of all available options:

```--repo``` / ```-r```
Path to a valid git repository. <b>This argument is required</b>.

```--metric``` or ```-m``` 
Select the metric to analyze.
Available choices:
- ```commits```
- ```lines```
- ```authors```
- ```files```
- ```rhythm```
- ```messages```

<em>(Note: Not all metrics support all plot types.)</em>

```--since```
Start date in ```(YYYY-MM-DD)``` format

```--until```
 End date in ```(YYYY-MM-DD)``` format

```--authors``` or ```-a```:
Filter commits by author. Expects a comma-seperated list.

```--branches``` or ```-b```:
Filter commits by branch. Expects a comma-seperated list.

```--plot``` or ```-p```:
Select the plot type to generate.

Available choices:
- ```bar```
- ```pie```
- ```timeline```
- ```heatmap```
- ```weekly```
- ```hourly```
- ```all```

```--output-dir```
Directory where generated plots will be saved.

```--ext```
Output file format for saved plots.
Options: ```png```, ```svg```, ```pdf```

### Example
```bash
python main.py \
    --repo "./my-repo" \
    --metric commits \
    --plot bar \
    --output-dir "./plots" \
    --ext svg
```