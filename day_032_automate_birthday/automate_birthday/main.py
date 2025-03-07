##################### Extra Hard Starting Project ######################
import datetime as dt
import smtplib
import pandas
import random
from vars import *

letter = ""
birthday_email = ""

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
year = now.year
month = now.month
day = now.day

now_format = f"{year},{month},{day}"


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv


# 4. Send the letter generated in step 3 to that person's email address.
def send_email():
    global letter, birthday_email
    email_subject = "Happy Birthday"
    email_body = letter

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=test_email, password=test_email_password)
        connection.sendmail(
            from_addr=test_email,
            to_addrs=birthday_email,
            msg=(f"Subject:{email_subject}\n\n{email_body}"),
        )
