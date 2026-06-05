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
        tuple[list[dict], list[dict]]: Two lists containing new followers and
        lost followers as dictionaries (login, profile_url). Returns
        ([], []) if an error occurs.
    """
    followers_file = "followers.json"

    # Load existing followers from file
    existing_followers_data = {}
    if os.path.exists(followers_file):
        try:
            with open(followers_file, 'r') as f:
                existing_followers_data = json.load(f)
        except json.JSONDecodeError:
            print(f"Warning: {followers_file} is corrupted or empty. Starting with an empty follower map.")
            existing_followers_data = {}
    
    if isinstance(existing_followers_data, list):
        # Backward compatibility with older list-based JSON format.
        existing_followers_data = {
            follower["login"]: follower["profile_url"]
            for follower in existing_followers_data
        }
    existing_follower_logins = set(existing_followers_data.keys())
    

    # Fetch current followers from GitHub API
    url = f"https://api.github.com/users/{username}/followers"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    current_followers_info = {}
    try:
        page = 1
        while True:
            response = requests.get(
                url,
                headers=headers,
                params={"per_page": 100, "page": page},
            )
            response.raise_for_status()
            followers_data = response.json()

            if not followers_data:
                break

            current_followers_info.update({
                follower['login']: follower['html_url']
                for follower in followers_data
            })
            page += 1
    except requests.exceptions.RequestException as e:
        print(f"Error fetching current followers from GitHub: {e}")
        return [], [], 0

    follower_login_from_api = set(current_followers_info.keys())

    # Identify new followers
    new_followers = []
    for login, profile_url in current_followers_info.items():
        if login not in existing_follower_logins:
            new_followers.append({'login': login, 'profile_url': profile_url})

    # Identify lost followers (users present before but missing now)
    lost_followers = []
    for login, profile_url in existing_followers_data.items():
        if login not in follower_login_from_api:
            lost_followers.append({'login': login, 'profile_url': profile_url})
    
    # Update the followers.json file with the current list of followers
    try:
        with open(followers_file, 'w') as f:
            json.dump(current_followers_info, f, indent=4)
        print(f"Updated {followers_file} with {len(current_followers_info)} followers.")
    except IOError as e:
        print(f"Error writing to {followers_file}: {e}")

    return new_followers, lost_followers, len(current_followers_info)


def send_email(
    sender_email: str,
    receiver_email: str,
    app_password: str,
    subject: str,
    new_followers: list[dict],
    lost_followers: list[dict],
    total_followers: int,
):
    msg = EmailMessage()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject

    # -------- Plain text fallback --------
    text_lines = [f"Current GitHub follower count: {total_followers}", ""]
    if new_followers:
        text_lines.append("New GitHub followers:")
        for f in new_followers:
            text_lines.append(f"- {f['login']}: {f['profile_url']}")
        text_lines.append("")

    if lost_followers:
        text_lines.append("Lost GitHub followers:")
        for f in lost_followers:
            text_lines.append(f"- {f['login']}: {f['profile_url']}")

    if not text_lines:
        text_lines.append("No follower changes.")

    msg.set_content("\n".join(text_lines))

    # -------- HTML version --------
    new_html_items = "".join(
        f"""
        <li>
          <a href="{f['profile_url']}" target="_blank">
            <strong>{f['login']}</strong>
          </a>
        </li>
        """
        for f in new_followers
    )

    lost_html_items = "".join(
        f"""
        <li>
          <a href="{f['profile_url']}" target="_blank">
            <strong>{f['login']}</strong>
          </a>
        </li>
        """
        for f in lost_followers
    )

    new_section = ""
    if new_followers:
        new_section = f"""
        <h2>🎉 New GitHub Followers</h2>
        <p>You got <strong>{len(new_followers)}</strong> new follower(s):</p>
        <ul>
          {new_html_items}
        </ul>
        """

    lost_section = ""
    if lost_followers:
        lost_section = f"""
        <h2>👋 Lost GitHub Followers</h2>
        <p>You lost <strong>{len(lost_followers)}</strong> follower(s):</p>
        <ul>
          {lost_html_items}
        </ul>
        """

    html_body = f"""
    <html>
      <body style="font-family: Arial, sans-serif;">
        <p>
          Current GitHub follower count:
          <strong>{total_followers}</strong>
        </p>
        {new_section}
        {lost_section}
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
