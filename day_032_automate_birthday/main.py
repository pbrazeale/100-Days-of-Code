import smtplib
from vars import *


connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=test_email, password=test_email_password)
connection.sendmail(from_addr=test_email, to_addrs=target_email, msg="Hello.")
connection.close()
