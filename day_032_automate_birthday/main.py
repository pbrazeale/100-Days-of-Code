# import smtplib
# from vars import *


# email_subject = "Hello"
# email_body = "This is the body of the email."


# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=test_email, password=test_email_password)
#     connection.sendmail(
#         from_addr=test_email,
#         to_addrs=target_email,
#         msg=(f"Subject:{email_subject}\n\n{email_body}"),
#     )

import datetime as dt

now = dt.datetime.now()
print(now.year)

date_of_birth = dt.datetime(year=1995, month=12, day=15)
print(date_of_birth)
