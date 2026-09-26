import os
from helper_function import (
    check_new_github_followers,
    follower_email_subject,
    send_email,
    update_usd_tt_buy_history,
)

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass


def main():
    username = os.environ.get('GITHUB_USERNAME')
    token = os.environ.get('GITHUB_TOKEN')

    if not username or not token:
        print("Please set GITHUB_USERNAME and GITHUB_TOKEN environment variables.")
        return

    new_followers, lost_followers, total_followers = check_new_github_followers(username, token)
    tt_rates = update_usd_tt_buy_history()
    send_email(
        sender_email=os.environ.get('SEND_GMAIL'),
        receiver_email=os.environ.get('RECIEVE_GMAIL'),
        app_password=os.environ.get('GMAIL_APP_PASSWORD'),
        subject=follower_email_subject(new_followers, lost_followers, tt_rates),
        new_followers=new_followers,
        lost_followers=lost_followers,
        total_followers=total_followers,
        tt_rates=tt_rates,
    )
    print("Email sent successfully!")


if __name__ == "__main__":
    main()
