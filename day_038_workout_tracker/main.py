import nutritionix
import requests
import personal_data

NUT_API_ID = nutritionix.APP_ID
NUT_API_KEY = nutritionix.API_KEY

# Personal Data
WEIGHT_KG = personal_data.weight_kg
HEIGHT_CM = personal_data.height_cm
AGE = personal_data.age

NUT_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
