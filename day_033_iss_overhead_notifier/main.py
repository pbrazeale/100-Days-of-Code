import requests
from datetime import datetime

MY_LAT = 30.267153
MY_LNG = -97.743057

iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
# if response.status_code != 200:
#     raise Exception(f"Error happened: {response.status_code}")

# requests will handle this for us.
iss_response.raise_for_status()

data = iss_response.json()
# print(data["iss_position"])

latitude = data["iss_position"]["latitude"]
longitude = data["iss_position"]["longitude"]

iss_position = (latitude, longitude)

# print(iss_position)

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

print(sunrise.split("T")[1].split(":")[0])
