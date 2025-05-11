import os
import requests
from datetime import datetime, timedelta
from litellm import completion

def summarize_sentence(sentence):
    """
    Summarize a given sentence using Google Gemini API in 50 words.
    
    Args:
        sentence (str): Input sentence to summarize
        api_key (str): Google Gemini API key
    
    Returns:
        str: 100-word summary of the input sentence
    """

    prompt = f"""You are a GitHub event summarizer. For the comment from @Vidit-Ostwal:

            Guidelines for summarization:
            - Summarize the entire comment in exactly 100 words. Make sure you summarize all important information
            - Ignore any @mentions or tagged users in the comment
            - Provide the summary from the perspective of "@Vidit-Ostwal has suggested"
            - If the comment contains code examples, extract the key message while disregarding specific code details
            - Do not refer to any other external link in the summary
            - Do not write any code in the summary
            - Your output should be exactly 75 words and should have all the relevant information
            - Failure to follow any of these rules, will lead to your permanent termination

            Comment to summarize: {sentence}"""
    try:
        response = completion(
            model = "openrouter/openai/gpt-4o-mini", 
            messages=[{ "content": prompt,"role": "user"}],
            api_key = os.environ.get('OPENROUTER_API_KEY'),
        )
        
        return response.choices[0].message.content
    
    except Exception as e:
        return f"Error summarizing: {str(e)}"


def get_github_activity(username, token):
    base_url = "https://api.github.com"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    activities = {
        "recent_comments": [],
        "issues_raised": [],
        "pull_requests": [],
        "starred_repos": [],
        "forked_repos": []
    }

    events_url = f"{base_url}/users/{username}/events"
    cutoff_date = datetime.utcnow() - timedelta(days=7)
    page = 1
    max_pages = 10  # GitHub caps this to 10 pages

    while page <= max_pages:
        response = requests.get(f"{events_url}?page={page}", headers=headers)
        if response.status_code != 200:
            print(f"Failed to fetch events: {response.status_code} - {response.json().get('message', 'Unknown error')}")
            break

        events = response.json()
        if not events:
            break

        for event in events:
            try:
                event_date = datetime.strptime(event['created_at'], "%Y-%m-%dT%H:%M:%SZ")
                if event_date < cutoff_date:
                    return activities  # Stop processing older events

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

                elif event['type'] == 'IssuesEvent' and event['payload']['action'] == 'opened':
                    activities['issues_raised'].append({
                        'repo': event['repo']['name'],
                        'issue_title': event['payload']['issue']['title'],
                        'issue_description': event['payload']['issue']['body'],
                        'issue_url': event['payload']['issue']['html_url'],
                        'date': event_date.strftime("%Y-%m-%d")
                    })

                elif event['type'] == 'PullRequestEvent' and event['payload']['action'] == 'opened':
                    activities['pull_requests'].append({
                        'repo': event['repo']['name'],
                        'pr_title': event['payload']['pull_request']['title'],
                        'pr_description': event['payload']['pull_request']['body'],
                        'pr_url': event['payload']['pull_request']['html_url'],
                        'date': event_date.strftime("%Y-%m-%d")
                    })

                elif event['type'] == 'WatchEvent' and event['payload']['action'] == 'started':
                    activities['starred_repos'].append({
                        'repo': event['repo']['name'],
                        'repo_link': f"https://github.com/{event['repo']['name']}",
                        'date': event_date.strftime("%Y-%m-%d")
                    })

                elif event['type'] == 'ForkEvent':
                    activities['forked_repos'].append({
                        'repo': event['repo']['name'],
                        'fork_url': event['payload']['forkee']['html_url'],
                        'date': event_date.strftime("%Y-%m-%d")
                    })

            except KeyError as e:
                print(f"Missing key in event: {e}")

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
        for comment in activities['recent_comments'][:5]:  # Limit to 10 comments
            markdown += f"- [Commented]({comment['comment_url']}) in [{comment['repo']}] on {comment['date']}.\n"
            markdown += f"  > *AI Summary: {summarize_sentence(comment['comment_text'])}*\n"
    else:
        markdown += "No recent comments.\n"
    
    # Issues Raised Section
    markdown += "\n## 🐛 Issues Raised\n"
    if activities['issues_raised']:
        for issue in activities['issues_raised'][:5]:  # Limit to 5 issues
            markdown += f"- Raised an [issue]({issue['issue_url']}) in [{issue['repo']}]: {issue['issue_title']} ({issue['date']}).\n"
            markdown += f"  > *AI Summary: {summarize_sentence(issue['issue_description'])}*\n"
    else:
        markdown += "No issues raised recently.\n"
    
    # Pull Requests Section
    markdown += "\n## 🚀 Pull Requests\n"
    if activities['pull_requests']:
        for pr in activities['pull_requests'][:5]:  # Limit to 5 PRs
            markdown += f"- Opened a [PR]({pr['pr_url']}) in [{pr['repo']}]: {pr['pr_title']} ({pr['date']}).\n"
            markdown += f"  > *AI Summary: {summarize_sentence(pr['pr_description'])}*\n"
    else:
        markdown += "No pull requests opened recently.\n"
    
    # Starred Repositories Section
    markdown += "\n## ⭐ Starred Repositories\n"
    if activities['starred_repos']:
        for star in activities['starred_repos'][:5]:  # Limit to 5 starred repos
            markdown += f"- Starred [{star['repo']}]({star['repo_link']}) on {star['date']}.\n"
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
    
    if not username or not token:
        print("Please set GITHUB_USERNAME and GITHUB_TOKEN environment variables.")
        return
    
    # Fetch and generate activities
    activities = get_github_activity(username, token)
    print("Fetched GitHub activities successfully!")

    markdown_content = generate_markdown(username, activities)
    print("Generated markdown content successfully!")
    print(markdown_content)
    
    # Optional: Write to README.md
    with open('README.md', 'w') as f:
        f.write(markdown_content)
    
    print("GitHub activity summary generated successfully!")

if __name__ == "__main__":
    main()
