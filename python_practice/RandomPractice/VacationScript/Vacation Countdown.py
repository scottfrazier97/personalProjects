import smtplib
from email.mime.text import MIMEText
from email.header import Header
import os
from dotenv import load_dotenv
import datetime

load_dotenv(r"C:\Users\troyf\OneDrive\Desktop\Personal Coding\personalProjects\.env")

# Get the folder where *this script* lives
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Build a full path to index.html
html_path = os.path.join(BASE_DIR, "index.html")
css_path = os.path.join(BASE_DIR, "style.css")

def get_days_until_vacay():
    today = datetime.date.today()
    departure_date = datetime.date(2025, 12, 2)
    days_until_vacation = str(departure_date - today).split()[0]
    return days_until_vacation if int(days_until_vacation) > 0 else "0"

def send_email():
    gmail_pw = os.getenv("GMAIL_PW")
    sender = os.getenv("SENDER_EMAIL")
    recipient = os.getenv("RECIPIENT_EMAIL")

    subject = "🎉 Vacation Countdown 🥳"

    # Load HTML template
    with open(html_path, "r", encoding="utf-8") as f:
        html_template = f.read()

    # Load CSS and inject into <style> tag
    with open(css_path, "r", encoding="utf-8") as f:
        css_content = f.read()

    # Replace placeholders
    body = html_template.replace("{{days}}", get_days_until_vacay())
    body = body.replace(
        '<link rel="stylesheet" type="text/css" href="style.css">',
        f"<style>{css_content}</style>"
    )

    msg = MIMEText(body, 'html', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = sender
    msg['To'] = recipient

    with smtplib.SMTP('smtp.gmail.com', 587) as s:
        s.starttls()
        s.login(sender, gmail_pw)
        s.sendmail(msg['From'], msg['To'], msg.as_string())

send_email()
