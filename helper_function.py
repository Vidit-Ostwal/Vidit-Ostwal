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

from hdfc_tt_buy import fetch_hdfc_usd_tt_buy

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


# Each stored day looks like {"date": "2026-11-20", "axis": "91.45", "hdfc": "91.50"};
# a bank whose fetch failed that day is simply absent.
BANKS = {
    "axis": {"name": "Axis Bank", "fetch": fetch_usd_tt_buy, "color": "#3987e5"},
    "hdfc": {"name": "HDFC Bank", "fetch": fetch_hdfc_usd_tt_buy, "color": "#d95926"},
}


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
    rates = []
    for entry in data:
        if not isinstance(entry, dict) or not entry.get("date"):
            continue
        if "usd" in entry and "axis" not in entry:
            # Older entries stored only the Axis rate, under "usd".
            entry = {**entry, "axis": entry["usd"]}
        clean = {"date": entry["date"]}
        clean.update({bank: entry[bank] for bank in BANKS if entry.get(bank)})
        if len(clean) > 1:
            rates.append(clean)
    return rates


def record_tt_rates(fetched: dict[str, str], on_date: str | None = None) -> list[dict]:
    """
    Merge today's fetched rates into the stored day (so a bank that fails on a
    re-run keeps its earlier value), keep the latest 10 days, return oldest first.
    """
    if on_date is None:
        on_date = datetime.now(ZoneInfo("Asia/Kolkata")).date().isoformat()

    rates = load_tt_rates()
    today = next((entry for entry in rates if entry["date"] == on_date), None)
    if today is None:
        today = {"date": on_date}
        rates.append(today)
    today.update(fetched)
    rates.sort(key=lambda entry: entry["date"])
    rates = rates[-TT_STORE_DAYS:]

    with open(TT_RATES_FILE, "w") as f:
        json.dump(rates, f, indent=4)
        f.write("\n")
    summary = ", ".join(f"{BANKS[bank]['name']} {rate}" for bank, rate in fetched.items())
    print(f"Stored USD TT Buy for {on_date}: {summary} ({len(rates)} day(s) kept).")
    return rates


def update_usd_tt_buy_history() -> list[dict]:
    """
    Fetch today's TT Buy from every bank, store what succeeded, and return up
    to the last 7 stored days, newest first. A failing bank never blocks the others.
    """
    fetched = {}
    for bank, info in BANKS.items():
        try:
            fetched[bank] = info["fetch"]()
        except (requests.exceptions.RequestException, ValueError, OSError, ImportError) as e:
            print(f"Error fetching {info['name']} USD TT Buy rate: {e}")

    history = sorted(load_tt_rates(), key=lambda entry: entry["date"])
    if fetched:
        try:
            history = record_tt_rates(fetched)
        except OSError as e:
            print(f"Error saving USD TT Buy rates: {e}")
    return list(reversed(history[-TT_EMAIL_DAYS:]))


def tt_rate_comparison(tt_rates: list[dict]) -> dict | None:
    """
    Compare banks on the latest stored day. TT Buy is what the bank pays you per
    USD received, so the higher rate is the better one.
    """
    if not tt_rates:
        return None
    latest = tt_rates[0]
    quotes = [(bank, float(latest[bank])) for bank in BANKS if latest.get(bank)]
    if not quotes:
        return None
    best_bank, best_rate = max(quotes, key=lambda quote: quote[1])
    others = [rate for bank, rate in quotes if bank != best_bank]
    gap = best_rate - max(others) if others else None
    return {
        "date": latest["date"],
        "quotes": [(bank, latest[bank]) for bank, _ in quotes],
        "missing": [bank for bank in BANKS if not latest.get(bank)],
        "best": best_bank if gap else None,  # None when only one bank or a tie
        "gap": gap,
    }


def render_tt_rate_chart(tt_rates: list[dict]) -> bytes | None:
    """
    Render a dark-theme PNG line chart of USD TT Buy against date, one line per bank.
    Expects entries newest first (as returned by update_usd_tt_buy_history).
    Returns None when there are fewer than 2 days or matplotlib is missing,
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

    entries = sorted(tt_rates, key=lambda entry: entry["date"])
    all_dates = [datetime.fromisoformat(entry["date"]) for entry in entries]
    series = {}
    for bank in BANKS:
        points = [
            (datetime.fromisoformat(entry["date"]), float(entry[bank]))
            for entry in entries
            if entry.get(bank)
        ]
        if points:
            series[bank] = points
    if not series:
        return None

    fig, ax = plt.subplots(figsize=(6.4, 3.2), dpi=200)
    fig.patch.set_facecolor(surface)
    ax.set_facecolor(surface)

    for bank, points in series.items():
        color = BANKS[bank]["color"]
        dates = [d for d, _ in points]
        values = [v for _, v in points]
        ax.plot(dates, values, color=color, linewidth=2, solid_capstyle="round",
                zorder=2, label=BANKS[bank]["name"])
        # Markers with a surface-coloured ring so overlapping points stay readable.
        ax.scatter(dates, values, s=48, color=color, edgecolors=surface, linewidths=2, zorder=3)

    # Direct-label each bank's latest value; the higher one above, the lower below.
    latest = {bank: points[-1] for bank, points in series.items()}
    ranked = sorted(latest, key=lambda bank: latest[bank][1], reverse=True)
    for rank, bank in enumerate(ranked):
        when, value = latest[bank]
        above = rank == 0
        ax.annotate(
            f"{value:.2f}",
            (when, value),
            xytext=(0, 10 if above else -16),
            textcoords="offset points",
            ha="center",
            color=text_primary,
            fontsize=9,
            fontweight="bold",
        )

    ax.set_title(
        "USD TT Buy (INR)",
        loc="left",
        color=text_primary,
        fontsize=11,
        fontweight="bold",
        pad=12,
    )
    if len(series) > 1:
        # Legend sits on the title row, right-aligned.
        legend = ax.legend(
            loc="lower right", bbox_to_anchor=(1.0, 1.0), ncol=len(series), frameon=False,
            fontsize=8, handlelength=1.6, borderaxespad=0.6,
        )
        for text in legend.get_texts():
            text.set_color(text_secondary)

    ax.set_xticks(all_dates)
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%d %b"))
    ax.tick_params(colors=text_secondary, labelsize=8, length=0, pad=6)
    ax.grid(axis="y", color=grid, linewidth=0.6)
    ax.set_axisbelow(True)
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.spines["bottom"].set_color(grid)

    values = [v for points in series.values() for _, v in points]
    span = max(values) - min(values)
    margin = max(span * 0.25, 0.1)
    ax.set_ylim(min(values) - margin * 1.3, max(values) + margin * 1.6)

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
    comparison = tt_rate_comparison(tt_rates or [])
    if comparison:
        quotes = " · ".join(
            f"{BANKS[bank]['name'].split()[0]} {rate}" for bank, rate in comparison["quotes"]
        )
        return f"Daily update · USD TT Buy {quotes}"
    return "Daily update"


def _comparison_verdict(comparison: dict) -> str:
    if comparison["best"]:
        return (
            f"{BANKS[comparison['best']]['name']} pays ₹{comparison['gap']:.2f} more per USD."
        )
    if len(comparison["quotes"]) > 1:
        return "Both banks pay the same rate."
    return ""


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
    comparison = tt_rate_comparison(tt_rates)
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

    if comparison:
        text_lines.append("")
        text_lines.append(f"USD TT Buy — {comparison['date']}")
        for bank, rate in comparison["quotes"]:
            text_lines.append(f"- {BANKS[bank]['name']}: {rate}")
        for bank in comparison["missing"]:
            text_lines.append(f"- {BANKS[bank]['name']}: unavailable")
        verdict = _comparison_verdict(comparison)
        if verdict:
            text_lines.append(verdict)
        text_lines.append("")
        text_lines.append("Last 7 stored days:")
        for entry in tt_rates:
            cells = ", ".join(
                f"{BANKS[bank]['name'].split()[0]} {entry.get(bank, '-')}" for bank in BANKS
            )
            text_lines.append(f"- {entry['date']}: {cells}")

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
        <img src="{chart_src}" alt="USD TT Buy by bank, last {len(tt_rates)} days"
             width="640" style="display: block; max-width: 100%; height: auto; border-radius: 8px; margin: 8px 0 16px;" />
        """

    tt_section = ""
    if comparison:
        best = comparison["best"]
        quote_rows = "".join(
            f"""
            <tr>
              <td style="padding: 4px 24px 4px 0;">{BANKS[bank]['name']}</td>
              <td style="padding: 4px 0; text-align: right;"><strong>{rate}</strong>{' ✓' if bank == best else ''}</td>
            </tr>
            """
            for bank, rate in comparison["quotes"]
        ) + "".join(
            f"""
            <tr>
              <td style="padding: 4px 24px 4px 0;">{BANKS[bank]['name']}</td>
              <td style="padding: 4px 0; text-align: right; color: #777;">unavailable</td>
            </tr>
            """
            for bank in comparison["missing"]
        )
        on_date = datetime.fromisoformat(comparison["date"]).strftime("%d %b %Y")
        verdict = _comparison_verdict(comparison)
        tt_section = f"""
        <h2>USD TT Buy — bank comparison</h2>
        <p style="margin: 0 0 4px; color: #555;">Rates for {on_date} (₹ paid per USD received — higher is better):</p>
        <table style="border-collapse: collapse; margin-bottom: 4px;">
          {quote_rows}
        </table>
        {f'<p style="margin: 4px 0 12px;">{verdict}</p>' if verdict else ''}
        {chart_html}
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
