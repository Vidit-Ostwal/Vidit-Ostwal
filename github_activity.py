import os
import requests
from datetime import datetime, timedelta
from litellm import completion
import json
from dotenv import load_dotenv
from helper_function import check_new_github_followers, send_email
load_dotenv()

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
        print(f"Fetching Page {page}.....")
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

                if event['type'] == 'IssueCommentEvent':
                    if len(activities['recent_comments']) == 10:
                        continue
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
                    if len(activities['issues_raised']) == 5:
                        continue
                    activities['issues_raised'].append({
                        'repo': event['repo']['name'],
                        'issue_title': event['payload']['issue']['title'],
                        'issue_description': event['payload']['issue']['body'],
                        'issue_url': event['payload']['issue']['html_url'],
                        'date': event_date.strftime("%Y-%m-%d")
                    })

                elif event['type'] == 'PullRequestEvent' and event['payload']['action'] == 'opened':
                    if len(activities['pull_requests']) == 5:
                        continue
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


def generate_blogs_markdown():
    with open('blogs.json', 'r') as f:
        blog_json = json.load(f)

    markdown = ""
    for blog in blog_json['blogs']:
        markdown += f"- [{blog['blog_name']}]({blog['blog_url']}) - *{blog['blog_posting_date']}*\n"
        for sub_blog in blog.get("sub_blogs", []):
            markdown += f"  - [{sub_blog['blog_name']}]({sub_blog['blog_url']}) - *{sub_blog['blog_posting_date']}*\n"

    substack_blogs = get_all_substack_blogs()
    print("Number of substack blogs: ", len(substack_blogs))
    for blog in substack_blogs:
        markdown += f"- [{blog['title']}]({blog['link']}) - *{blog['published']}*\n"
        markdown += f"{blog['subtitle']}\n"

    print("Generated blogs markdown successfully!")

    return markdown


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
    
    # Blog Section
    blog_markdown = open('blogs.md', 'r').read()
    markdown += blog_markdown
    markdown += "\n\n"

    # Recent Comments Section
    if len(activities['recent_comments']):
        markdown += "## 💬 Recent Comments\n"
        for comment in activities['recent_comments'][:5]:  # Limit to 10 comments
            markdown += f"- [Commented]({comment['comment_url']}) in [{comment['repo']}] on {comment['date']}.\n"
            markdown += f"  > *AI Summary: {summarize_sentence(comment['comment_text'])}*\n"
    
    # Issues Raised Section
    if len(activities['issues_raised']):
        markdown += "\n## 🐛 Issues Raised\n"
        for issue in activities['issues_raised'][:5]:  # Limit to 5 issues
            markdown += f"- Raised an [issue]({issue['issue_url']}) in [{issue['repo']}]: {issue['issue_title']} ({issue['date']}).\n"
            markdown += f"  > *AI Summary: {summarize_sentence(issue['issue_description'])}*\n"
    
    # Pull Requests Section
    if len(activities['pull_requests']):
        markdown += "\n## 🚀 Pull Requests\n"
        for pr in activities['pull_requests'][:5]:  # Limit to 5 PRs
            markdown += f"- Opened a [PR]({pr['pr_url']}) in [{pr['repo']}]: {pr['pr_title']} ({pr['date']}).\n"
            markdown += f"  > *AI Summary: {summarize_sentence(pr['pr_description'])}*\n"
    
    # Starred Repositories Section
    if len(activities['starred_repos']):
        markdown += "\n## ⭐ Starred Repositories\n"
        for star in activities['starred_repos'][:5]:  # Limit to 5 starred repos
            markdown += f"- Starred [{star['repo']}]({star['repo_link']}) on {star['date']}.\n"
    
    # Forked Repositories Section
    if len(activities['forked_repos']):
        markdown += "\n## 🍴 Forked Repositories\n"
        for fork in activities['forked_repos'][:5]:  # Limit to 5 forks
            markdown += f"- Forked [{fork['repo']}]({fork['fork_url']}) on {fork['date']}.\n"
    
    return markdown


def main():
    # Get GitHub username and personal access token from environment variables
    username = os.environ.get('GITHUB_USERNAME')
    token = os.environ.get('GITHUB_TOKEN')
    token_2 = os.environ.get('GITHUB_TOKEN_2')
    
    if not username or not token:
        print("Please set GITHUB_USERNAME and GITHUB_TOKEN environment variables.")
        return
    
    # # Fetch and generate activities
    # activities = get_github_activity(username, token)
    # print("Fetched GitHub activities successfully!")

    # markdown_content = generate_markdown(username, activities)
    # print("Generated markdown content successfully!")
    
    # # Optional: Write to README.md
    # with open('README.md', 'w') as f:
    #     f.write(markdown_content)
    
    # print("GitHub activity summary generated successfully!")

    # Check for follower changes
    new_followers, lost_followers = check_new_github_followers(username, token_2)
    if new_followers or lost_followers:
        send_email(
            sender_email=os.environ.get('SEND_GMAIL'),
            receiver_email=os.environ.get('RECIEVE_GMAIL'),
            app_password=os.environ.get('GMAIL_APP_PASSWORD'),
            subject="GitHub Follower Updates",
            new_followers=new_followers,
            lost_followers=lost_followers,
        )
        print("Email sent successfully!")


if __name__ == "__main__":
    main()
