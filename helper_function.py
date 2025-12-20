import os
import json
import requests
import ssl
import smtplib
from email.message import EmailMessage
from datetime import datetime
import feedparser

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


def get_all_substack_blogs(url):
    def parse_to_dd_mm_yyyy(date_str: str) -> str:
        try:
            dt = datetime.strptime(
                date_str, "%a, %d %b %Y %H:%M:%S GMT"
            )
            return dt.strftime("%d-%m-%Y")
        except ValueError:
            return None
            
    feed = feedparser.parse(url)
    blogs_list = [feedparser.FeedParserDict(title=e.title, link=e.link, published=parse_to_dd_mm_yyyy(e.published)) for e in feed.entries if e.title != "Coming soon"]
    
    return blogs_list[::-1]
