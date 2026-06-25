"""
fetch_emails.py

Phase 1: connect to ONE Gmail account using OAuth, and print the subject
+ sender of every email received today.

How the OAuth flow works the first time you run this:
1. This script looks for a file called token.json (it won't exist yet).
2. Since it doesn't exist, it opens your default web browser to a Google
   login page.
3. You log in and click "Allow" to grant this app read-only access to Gmail.
4. Google sends back a token, which this script saves into token.json.
5. Every future run reuses token.json automatically — no browser popup
   needed again, unless the token expires or is revoked.
"""

import os
import datetime
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# SCOPES define exactly what permission we're asking for.
# "readonly" means this app can read email, but cannot send, delete, or
# modify anything. This is intentional and important for safety.
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]


def get_credentials():
    """
    Handles the OAuth flow. Returns valid credentials, either by loading
    a saved token, refreshing an expired one, or running the login flow
    for the first time.
    """
    creds = None

    # If we've logged in before, token.json will exist - reuse it.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    # If there's no valid token, either refresh it or log in fresh.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            # Token expired but we can refresh it without a new browser login
            creds.refresh(Request())
        else:
            # No token at all yet - run the full browser-based login flow
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)

        # Save the token (whether refreshed or newly created) for next time
        with open("token.json", "w") as token_file:
            token_file.write(creds.to_json())

    return creds


def get_todays_emails(service):
    """
    Queries Gmail for messages received today, and returns a list of
    (sender, subject) tuples.
    """
    # Gmail search queries use the same syntax as the Gmail search bar.
    # "after:YYYY/MM/DD" filters to messages received on or after that date.
    today_str = datetime.date.today().strftime("%Y/%m/%d")
    query = f"after:{today_str}"

    results = service.users().messages().list(userId="me", q=query).execute()
    messages = results.get("messages", [])

    email_summaries = []

    for msg in messages:
        # Each message in the list only has an ID - we need a second call
        # to get the actual subject/sender for each one.
        msg_data = (
            service.users()
            .messages()
            .get(userId="me", id=msg["id"], format="metadata",
                 metadataHeaders=["From", "Subject"])
            .execute()
        )

        headers = msg_data["payload"]["headers"]
        sender = next((h["value"] for h in headers if h["name"] == "From"), "(unknown sender)")
        subject = next((h["value"] for h in headers if h["name"] == "Subject"), "(no subject)")

        email_summaries.append((sender, subject))

    return email_summaries


def main():
    creds = get_credentials()
    service = build("gmail", "v1", credentials=creds)

    emails = get_todays_emails(service)

    print(f"\nFound {len(emails)} email(s) today:\n")
    for sender, subject in emails:
        print(f"From: {sender}")
        print(f"Subject: {subject}")
        print("-" * 40)


if __name__ == "__main__":
    main()