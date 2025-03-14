import requests
import pixela_var

USERNAME = pixela_var.user
TOKEN = pixela_var.token

pixela_endpoint = "https://pixe.la/v1/users"

pixela_user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Setup user account
# response_user = requests.post(url=pixela_endpoint, json=pixela_user_params)
# print(response_user.text)

# Create Graph
pixela_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

pixela_graph_params = {
    "id": "g01",
    "name": "Pages Read",
    "unit": "Pages",
    "type": "int",
    "color": "ajisai",
}

headers = {"X-USER-TOKEN": TOKEN}

reponse_g01 = requests.post(
    url=pixela_graph_endpoint, json=pixela_graph_params, headers=headers
)
print(reponse_g01.text)
