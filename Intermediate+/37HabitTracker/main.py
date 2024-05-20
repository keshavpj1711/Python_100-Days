import requests
import os 
from dotenv import load_dotenv

# Basically loading those environment variables which are to be used
load_dotenv()

pixela_endpoint = "https://pixe.la/v1/users"

# Setting up our pixela account
user_param = {
    "token": str(os.environ.get("pixela_token")),
    "username": str(os.environ.get("pixela_username")),
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# To setup user account 
# response = requests.post(url=pixela_endpoint, json=user_param)
# print(response.text)