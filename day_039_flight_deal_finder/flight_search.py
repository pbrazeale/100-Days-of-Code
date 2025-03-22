import os
import requests
from dotenv import load_dotenv
import datetime

load_dotenv()

IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations"
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._api_key = os.environ["AMADAUS_API_KEY"]
        self._api_secret = os.environ["AMADAUS_API_SECRET"]
        self._token = self._get_new_token()

    def get_destination_code(self, city_name):
        headers = {"Authorization": f"Bearer {self._token}"}
        amadaus_params = {
            "keyword": city_name,
            "max": "2",
            "subTYpe": "AIRPOT",
        }

        amadaus_response = requests.get(
            url=IATA_ENDPOINT,
            headers=headers,
            params=amadaus_params,
        )

        print(
            f"Status code {amadaus_response.status_code}. Airport IATA: {amadaus_response.text}"
        )
        try:
            code = amadaus_response.json()["data"][0]["iataCode"]
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}.")
            return "Not Found"

        return code

    def _get_new_token(self):
        header = {"Content-Type": "application/x-www-form-urlencoded"}
        body = {
            "grant_type": "client_credentials",
            "client_id": self._api_key,
            "client_secret": self._api_secret,
        }
        response = requests.post(
            url=TOKEN_ENDPOINT,
            headers=header,
            data=body,
        )

        # New bearer token. Typically expires in 1799 seconds (30min)
        print(f"Your token is {response.json()['access_token']}")
        print(f"Your token expires in {response.json()['expires_in']} seconds")
        return response.json()["access_token"]
