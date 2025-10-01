import datetime
from datetime import date

def get_days_until_vacay():

    today = datetime.date.today()
    departure_date = datetime.date(2025, 12, 12)

    days_until_vacation = str(departure_date - today).split()[0]

    return days_until_vacation


def send_email():

    import smtplib
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login("scottboyy97@gmail.com", "sender_email_id_password")

    # message to be sent
    message = "Message_you_need_to_send"

    # sending the mail
    s.sendmail("sender_email_id", "receiver_email_id", message)

    # terminating the session
    s.quit()