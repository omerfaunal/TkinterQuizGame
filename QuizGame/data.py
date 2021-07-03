import requests


def get_questions(category):
    parameters = {
        "amount": 10,
        "type": "boolean",
        "category": category,
    }
    data = requests.get(url="https://opentdb.com/api.php", params=parameters)
    data.raise_for_status()
    return data.json()["results"]
