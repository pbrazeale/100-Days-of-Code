from Vars import amadaus
from day_038_workout_tracker import sheety
import pprint
import requests

# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

# Sheety
SHEETY_ENDPOINT = "https://api.sheety.co/"
SHEETY_USERNAME = sheety.username
SHEETY_PROJECT = "workoutTraining"
SHEETY_SHEET1 = "sheet1"
SHEETY_TOKEN = sheety.token

sheety_header = {"Authorization": f"Bearer {SHEETY_TOKEN}"}
sheety_endpoint = (
    f"{SHEETY_ENDPOINT}/{SHEETY_USERNAME}/{SHEETY_PROJECT}/{SHEETY_SHEET1}"
)

sheety_response = requests.get(url=sheety_endpoint, headers=sheety_header)

pprint(sheety_response.json())
