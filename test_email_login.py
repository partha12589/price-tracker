import smtplib
from dotenv import load_dotenv
import os

load_dotenv()
sender_email = os.getenv("EMAIL_USER1")
sender_password = os.getenv("EMAIL_PASS")

try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender_email, sender_password)
    print("Login successful!")
except Exception as e:
    print("Login failed:", e)
