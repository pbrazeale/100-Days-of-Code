import smtplib
from vars import *


email_subject = "Hello"
email_body = "This is the body of the email."


with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=test_email, password=test_email_password)
    connection.sendmail(
        from_addr=test_email,
        to_addrs=target_email,
        msg=(f"Subject:{email_subject}\n\n{email_body}"),
    )
