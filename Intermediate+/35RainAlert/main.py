import requests

# Location for which weather is to be accessed
LOC_LAT = 30.019764
LOC_LNG = 77.398468

# API Key for auth
API_KEY = "d14209b71019b3cf0b94de684dcb5c12"

# Enter your location
location = input("Enter location: ")

# Getting the response from the openweather api
# response = requests.get(url=f"https://api.openweathermap.org/data/2.5/weather?lat={LOC_LAT}&lon={LOC_LNG}&appid={API_KEY}&units=metric")
response = requests.get(url=f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric")
# Raising any exceptions
response.raise_for_status()

# Getting data
data = response.json()
coord_data = data["coord"]
weather_data = data["weather"]
temp_data = data["main"]
visibility_data = data["visibility"]
wind_data = data["wind"]

print(coord_data)
print(temp_data)

