import os
import requests
from datetime import datetime, timedelta

import google.generativeai as genai

def summarize_sentence(sentence):
    """
    Summarize a given sentence using Google Gemini API in 50 words.
    
    Args:
        sentence (str): Input sentence to summarize
        api_key (str): Google Gemini API key
    
    Returns:
        str: 100-word summary of the input sentence
    """
    genai.configure(api_key=os.environ.get('GOOGLE_API_KEY'))
    print(os.environ.get('GOOGLE_API_KEY'))
    
    model = genai.GenerativeModel('gemini-pro')
    
    prompt = f"""You are a GitHub event summarizer. For the comment from @Vidit-Ostwal:

            Guidelines for summarization:
            - Summarize the entire comment in exactly 100 words. Make sure you summarize all important information
            - Ignore any @mentions or tagged users in the comment
            - Provide the summary from the perspective of "@Vidit-Ostwal has suggested"
            - If the comment contains code examples, extract the key message while disregarding specific code details
            - Do not refer to any other external link in the summary
            - Your output should be exactly 100 words and should have all the relevant information
            - Failure to follow any of these rules, will lead to your permanent termination

            Comment to summarize: {sentence}"""
    try:
        response = model.generate_content(prompt)
        summary = response.text.strip()
        
        # Ensure summary is close to 50 words
        words = summary.split()
        if len(words) > 50:
            summary = ' '.join(words[:50])
        
        return summary
    
    except Exception as e:
        return f"Error summarizing: {str(e)}"

def get_github_activity(username, token):
    """
    Fetch recent GitHub activities for a user.
    
    Args:
        username (str): GitHub username
        token (str): GitHub Personal Access Token
    
    Returns:
        dict: Consolidated GitHub activity summary, including comments, issues, pull requests,
              starred repositories, and forks.
    """
    # GitHub API base URL
    base_url = "https://api.github.com"
    
    # Headers for authentication and API version
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    # Initialize the activity summary
    activities = {
        "recent_comments": [],
        "issues_raised": [],
        "pull_requests": [],
        "starred_repos": [],
        "forked_repos": []
    }
    
    # GitHub Events API (supports user events)
    events_url = f"{base_url}/users/{username}/events"
    
    # Fetch events with pagination (in case of more than 30 results)
    page = 1
    cutoff_date = datetime.now() - timedelta(days=30)
    
    while True:
        response = requests.get(f"{events_url}?page={page}", headers=headers)
        if response.status_code != 200:
            print(f"Failed to fetch events: {response.status_code} - {response.json().get('message', 'Unknown error')}")
            break
        
        events = response.json()
        if not events:
            break  # No more events to process
        
        for event in events:
            try:
                event_date = datetime.strptime(event['created_at'], "%Y-%m-%dT%H:%M:%SZ")
                if event_date < cutoff_date:
                    break  # Stop if the event is older than 30 days
                
                # Collect comments
                # Fetch full comment details for IssueCommentEvent
                if event['type'] == 'IssueCommentEvent':
                    comment_url = event['payload']['comment']['url']
                    comment_response = requests.get(comment_url, headers=headers)
                    
                    if comment_response.status_code == 200:
                        comment_details = comment_response.json()
                        activities['recent_comments'].append({
                            'repo': event['repo']['name'],
                            'comment_url': comment_details['html_url'],
                            'comment_text': comment_details['body'],
                            'date': event_date.strftime("%Y-%m-%d")
                        })
                
                # Collect issues raised
                elif event['type'] == 'IssuesEvent' and event['payload']['action'] == 'opened':
                    activities['issues_raised'].append({
                        'repo': event['repo']['name'],
                        'issue_title': event['payload']['issue']['title'],
                        'issue_url': event['payload']['issue']['html_url'],
                        'date': event_date.strftime("%Y-%m-%d")
                    })
                
                # Collect pull requests
                elif event['type'] == 'PullRequestEvent' and event['payload']['action'] == 'opened':
                    activities['pull_requests'].append({
                        'repo': event['repo']['name'],
                        'pr_title': event['payload']['pull_request']['title'],
                        'pr_url': event['payload']['pull_request']['html_url'],
                        'date': event_date.strftime("%Y-%m-%d")
                    })
                
                # Collect starred repositories
                elif event['type'] == 'WatchEvent' and event['payload']['action'] == 'started':
                    activities['starred_repos'].append({
                        'repo': event['repo']['name'],
                        'date': event_date.strftime("%Y-%m-%d")
                    })
                
                # Collect forked repositories
                elif event['type'] == 'ForkEvent':
                    activities['forked_repos'].append({
                        'repo': event['repo']['name'],
                        'fork_url': event['payload']['forkee']['html_url'],
                        'date': event_date.strftime("%Y-%m-%d")
                    })
            
            except KeyError as e:
                print(f"Missing key in event: {e}")
        
        # Go to the next page
        page += 1
    
    return activities

def generate_markdown(username, activities):
    """
    Generate a markdown summary of GitHub activities.
    
    Args:
        username (str): GitHub username
        activities (dict): GitHub activity summary
    
    Returns:
        str: Markdown formatted activity summary
    """
    markdown = f"# Recent GitHub Activity for {username}\n\n"
    
    # Recent Comments Section
    markdown += "## 💬 Recent Comments\n"
    if activities['recent_comments']:
        for comment in activities['recent_comments'][:5]:  # Limit to 5 comments
            markdown += f"- Commented in [{comment['repo']}]({comment['comment_url']}) on {comment['date']}.\n"
            markdown += f"  > *AI Summary: {summarize_sentence(comment['comment_text'])}*\n"
    else:
        markdown += "No recent comments.\n"
    
    # Issues Raised Section
    markdown += "\n## 🐛 Issues Raised\n"
    if activities['issues_raised']:
        for issue in activities['issues_raised'][:5]:  # Limit to 5 issues
            markdown += f"- Raised an issue in [{issue['repo']}]({issue['issue_url']}): {issue['issue_title']} ({issue['date']}).\n"
    else:
        markdown += "No issues raised recently.\n"
    
    # Pull Requests Section
    markdown += "\n## 🚀 Pull Requests\n"
    if activities['pull_requests']:
        for pr in activities['pull_requests'][:5]:  # Limit to 5 PRs
            markdown += f"- Opened a PR in [{pr['repo']}]({pr['pr_url']}): {pr['pr_title']} ({pr['date']}).\n"
    else:
        markdown += "No pull requests opened recently.\n"
    
    # Starred Repositories Section
    markdown += "\n## ⭐ Starred Repositories\n"
    if activities['starred_repos']:
        for star in activities['starred_repos'][:5]:  # Limit to 5 starred repos
            markdown += f"- Starred [{star['repo']}] on {star['date']}.\n"
    else:
        markdown += "No repositories starred recently.\n"
    
    # Forked Repositories Section
    markdown += "\n## 🍴 Forked Repositories\n"
    if activities['forked_repos']:
        for fork in activities['forked_repos'][:5]:  # Limit to 5 forks
            markdown += f"- Forked [{fork['repo']}]({fork['fork_url']}) on {fork['date']}.\n"
    else:
        markdown += "No repositories forked recently.\n"
    
    return markdown


def main():
    # Get GitHub username and personal access token from environment variables
    username = os.environ.get('GITHUB_USERNAME')
    token = os.environ.get('GITHUB_TOKEN')
    print(username, token)
    
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
