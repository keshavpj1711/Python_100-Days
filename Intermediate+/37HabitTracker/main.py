import requests
import os 
from dotenv import load_dotenv

# Basically loading those environment variables which are to be used
load_dotenv()

USERNAME = str(os.environ.get("pixela_username"))
TOKEN = str(os.environ.get("pixela_token"))

pixela_endpoint = "https://pixe.la/v1/users"

# Setting up our pixela account
user_param = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# To setup user account 
# response = requests.post(url=pixela_endpoint, json=user_param)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# Cofiguring your graph
graph_config = {
    "id": "graph01",
    "name": "ReadingG",
    "unit": "pages",
    "type": "int",
    "color": "momiji"
}

header = {
    "X-USER-TOKEN": TOKEN,
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
print(response.text)

