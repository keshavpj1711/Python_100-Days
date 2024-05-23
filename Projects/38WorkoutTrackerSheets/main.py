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
response = requests.post(url=f"{host_domain}{lang_for_exercise_endpoint}", json=parameters, headers=header)
response.raise_for_status() # Raise exceptions if any

# Checking the data we recieved 
data = response.json()
# print(data)

# Getting the actual data from the response 
excercises_data = data["exercises"]
exercises = [] # [{excercise_type: , duration_min: , cal_burned: ,}]

# Adding all the excerices you did to excercise
for i in range(len(excercises_data)):
    exercises.append({
        "excercise_type": excercises_data[i]["name"],
        "duration_min": excercises_data[i]["duration_min"],
        "cal_burned": excercises_data[i]["nf_calories"] 
    })

    print(exercises[i])

