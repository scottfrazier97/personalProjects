import smtplib
from email.mime.text import MIMEText
from email.header import Header
import os
from dotenv import load_dotenv
import datetime

load_dotenv(r"C:\Users\troyf\OneDrive\Desktop\Personal Coding\personalProjects\.env")

def get_days_until_vacay():
    today = datetime.date.today()
    departure_date = datetime.date(2025, 12, 12)
    days_until_vacation = str(departure_date - today).split()[0]

    if int(days_until_vacation) > 0:
        return days_until_vacation
    else:
        pass

def send_email():
    gmail_pw = os.getenv("GMAIL_PW")
    recipient = os.getenv("RECIPIENT_EMAIL")

    if not gmail_pw:
        raise ValueError("GMAIL_PW not found in environment variables!")

    subject = "🎉 Vacation Countdown 🥳"
    body = f"""
        WUDDUP BOO!

        Only {get_days_until_vacay()} days left until the big adventure! 🏖️✈️

        Here's what you can do while waiting:
        - Start packing 🧳
        - Make a playlist 🎶
        - Count down the days ⏳

        Stay excited! 😎
    """
    # Use MIMEText to handle UTF-8
    msg = MIMEText(body, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = "scottyboyy97@gmail.com"
    msg['To'] = recipient

    with smtplib.SMTP('smtp.gmail.com', 587) as s:
        s.starttls()
        s.login("scottyboyy97@gmail.com", gmail_pw)
        s.sendmail(msg['From'], msg['To'], msg.as_string())

send_email()
