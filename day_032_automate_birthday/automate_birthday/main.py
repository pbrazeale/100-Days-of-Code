##################### Extra Hard Starting Project ######################
import datetime as dt
import smtplib
import pandas
import random
from vars2 import *

data = pandas.read_csv("birthdays.csv")

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
month = now.month
day = now.day
now_format = (month, day)

birthdays_dict = {
    (data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()
}


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if now_format in birthdays_dict:
    birthday_person = birthdays_dict[now_format]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"

    with open(file_path) as file:
        letter = file.read()
        letter = letter.replace("[NAME]", birthday_person["name"].title())
        print(letter)

    # 4. Send the letter generated in step 3 to that person's email address.
    email_subject = "Happy Birthday"
    email_body = letter

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=test_email, password=test_email_password)
        connection.sendmail(
            from_addr=test_email,
            to_addrs=birthday_person["email"],
            msg=(f"Subject:{email_subject}\n\n{email_body}"),
        )
