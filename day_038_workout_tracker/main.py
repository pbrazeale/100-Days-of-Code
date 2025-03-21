import nutritionix
import requests
import personal_data
import datetime as dt
import sheety

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
SHEETY_USERNAME = sheety.username
SHEETY_PROJECT = "workoutTraining"
SHEETY_SHEET1 = "sheet1"
SHEETY_TOKEN = sheety.token

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
# print(nut_reults)

nut_exercise = nut_reults["exercises"][0]["name"]
nut_duration = nut_reults["exercises"][0]["duration_min"]
nut_calories = nut_reults["exercises"][0]["nf_calories"]
# print(f"{nut_exercise}\n{nut_duration}\n{nut_calories}")

# DateTime
now = dt.datetime.now()
sheety_date = now.strftime(f"%m/%d/%Y")
sheety_time = now.strftime(f"%X")

# Sheety API CALL
sheety_header = {"Authorization": f"Bearer {SHEETY_TOKEN}"}
sheety_post_endpoint = (
    f"{SHEETY_ENDPOINT}/{SHEETY_USERNAME}/{SHEETY_PROJECT}/{SHEETY_SHEET1}"
)
sheety_post_params = {
    f"{SHEETY_SHEET1}": {
        "date": sheety_date,
        "time": sheety_time,
        "exercise": nut_exercise,
        "duration": nut_duration,
        "calories": nut_calories,
    },
}
sheety_response = requests.post(
    url=sheety_post_endpoint, json=sheety_post_params, headers=sheety_header
)

print(sheety_response.text)
