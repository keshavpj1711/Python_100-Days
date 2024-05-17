import requests
from datetime import datetime

# These are the parameters we need to pass during api call
parameters = {
    # Lats and Longs for your location 
    "lat":28.644800,
    "lng":77.216721,
    "formatted":0, # To get 24 hour clock format
    "tzid":"Asia/Kolkata"
}

# This is how you pass parameters
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)

# Checking for any errors
response.raise_for_status()

data = response.json()
# print(data)

# Getting sunrise and sunset times
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

curr_time = datetime.now()

# Now our task is to just compare the current hour against sunset and sunrise hour
# So first we need to get hold of just the hour 
sunrise = sunrise.split("T")[1].split(":")[0]
sunset = sunset.split("T")[1].split(":")[0]
curr_time = curr_time.hour
