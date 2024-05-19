import requests

location = input("Enter your location: ")

parameters = {
    "units": "metric",
    "api_key": "d14209b71019b3cf0b94de684dcb5c12", 
    "cnt": 4, 
    # This gives us only first 4 datas that is 12hrs
}

# Getting response from api and checking for any exceptions
response = requests.get(url=f"api.openweathermap.org/data/2.5/forecast?q={location}", params=parameters)
response.raise_for_status()

data = response.json()
weather_list = data["list"]


for i in range(0, 4):
    weather_temp = weather_list[i]["weather"] # Storing the element with which we are working with
    weather_code = weather_temp[0]["id"]
    print(weather_code)