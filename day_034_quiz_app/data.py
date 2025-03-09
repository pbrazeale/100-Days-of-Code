import requests

trivia_response = requests.get(
    url="https://opentdb.com/api.php?amount=10&category=18&type=boolean"
)
data = trivia_response.json()
print(data["results"])

# question_data
