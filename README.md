# jira-issue-reader



# Jira Issue Exporter

Read Jira issues and export them to files eg. to use for AI learn data.
This script fetches issues from a Jira Server instance using the Jira REST API and exports each issue to its own text file.

## Prerequisites

- Python 3.x
- `requests` library (install with `pip install requests`)

## Configuration

Before running the script, you need to configure a few things:

1. Set the `JIRA_URL` variable to point to your Jira Server instance.
2. Adjust the `JQL_FILTER` variable to match the filter criteria you want (e.g., specific project and status).

## Usage

1. Clone this repository:
   git clone https://github.com/your-username/jira-issue-exporter.git

