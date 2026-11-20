import os
import json
import re
import requests
import ssl
import smtplib
from datetime import datetime
from email.message import EmailMessage
from email.utils import make_msgid
from io import BytesIO
from zoneinfo import ZoneInfo

AXIS_CARD_RATE_URL = "https://application.axis.bank.in/webforms/corporatecardrate/index.aspx"
TT_RATES_FILE = "usd_tt_buy.json"
TT_STORE_DAYS = 10
TT_EMAIL_DAYS = 7
TT_CHART_DIR = "assets/tt-charts"

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


def render_tt_rate_chart(tt_rates: list[dict]) -> bytes | None:
    """
    Render a dark-theme PNG line chart of USD TT Buy against date.
    Expects entries newest first (as returned by update_usd_tt_buy_history).
    Returns None when there are fewer than 2 points or matplotlib is missing,
    so the email still goes out without the chart.
    """
    if len(tt_rates) < 2:
        return None
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        import matplotlib.dates as mdates
    except ImportError:
        print("matplotlib not installed; sending email without the rate chart.")
        return None

    surface = "#1a1a19"
    text_primary = "#f0efec"
    text_secondary = "#c3c2b7"
    grid = "#3a3a38"
    series = "#3987e5"

    points = sorted(
        (datetime.fromisoformat(entry["date"]), float(entry["usd"]))
        for entry in tt_rates
    )
    dates = [d for d, _ in points]
    values = [v for _, v in points]

    fig, ax = plt.subplots(figsize=(6.4, 3.0), dpi=200)
    fig.patch.set_facecolor(surface)
    ax.set_facecolor(surface)

    ax.plot(dates, values, color=series, linewidth=2, solid_capstyle="round", zorder=2)
    # Markers with a surface-coloured ring so they read cleanly on the line.
    ax.scatter(dates, values, s=48, color=series, edgecolors=surface, linewidths=2, zorder=3)

    # Selective direct label: latest value only.
    ax.annotate(
        f"{values[-1]:.2f}",
        (dates[-1], values[-1]),
        xytext=(0, 10),
        textcoords="offset points",
        ha="center",
        color=text_primary,
        fontsize=9,
        fontweight="bold",
    )

    ax.set_title(
        "USD TT Buy · Axis Bank (INR)",
        loc="left",
        color=text_primary,
        fontsize=11,
        fontweight="bold",
        pad=12,
    )

    ax.set_xticks(dates)
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%d %b"))
    ax.tick_params(colors=text_secondary, labelsize=8, length=0, pad=6)
    ax.grid(axis="y", color=grid, linewidth=0.6)
    ax.set_axisbelow(True)
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.spines["bottom"].set_color(grid)

    span = max(values) - min(values)
    margin = max(span * 0.25, 0.1)
    ax.set_ylim(min(values) - margin, max(values) + margin * 1.6)

    fig.tight_layout()
    buffer = BytesIO()
    fig.savefig(buffer, format="png", facecolor=surface)
    plt.close(fig)
    return buffer.getvalue()


def publish_tt_rate_chart(chart_png: bytes, on_date: str) -> str | None:
    """
    Save the chart under TT_CHART_DIR (keeping the latest TT_STORE_DAYS files)
    and return its raw.githubusercontent.com URL. The workflow commits and
    pushes the file right after the email is sent. Returns None outside
    GitHub Actions, where there is no pushed copy to link to.
    """
    repo = os.environ.get("GITHUB_REPOSITORY")
    branch = os.environ.get("GITHUB_REF_NAME")
    if not repo or not branch:
        return None
    try:
        os.makedirs(TT_CHART_DIR, exist_ok=True)
        path = os.path.join(TT_CHART_DIR, f"{on_date}.png")
        with open(path, "wb") as f:
            f.write(chart_png)
        charts = sorted(name for name in os.listdir(TT_CHART_DIR) if name.endswith(".png"))
        for old in charts[:-TT_STORE_DAYS]:
            os.remove(os.path.join(TT_CHART_DIR, old))
    except OSError as e:
        print(f"Error saving rate chart: {e}")
        return None
    return f"https://raw.githubusercontent.com/{repo}/{branch}/{TT_CHART_DIR}/{on_date}.png"


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
    chart_png = render_tt_rate_chart(tt_rates)
    chart_cid = make_msgid(domain="tt-rate.chart")
    chart_src = None
    if chart_png:
        # Prefer a hosted URL so mail clients don't list the chart as an attachment;
        # fall back to an embedded CID image when not running in GitHub Actions.
        chart_src = publish_tt_rate_chart(chart_png, tt_rates[0]["date"])
    use_cid = bool(chart_png) and chart_src is None
    if use_cid:
        chart_src = f"cid:{chart_cid[1:-1]}"
    chart_html = ""
    if chart_src:
        chart_html = f"""
        <img src="{chart_src}" alt="USD TT Buy rate, last {len(tt_rates)} days"
             width="640" style="display: block; max-width: 100%; height: auto; border-radius: 8px; margin: 8px 0 16px;" />
        """

    tt_section = ""
    if tt_rates and chart_html:
        tt_section = f"""
        <h2>USD TT Buy — Axis Bank</h2>
        {chart_html}
        """
    elif tt_rates:
        # No chart (fewer than 2 days or matplotlib missing): show the rows instead.
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
    if use_cid:
        msg.get_payload()[1].add_related(
            chart_png, maintype="image", subtype="png", cid=chart_cid
        )

    # -------- Send email --------
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, app_password)
        server.send_message(msg)
