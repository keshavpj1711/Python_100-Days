import requests
import os 
import datetime
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

# Creating and cofiguring our graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
# print(response.text)
 
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config["id"]}"


# Pushing a pixel

# Getting current date and changing to required format i.e. yyyymmdd
present_date = str(datetime.date.today())
present_date = present_date.split("-")
curr_date = ""
for i in present_date:
    curr_date += i
# print(curr_date)

# No of pages read
pages_read = (input("No of pages you read: "))

pixel_config = {
    "date": curr_date,
    "quantity": pages_read,
}

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=header)
print(response.text)
print(response)