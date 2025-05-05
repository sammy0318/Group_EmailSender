## Email Sending Script using Gmail SMTP

This Python script allows you to send emails using Gmail's SMTP server. It supports sending plain text and HTML-formatted emails, and it is capable of sending bulk emails to multiple recipients.

## Features

Sends emails via Gmail SMTP server (smtp.gmail.com).

Supports both plain text and HTML email formats.

Handles sending emails to multiple recipients.

Allows the use of Gmail's app password for secure authentication.

## Prerequisites

Python 3.x installed on your system.

A Gmail account with 2-Step Verification enabled (for app password generation).

The following Python libraries:

smtplib (comes pre-installed with Python).

email (comes pre-installed with Python).

ssl (comes pre-installed with Python).

time (comes pre-installed with Python).

## Installation

Generate an app password for Gmail:

If you have 2-Step Verification enabled for your Gmail account, generate an app password by following the steps below:

Go to your Google account settings.

Navigate to Security > App passwords.

Generate a new app password for "Mail" and note it down.

Clone the repository or create a new Python file:

Copy the script into a new Python file (e.g., send_bulk_email.py).

Install required libraries:

You don't need any external libraries for this script, as the necessary modules (smtplib, email, ssl, time) are part of Python’s standard library.

## Usage

Configure the script:

Gmail credentials: Replace the sender_email with your Gmail address and the password field with your app password.

Recipient list: Add the recipient email addresses in the recipients list.

Subject: Add your desired email subject in the subject field.

Email content: Customize both plain_text and html_content to fit your message.

Run the script:

After setting up the script with your information, run it using Python:

bash
Copy
Edit
python send_bulk_email.py
The script will send emails to the recipients in the recipients list. It will print out whether the email was successfully sent or if an error occurred.

## Example

sender_email = "your_email@gmail.com"
password = "your_app_password"

recipients = [
"recipient1@example.com",
"recipient2@example.com"
]

subject = "Test Email"
plain_text = "This is a test email."
html_content = "<html><body><p>This is a test email in HTML format.</p></body></html>"

## Important Notes

Limitations:

Gmail has a sending limit of 500 recipients per day. Be cautious about sending large volumes of emails in one go to avoid your account getting blocked.

The script is designed to send one email every 5 seconds (time.sleep(5)) to avoid rate limits from Gmail.

Security:

Never share your app password publicly or with anyone.

If you want to keep email addresses private, consider using the BCC field instead of the To field.
