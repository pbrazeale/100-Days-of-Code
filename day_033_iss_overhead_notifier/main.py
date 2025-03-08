import requests
from datetime import datetime
import smtplib
from vars2 import *
import time

# import iss_call

MY_LAT = 30.267153
MY_LNG = -97.743057
iss_lat = 0
iss_lng = 0
sunset = 0
sunrise = 0
time_now = datetime.now()


def iss_call():
    global iss_lng, iss_lat
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    data = iss_response.json()

    iss_lat = float(data["iss_position"]["latitude"])
    iss_lng = float(data["iss_position"]["longitude"])


def sun_call():
    global sunset, sunrise
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }
    sunrise_resposne = requests.get(
        url="https://api.sunrise-sunset.org/json", params=parameters
    )
    sunrise_resposne.raise_for_status()

    # print(sunrise_resposne.json())
    data = sunrise_resposne.json()
    sunset = data["results"]["sunset"]
    sunrise = data["results"]["sunrise"]
    # print(f"sunrise {sunrise.split("T")[1].split(":")[0]}")


def is_dark():
    # Check if iss within sight
    if (
        int(sunset.split("T")[1].split(":")[0]) - 6 < time_now.hour
        or int(sunrise.split("T")[1].split(":")[0]) - 6 > time_now.hour
    ):
        return True


def iss_overhead():
    # if dark
    if (
        (MY_LAT + 5) > iss_lat
        and (MY_LAT - 5) < iss_lat
        and (MY_LNG + 5) > iss_lng
        and (MY_LNG - 5) < iss_lng
    ):
        return True


# send email
def send_email():
    email_subject = "ISS Overhead"
    email_body = f"Go outside and look {iss_lat}, {iss_lng}"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=test_email, password=test_email_password)
        connection.sendmail(
            from_addr=test_email,
            to_addrs=target_email,
            msg=(f"Subject:{email_subject}\n\n{email_body}"),
        )


# check is_dark and iss_overhead every 10 minutes
def check_10_min():
    while True:
        time.sleep(600)
        if is_dark() and iss_overhead():
            send_email()


def main():
    # print(time_now.hour)
    sun_call()
    check_10_min()


if __name__ == "__main__":
    main()
