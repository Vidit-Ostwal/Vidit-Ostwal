import os
import requests
from datetime import datetime, timedelta

def get_github_activity(username, token):
    """
    Fetch recent GitHub activities for a user
    
    Args:
        username (str): GitHub username
        token (str): GitHub Personal Access Token
    
    Returns:
        dict: Consolidated GitHub activity summary
    """
    # GitHub API base URL
    base_url = "https://api.github.com"
    
    # Headers for authentication and API version
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    # Retrieve recent activities
    activities = {
        "recent_comments": [],
        "issues_raised": [],
        "pull_requests": []
    }
    
    # Fetch recent comments across repositories
    comments_url = f"{base_url}/users/{username}/events"
    comments_response = requests.get(comments_url, headers=headers)
    
    if comments_response.status_code == 200:
        events = comments_response.json()
        
        # Filter and process events in the last 30 days
        cutoff_date = datetime.now() - timedelta(days=30)
        
        for event in events:
            event_date = datetime.strptime(event['created_at'], "%Y-%m-%dT%H:%M:%SZ")
            
            if event_date < cutoff_date:
                break
            
            # Collect comments
            if event['type'] == 'CommentEvent':
                activities['recent_comments'].append({
                    'repo': event['repo']['name'],
                    'comment_url': event.get('payload', {}).get('comment', {}).get('html_url', ''),
                    'date': event_date.strftime("%Y-%m-%d")
                })
            
            # Collect issues
            if event['type'] == 'IssuesEvent' and event['payload']['action'] == 'opened':
                activities['issues_raised'].append({
                    'repo': event['repo']['name'],
                    'issue_title': event['payload']['issue']['title'],
                    'issue_url': event['payload']['issue']['html_url'],
                    'date': event_date.strftime("%Y-%m-%d")
                })
            
            # Collect pull requests
            if event['type'] == 'PullRequestEvent' and event['payload']['action'] == 'opened':
                activities['pull_requests'].append({
                    'repo': event['repo']['name'],
                    'pr_title': event['payload']['pull_request']['title'],
                    'pr_url': event['payload']['pull_request']['html_url'],
                    'date': event_date.strftime("%Y-%m-%d")
                })
    
    return activities

def generate_markdown(username, activities):
    """
    Generate a markdown summary of GitHub activities
    
    Args:
        username (str): GitHub username
        activities (dict): GitHub activity summary
    
    Returns:
        str: Markdown formatted activity summary
    """
    markdown = f"## Recent GitHub Activity for {username}\n\n"
    
    # Recent Comments Section
    markdown += "### 💬 Recent Comments\n"
    if activities['recent_comments']:
        for comment in activities['recent_comments'][:5]:  # Limit to 5 comments
            markdown += f"- In [{comment['repo']}]({comment['comment_url']}), commented on {comment['date']}\n"
    else:
        markdown += "No recent comments.\n"
    
    # Issues Raised Section
    markdown += "\n### 🐛 Issues Raised\n"
    if activities['issues_raised']:
        for issue in activities['issues_raised'][:5]:  # Limit to 5 issues
            markdown += f"- In [{issue['repo']}]({issue['issue_url']}): {issue['issue_title']} ({issue['date']})\n"
    else:
        markdown += "No issues raised recently.\n"
    
    # Pull Requests Section
    markdown += "\n### 🚀 Pull Requests\n"
    if activities['pull_requests']:
        for pr in activities['pull_requests'][:5]:  # Limit to 5 PRs
            markdown += f"- In [{pr['repo']}]({pr['pr_url']}): {pr['pr_title']} ({pr['date']})\n"
    else:
        markdown += "No pull requests opened recently.\n"
    
    return markdown

def main():
    # Get GitHub username and personal access token from environment variables
    username = os.environ.get('GITHUB_USERNAME')
    token = os.environ.get('GITHUB_TOKEN')
    
    if not username or not token:
        print("Please set GITHUB_USERNAME and GITHUB_TOKEN environment variables.")
        return
    
    # Fetch and generate activities
    activities = get_github_activity(username, token)
    markdown_content = generate_markdown(username, activities)
    
    # Optional: Write to README.md
    with open('README.md', 'w') as f:
        f.write(markdown_content)
    
    print("GitHub activity summary generated successfully!")

if __name__ == "__main__":
    main()
