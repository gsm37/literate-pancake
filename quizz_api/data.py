import requests
param = {
    "amount":10,
    "type":"boolean",

}

response = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean")
response.raise_for_status()
data = response.json()

question_data = data["results"]