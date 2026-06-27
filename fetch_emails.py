

import os
import datetime
import base64
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]



def get_credentials():
    creds = None

    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)

        with open("token.json", "w") as token_file:
            token_file.write(creds.to_json())

    return creds


def get_todays_emails(service):
    
    today_str = datetime.date.today().strftime("%Y/%m/%d")
    query = f"after:{today_str}"

    results = service.users().messages().list(userId="me", q=query).execute()
    messages = results.get("messages", [])

    email_summaries = []

    for msg in messages:
        
        msg_data = (
            service.users().messages().get(userId="me", id=msg["id"], format="full").execute()
        )

        body= get_email_body(msg_data)

        headers = msg_data["payload"]["headers"]
        sender = next((h["value"] for h in headers if h["name"] == "From"), "(unknown sender)")
        subject = next((h["value"] for h in headers if h["name"] == "Subject"), "(no subject)")

        email_summaries.append({"sender": sender, "subject": subject, "body": body})

    return email_summaries


def get_email_body(msg_data):
    message=None
    if msg_data["payload"]["mimeType"] == "text/plain":
        message = msg_data["payload"]["body"]["data"]
    
    else:
        for part in msg_data["payload"].get("parts", []):
            if part["mimeType"] == "text/plain":
                message = part["body"]["data"]
                break
        if message is None:
            return ""
        
    return base64.urlsafe_b64decode(message).decode("utf-8")
    
creds = get_credentials()
service = build("gmail", "v1", credentials=creds)
allEmails = get_todays_emails(service)

def main(emails):
    print(f"\nFound {len(emails)} email(s) today:\n")

    allEmailBody="None"
    for email in emails:
        allEmailBody+=f"{email['body']}\n\n new email: \n"

    return allEmailBody

def getMetadata(emails):
    metaData=""
    for email in emails:
        metaData+=f"Email from {email['sender']}\n\n Subject: {email['subject']}\n========================\n"
    return metaData
        

if __name__ == "__main__":
    main()