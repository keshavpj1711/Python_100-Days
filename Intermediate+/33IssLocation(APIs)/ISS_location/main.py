import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response)
response.raise_for_status()
# raise_for_status() basically raises the error for us for all the unsuccesful requests

# Getting hold of data 
# Since it gives back a json format data 
data = response.json()
# print(data)

# Now we only require iss_position key from the json response
iss_pos = data["iss_position"]

# Getting the lats and longs
iss_pos_latitude = iss_pos["latitude"]
iss_pos_longitude = iss_pos["longitude"]

print(f"Current ISS position is \nLatitude: {iss_pos_latitude}\nLongitude: {iss_pos_longitude}")