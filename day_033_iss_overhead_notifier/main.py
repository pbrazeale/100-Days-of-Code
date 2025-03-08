import requests
from datetime import datetime
import smtplib

MY_LAT = 30.267153
MY_LNG = -97.743057

iss_latitude = float(0)
iss_longitude = float(0)


def iss_call():
    global iss_latitude, iss_longitude

    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    data = iss_response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])


def main():

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

    time_now = datetime.now()
    # print(time_now.hour)

    # Check if within sight
    within_sight = False
    if (
        (MY_LAT + 5) > iss_latitude
        and (MY_LAT - 5) < iss_latitude
        and (MY_LNG + 5) > iss_longitude
        and (MY_LNG - 5) < iss_longitude
    ):
        within_sight = True
    # print(iss_position)

    # if dark and iss overhead
    if (
        int(sunset.split("T")[1].split(":")[0]) - 6 < time_now.hour
        or int(sunrise.split("T")[1].split(":")[0]) - 6 > time_now.hour
        and within_sight
    ):
        send_email()


def send_email():
    pass


if __name__ == "__main__":
    main()
