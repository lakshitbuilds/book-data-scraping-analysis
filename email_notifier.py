import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

def send_email(subject, message):
    sender_email = os.getenv("EMAIL_ADDRESS")
    app_password = os.getenv("EMAIL_APP_PASSWORD")
    receiver_email = os.getenv("EMAIL_TO", sender_email)

    if not sender_email or not app_password:
        raise ValueError(
            "Email settings are missing. Set EMAIL_ADDRESS and EMAIL_APP_PASSWORD."
        )

    email = EmailMessage()
    email["From"] = sender_email
    email["To"] = receiver_email
    email["Subject"] = subject
    email.set_content(message)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender_email, app_password)
        smtp.send_message(email)
