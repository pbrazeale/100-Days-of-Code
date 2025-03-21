import nutritionix
import requests
import personal_data
import datetime as dt

# NUTRITIONIX
NUT_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
NUT_API_ID = nutritionix.APP_ID
NUT_API_KEY = nutritionix.API_KEY

# Personal Data
WEIGHT_KG = personal_data.weight_kg
HEIGHT_CM = personal_data.height_cm
AGE = personal_data.age

# Sheety
SHEETY_ENDPOINT = "https://api.sheety.co/"
SHEETY_USERNAME = "4dfcd642881f2f86ea467aeb6da6e18b"
SHEETY_PROJECT = "workoutTraining"
SHEETY_SHEET1 = "sheet1"

# Query
nut_query = input(
    "What 'exercise' did you do and for how 'long'? Exmaple: 'swam for 1 hour'\n:  "
)


# Requests
headers = {"x-app-id": NUT_API_ID, "x-app-key": NUT_API_KEY}

parameters = {
    "query": nut_query,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

# NUTRITIONIX API Call
nut_response = requests.post(NUT_ENDPOINT, json=parameters, headers=headers)
nut_reults = nut_response.json()
print(nut_reults)

# Sheety API CALL
sheety_response = requests.get(
    f"{SHEETY_ENDPOINT}/{SHEETY_USERNAME}/{SHEETY_PROJECT}/{SHEETY_SHEET1}"
)
sheety_results = sheety_response.json()
