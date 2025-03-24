import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

# Sheety
SHEETY_API = "https://api.sheety.co/"
SHEETY_USERNAME = os.environ["SHEETY_USERNAME"]
SHEETY_PROJECT = "flightDeals"
SHEETY_SHEET1 = "prices"
SHEETY_ENDPOINT = (
    f"{SHEETY_API}/{os.environ["SHEETY_PATH"]}/{SHEETY_PROJECT}/{SHEETY_SHEET1}"
)


class DataManager:
    def __init__(self):
        self._user = SHEETY_USERNAME
        self._password = os.environ["SHEETY_PASS"]
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}

    def get_destination_data(self):
        sheety_response = requests.get(url=SHEETY_ENDPOINT, auth=self._authorization)
        data = sheety_response.json()
        # print(data)
        self.destination_data = data[SHEETY_SHEET1]
        return self.destination_data

    # 6. In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {"price": {"iataCode": city["iataCode"]}}
            response = requests.put(
                url=f"{SHEETY_ENDPOINT}/{city['id']}",
                json=new_data,
                auth=self._authorization,
            )
            print(response.text)
