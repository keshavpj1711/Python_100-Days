# This is where we will get the response of the api

import requests

response = requests.get(url="https://opentdb.com/api.php?amount=10&category=18&difficulty=medium&type=boolean")
# For handling any error
response.raise_for_status()

# Getting the data 
questions = response.json()
