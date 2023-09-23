import requests
import os
import string

# Jira configuration
JIRA_URL = "https://jira.atlassian.com/"
JQL_FILTER = "project = 10240 AND issuetype = 1 ORDER BY key DESC"  # Replace with your JQL filter

def get_jira_issues(jira_url, jql_filter):
    headers = {
        "Accept": "application/json"
    }
    
    params = {
        "jql": jql_filter,
        "fields": "key,summary,description",  # You can modify this to fetch other fields
    }
    
    response = requests.get(f"{jira_url}/rest/api/2/search", headers=headers, params=params)
    
    if response.status_code != 200:
        raise Exception(f"Failed to fetch Jira issues. Status code: {response.status_code}, Response: {response.text}")
    
    data = response.json()
    return data["issues"]

def save_issue_to_file(issue):
    # Create a filename using the issue key and summary
    filename = f"{issue['key']} - {issue['fields']['summary']}.txt"
    # filename = os.path.join(output_dir, filename)

    # Ensure the filename is valid (remove or replace invalid characters)
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    filename = ''.join(c for c in filename if c in valid_chars)

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(f"Issue Key: {issue['key']}\n")
        file.write(f"Summary: {issue['fields']['summary']}\n")
        file.write(f"Description:\n{issue['fields']['description']}\n")

if __name__ == "__main__":
    issues = get_jira_issues(JIRA_URL, JQL_FILTER)
    for issue in issues:
        save_issue_to_file(issue)

