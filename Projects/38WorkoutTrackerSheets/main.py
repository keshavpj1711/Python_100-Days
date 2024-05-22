import requests
import os 
from dotenv import load_dotenv

# loading the .env file to access our environment variables
load_dotenv()

host_domain = "https://trackapi.nutritionix.com"
lang_for_exercise_endpoint = "/v2/natural/exercise"

# defining headers to auth our api request
header = {
    "x-app-id": os.environ.get("app_id"),
    "x-app-key": os.environ.get("api_key")
}

# Getting the response from the user 
user_input = input("Which Exercise you did: ")

# Setting the parameters 
parameters = {
    "query": user_input,
}

# Making a request
response = requests.post(url=f"{host_domain}{lang_for_exercise_endpoint}", params=parameters, headers=header)
response.raise_for_status() # Raise exceptions if any

# Checking the data we recieved 
data = response.json()
print(data)

