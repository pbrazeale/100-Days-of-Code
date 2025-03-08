import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")

# if response.status_code != 200:
#     raise Exception(f"Error happened: {response.status_code}")

# requests will handle this for us.
response.raise_for_status()

data = response.json()

longitude = data["iss_positon"]["longitude"]
latitude = data["iss_positon"]["latitude"]
