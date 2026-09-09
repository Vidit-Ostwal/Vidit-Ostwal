import os
from helper_function import check_new_github_followers, follower_email_subject, send_email

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
    if new_followers or lost_followers:
        send_email(
            sender_email=os.environ.get('SEND_GMAIL'),
            receiver_email=os.environ.get('RECIEVE_GMAIL'),
            app_password=os.environ.get('GMAIL_APP_PASSWORD'),
            subject=follower_email_subject(new_followers, lost_followers),
            new_followers=new_followers,
            lost_followers=lost_followers,
            total_followers=total_followers,
        )
        print("Email sent successfully!")


if __name__ == "__main__":
    main()
