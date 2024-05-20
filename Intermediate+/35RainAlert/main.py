import requests
import os
from dotenv import load_dotenv

load_dotenv()

location = input("Enter your location: ")

parameters = {
    "units": "metric",
    "appid": os.environ.get("api_key"), 
    "cnt": 4, 
    # This gives us only first 4 datas that is 12hrs
}

# Getting response from api and checking for any exceptions
response = requests.get(url=f"https://api.openweathermap.org/data/2.5/forecast?q={location}", params=parameters)
response.raise_for_status()

data = response.json()
weather_list = data["list"]

will_rain = False

for i in range(0, 4):
    weather_temp = weather_list[i]["weather"] # Storing the element with which we are working with
    weather_code = weather_temp[0]["id"]
    # print(weather_code)

    if weather_code < 700:
        will_rain = True

if will_rain:
    print("Bring Your Umbrella")
    # Now to add the alert feature what we can do is 
        # Either send an sms using some messaging api 
        # Or else send an email as we did earlier
    # At this point i am going to leave it here as money issues :sadgeko
else:
    print("You better leave your Umbrella at home")