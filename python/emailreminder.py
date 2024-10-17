#this script generates an email reminder to stretch or drink water
#and sends it to the user
#note: run pip install schedule before running this script

import smtplib
from email.mime.text import MIMEText
import time
import schedule
from datetime import datetime

# Set up email server and login details
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "Your email here"
SENDER_PASSWORD = "Your email password here"
RECIPIENT_EMAIL = "Recipient email here"

def send_email_reminder():
    subject = "Daily Reminder :)"
    body = "Don't forget to take a break and stretch and have some water!"

    # Create the email
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECIPIENT_EMAIL

    # Connect to the email server and send the email
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()  # Encrypt the connection
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, msg.as_string())

    print(f"Reminder sent at {datetime.now()}")

# Schedule the reminder (e.g., send every day at 10:00 AM)
schedule.every().day.at("10:00").do(send_email_reminder)

# Keep the script running and checking the schedule
while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minute
Footer
