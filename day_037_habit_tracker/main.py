import requests
import pixela_var
from datetime import datetime

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

pixela_headers = {"X-USER-TOKEN": TOKEN}

# reponse_g01 = requests.post(
#     url=pixela_graph_endpoint, json=pixela_graph_params, headers=pixela_headers
# )
# print(reponse_g01.text)

graph_ids = {"Pages Read": "g01"}

# Post Pixel
# https://docs.pixe.la/entry/post-pixel
today = datetime.today().strftime("%Y%m%d")
# print(today)
post_quantity = input("How many pages did you read?: ")

pixela_post_params = {"date": today, "quantity": post_quantity}
pixela_post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_ids["Pages Read"]}"
pixela_graph_post = requests.post(
    url=pixela_post_endpoint, json=pixela_post_params, headers=pixela_headers
)
