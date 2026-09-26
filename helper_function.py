import os
import json
import re
import requests
import ssl
import smtplib
from datetime import datetime
from email.message import EmailMessage
from zoneinfo import ZoneInfo

AXIS_CARD_RATE_URL = "https://application.axis.bank.in/webforms/corporatecardrate/index.aspx"
TT_RATES_FILE = "usd_tt_buy.json"
TT_STORE_DAYS = 10
TT_EMAIL_DAYS = 7

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


def fetch_usd_tt_buy() -> str:
    """
    TT Buy for US Dollar from the Axis Bank corporate card rate page.
    Same extraction as the first decimal in the US Dollar row.
    """
    response = requests.get(
        AXIS_CARD_RATE_URL,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=30,
    )
    response.raise_for_status()
    match = re.search(
        r"<th>\s*US Dollar\s*</th>(.*?)</tr>",
        response.text,
        re.DOTALL | re.IGNORECASE,
    )
    if not match:
        raise ValueError("US Dollar row not found on Axis Bank card rate page")

    row = re.sub(r"<!--.*?-->", "", match.group(1), flags=re.DOTALL)
    rate_match = re.search(r"<td>\s*([0-9]+\.[0-9]+)\s*</td>", row, re.DOTALL)
    if not rate_match:
        raise ValueError("USD TT Buy rate not found")
    return rate_match.group(1)


def load_tt_rates() -> list[dict]:
    if not os.path.exists(TT_RATES_FILE):
        return []
    try:
        with open(TT_RATES_FILE, "r") as f:
            data = json.load(f)
    except (json.JSONDecodeError, OSError):
        print(f"Warning: {TT_RATES_FILE} is corrupted or empty. Starting with an empty rate history.")
        return []
    if not isinstance(data, list):
        return []
    return [
        entry
        for entry in data
        if isinstance(entry, dict) and entry.get("date") and entry.get("usd")
    ]


def record_usd_tt_buy(rate: str, on_date: str | None = None) -> list[dict]:
    """
    Store one USD TT Buy value for a date, then keep only the latest 10 days.
    Returns the trimmed history, oldest first.
    """
    if on_date is None:
        on_date = datetime.now(ZoneInfo("Asia/Kolkata")).date().isoformat()

    rates = [entry for entry in load_tt_rates() if entry["date"] != on_date]
    rates.append({"date": on_date, "usd": rate})
    rates.sort(key=lambda entry: entry["date"])
    rates = rates[-TT_STORE_DAYS:]

    with open(TT_RATES_FILE, "w") as f:
        json.dump(rates, f, indent=4)
        f.write("\n")
    print(f"Stored USD TT Buy {rate} for {on_date} ({len(rates)} day(s) kept).")
    return rates


def update_usd_tt_buy_history() -> list[dict]:
    """
    Fetch today's TT Buy, store it, and return up to the last 7 stored days,
    newest first. If the fetch fails, return whatever history is already stored.
    """
    try:
        history = record_usd_tt_buy(fetch_usd_tt_buy())
    except (requests.exceptions.RequestException, ValueError, OSError) as e:
        print(f"Error fetching USD TT Buy rate: {e}")
        history = sorted(load_tt_rates(), key=lambda entry: entry["date"])
    return list(reversed(history[-TT_EMAIL_DAYS:]))


def follower_email_subject(
    new_followers: list[dict],
    lost_followers: list[dict],
    tt_rates: list[dict] | None = None,
) -> str:
    gained = len(new_followers)
    lost = len(lost_followers)
    if gained and lost:
        return f"Ching Chang +{gained} · Womp Womp -{lost} GitHub Followers"
    if gained:
        return f"Ching Chang! {gained} New GitHub Follower{'s' if gained != 1 else ''}"
    if lost:
        return f"Womp Womp... {lost} Lost GitHub Follower{'s' if lost != 1 else ''}"
    if tt_rates:
        return f"Daily update · USD TT Buy {tt_rates[0]['usd']}"
    return "Daily update"


def send_email(
    sender_email: str,
    receiver_email: str,
    app_password: str,
    subject: str,
    new_followers: list[dict],
    lost_followers: list[dict],
    total_followers: int,
    tt_rates: list[dict] | None = None,
):
    tt_rates = tt_rates or []
    msg = EmailMessage()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject

    # -------- Plain text fallback --------
    text_lines = [f"Current GitHub follower count: {total_followers}", ""]
    if new_followers:
        text_lines.append("💰 Ching Chang! New GitHub Followers")
        text_lines.append(f"The register just rang — {len(new_followers)} new follower(s) just walked in:")
        for f in new_followers:
            text_lines.append(f"- {f['login']}: {f['profile_url']}")
        text_lines.append("")

    if lost_followers:
        text_lines.append("👋 Womp Womp... Lost GitHub Followers")
        text_lines.append(f"The sad trombone played — {len(lost_followers)} follower(s) slipped away:")
        for f in lost_followers:
            text_lines.append(f"- {f['login']}: {f['profile_url']}")

    if not new_followers and not lost_followers:
        text_lines.append("No follower changes.")

    if tt_rates:
        text_lines.append("")
        text_lines.append("USD TT Buy (Axis Bank) — last 7 stored days")
        for entry in tt_rates:
            text_lines.append(f"- {entry['date']}: {entry['usd']}")

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
        <h2>💰 Ching Chang! New GitHub Followers</h2>
        <p>The register just rang — <strong>{len(new_followers)}</strong> new follower(s) just walked in:</p>
        <ul>
          {new_html_items}
        </ul>
        """

    lost_section = ""
    if lost_followers:
        lost_section = f"""
        <h2>👋 Womp Womp... Lost GitHub Followers</h2>
        <p>The sad trombone played — <strong>{len(lost_followers)}</strong> follower(s) slipped away:</p>
        <ul>
          {lost_html_items}
        </ul>
        """

    tt_rows = "".join(
        f"""
        <tr>
          <td style="padding: 4px 16px 4px 0;">{entry['date']}</td>
          <td style="padding: 4px 0;">{entry['usd']}</td>
        </tr>
        """
        for entry in tt_rates
    )
    tt_section = ""
    if tt_rates:
        tt_section = f"""
        <h2>USD TT Buy — Axis Bank</h2>
        <p>Last {len(tt_rates)} stored day(s):</p>
        <table style="border-collapse: collapse;">
          <thead>
            <tr>
              <th style="text-align: left; padding: 4px 16px 4px 0;">Date</th>
              <th style="text-align: left; padding: 4px 0;">USD</th>
            </tr>
          </thead>
          <tbody>
            {tt_rows}
          </tbody>
        </table>
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
        {tt_section}
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
