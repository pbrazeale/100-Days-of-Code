import requests
from datetime import datetime
import smtplib

# import iss_call

MY_LAT = 30.267153
MY_LNG = -97.743057
iss_lat = 0
iss_lng = 0
sunset = 0
sunrise = 0


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


def main():
    time_now = datetime.now()
    # print(time_now.hour)
    sun_call()

    # if dark
    if (
        int(sunset.split("T")[1].split(":")[0]) - 6 < time_now.hour
        or int(sunrise.split("T")[1].split(":")[0]) - 6 > time_now.hour
    ):
        # Check if within sight
        if (
            (MY_LAT + 5) > iss_lat
            and (MY_LAT - 5) < iss_lat
            and (MY_LNG + 5) > iss_lng
            and (MY_LNG - 5) < iss_lng
        ):
            # send email
            send_email()


def send_email():
    pass


if __name__ == "__main__":
    main()
