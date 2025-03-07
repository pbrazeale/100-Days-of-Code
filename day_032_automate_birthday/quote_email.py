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
