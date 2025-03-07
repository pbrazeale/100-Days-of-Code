import smtplib
from vars import *
import datetime as dt
import random

now = dt.datetime.now()
quote_of_the_day = ""


# select quote line with random as quote_of_the_day
def select_quote():
    global quote_of_the_day
    with open("quotes.txt", "r") as file:
        quotes = file.readlines()

    quote_of_the_day = random.choice(quotes).strip()


def send_email():
    global quote_of_the_day
    email_subject = "Quote Of The Day"
    email_body = quote_of_the_day

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=test_email, password=test_email_password)
        connection.sendmail(
            from_addr=test_email,
            to_addrs=target_email,
            msg=(f"Subject:{email_subject}\n\n{email_body}"),
        )
