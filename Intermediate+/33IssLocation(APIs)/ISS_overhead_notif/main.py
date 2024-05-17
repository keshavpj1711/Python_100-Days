import requests

# These are the parameters we need to pass during api call
parameters = {
    # Lats and Longs for your location 
    "lat":28.644800,
    "lng":77.216721,
    "tzid":"Asia/Kolkata"
}

# This is how you pass parameters
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)

# Checking for any errors
response.raise_for_status()

data = response.json()
print(data)

