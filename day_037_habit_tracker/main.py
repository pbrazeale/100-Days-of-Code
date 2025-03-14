import requests
import pixela_var

pixela_endpoint = "https://pixe.la/v1/users"

pixela_user_params = {
    "token": pixela_var.token,
    "username": pixela_var.user,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response_user = requests.post(url=pixela_endpoint, json=pixela_user_params)
