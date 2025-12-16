import os
import requests
from datetime import datetime, timedelta
from litellm import completion
import json
from dotenv import load_dotenv
import smtplib
import ssl
from email.message import EmailMessage
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


def generate_blogs_markdown(blogs):
    markdown = ""
    for blog in blogs:
        markdown += f"- [{blog['blog_name']}]({blog['blog_url']}) - *{blog['blog_posting_date']}*\n"
        for sub_blog in blog.get("sub_blogs", []):
            markdown += f"  - [{sub_blog['blog_name']}]({sub_blog['blog_url']}) - *{sub_blog['blog_posting_date']}*\n"
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

    with open('blogs.json', 'r') as f:
        blog_json = json.load(f)

    blog_markdown = generate_blogs_markdown(blog_json['blogs'])
    markdown = f"# Recent GitHub Activity for {username}\n\n"
    
    # Blog Section
    markdown += '## 📝 Recent Blogs\n'
    markdown += blog_markdown

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


def check_new_github_followers(username, token):
    """
    Fetches the list of followers for a given GitHub username, compares them
    with a local 'followers.json' file, identifies new followers, and updates
    the local file.

    Args:
        username (str): The GitHub username.
        token (str): Your GitHub Personal Access Token with 'read:user' scope.

    Returns:
        list: A list of new follower dictionaries (login, profile_url),
              or an empty list if no new followers or an error occurs.
    """
    followers_file = "followers.json"

    # Load existing followers from file
    existing_followers_data = []
    if os.path.exists(followers_file):
        try:
            with open(followers_file, 'r') as f:
                existing_followers_data = json.load(f)
        except json.JSONDecodeError:
            print(f"Warning: {followers_file} is corrupted or empty. Starting with an empty list of existing followers.")
            existing_followers_data = []
    
    existing_follower_logins = {f['login'] for f in existing_followers_data}

    # Fetch current followers from GitHub API
    url = f"https://api.github.com/users/{username}/followers"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    current_followers_info = []
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        followers_data = response.json()
        current_followers_info = [{'login': follower['login'], 'profile_url': follower['html_url']} for follower in followers_data]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching current followers from GitHub: {e}")
        return []

    # Identify new followers
    new_followers = []
    for follower in current_followers_info:
        if follower['login'] not in existing_follower_logins:
            new_followers.append(follower)
    
    # Update the followers.json file with the current list of followers
    try:
        with open(followers_file, 'w') as f:
            json.dump(current_followers_info, f, indent=4)
        print(f"Updated {followers_file} with {len(current_followers_info)} followers.")
    except IOError as e:
        print(f"Error writing to {followers_file}: {e}")

    return new_followers


def send_email(
    sender_email: str,
    receiver_email: str,
    app_password: str,
    subject: str,
    followers: list[dict],
):
    msg = EmailMessage()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject

    # -------- Plain text fallback --------
    text_lines = ["New GitHub followers:\n"]
    for f in followers:
        text_lines.append(f"- {f['login']}: {f['profile_url']}")

    msg.set_content("\n".join(text_lines))

    # -------- HTML version --------
    html_items = "".join(
        f"""
        <li>
          <a href="{f['profile_url']}" target="_blank">
            <strong>{f['login']}</strong>
          </a>
        </li>
        """
        for f in followers
    )

    html_body = f"""
    <html>
      <body style="font-family: Arial, sans-serif;">
        <h2>🎉 New GitHub Followers</h2>
        <p>You got <strong>{len(followers)}</strong> new follower(s):</p>
        <ul>
          {html_items}
        </ul>
        <hr />
        <p style="color: #777; font-size: 12px;">
          Sent automatically by your GitHub follower notifier.
        </p>
      </body>
    </html>
    """

    msg.add_alternative(html_body, subtype="html")

    # -------- Send email --------
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, app_password)
        server.send_message(msg)


def main():
    # Get GitHub username and personal access token from environment variables
    username = os.environ.get('GITHUB_USERNAME')
    token = os.environ.get('GITHUB_TOKEN')
    token_2 = os.environ.get('GITHUB_TOKEN_2')
    
    if not username or not token:
        print("Please set GITHUB_USERNAME and GITHUB_TOKEN environment variables.")
        return
    
    # Fetch and generate activities
    activities = get_github_activity(username, token)
    print("Fetched GitHub activities successfully!")

    markdown_content = generate_markdown(username, activities)
    print("Generated markdown content successfully!")
    
    # Optional: Write to README.md
    with open('README.md', 'w') as f:
        f.write(markdown_content)
    
    print("GitHub activity summary generated successfully!")

    # Check for new followers
    new_followers = check_new_github_followers(username, token_2)
    if new_followers:
        send_email(
            sender_email=os.environ.get('SEND_GMAIL'),
            receiver_email=os.environ.get('RECIEVE_GMAIL'),
            app_password=os.environ.get('GMAIL_APP_PASSWORD'),
            subject="🎉 New GitHub Followers Today",
            followers=new_followers,
        )
        print("Email sent successfully!")


if __name__ == "__main__":
    main()
