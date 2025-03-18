import nutritionix
import requests
import personal_data

# NUTRITIONIX
NUT_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
NUT_API_ID = nutritionix.APP_ID
NUT_API_KEY = nutritionix.API_KEY

# Personal Data
WEIGHT_KG = personal_data.weight_kg
HEIGHT_CM = personal_data.height_cm
AGE = personal_data.age

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
