import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, recipient_email, subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Upgrade to secure connection

        server.login(sender_email, sender_password)

        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)

        
        server.quit()

        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")

sender_email = input("Enter your Gmail address: ")
sender_password = input("Enter your Gmail password: ")
recipient_email = input("Enter the recipient's email address: ")
subject = input("Enter the email subject: ")
body = input("Enter the email body: ")

send_email(sender_email, sender_password, recipient_email, subject, body)
