import requests # To actually make api requests
import os # To get env vars
from dotenv import load_dotenv # Loading the contents of .env file i.e. env vars
import datetime # To get todays date and time

# loading the .env file to access our environment variables
load_dotenv()

host_domain = "https://trackapi.nutritionix.com"
lang_for_exercise_endpoint = "/v2/natural/exercise"

# defining headers to auth our api request
header_nutritionix = {
    "x-app-id": os.environ.get("nutritionix_app_id"),
    "x-app-key": os.environ.get("nutritionix_api_key")
}

# Getting the response from the user 
user_input = input("Which Exercise you did: ")

# Setting the parameters 
parameters = {
    "query": user_input,
}

# Making a request
response_nutritionix = requests.post(url=f"{host_domain}{lang_for_exercise_endpoint}", json=parameters, headers=header_nutritionix)
response_nutritionix.raise_for_status() # Raise exceptions if any

# Checking the data we recieved 
data_nutritionix = response_nutritionix.json()
# print(data)

# Getting the actual data from the response 
excercises_data = data_nutritionix["exercises"]
exercises = [] # [{excercise_type: , duration_min: , cal_burned: ,}]

# Adding all the excerices you did to excercise
for i in range(len(excercises_data)):
    exercises.append({
        "excercise_type": excercises_data[i]["name"],
        "duration_min": excercises_data[i]["duration_min"],
        "cal_burned": excercises_data[i]["nf_calories"] 
    })

    print(exercises[i])


# Now we will be working with our created google sheet

# Sheety enpoint
sheety_endpoint = "https://api.sheety.co/aadea55b3946ad56fe2568ec9a2924f3/workoutTracker/sheet1"

# Authentication
header_sheety = {
    "Authorization": f"Bearer {os.environ.get("sheety_token")}"
}

# Connecting with sheety
response_sheety = requests.get(url=f"{sheety_endpoint}", headers=header_sheety)
response_sheety.raise_for_status()

# Checking the response of sheety api
data_sheety = response_sheety.json()
print(data_sheety)
