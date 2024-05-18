import requests
from datetime import datetime
import smtplib

MY_LAT = 28.644800
MY_LNG = 77.216721

def sendsms(reciever_email):
    # Basically this function sends and ISS Overhead Notification to the input email
    
    # Setting up connection to send email
    my_email = "test.user.python0520@gmail.com"
    my_password = "ayqkjzzlvconjyqk"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        # Starting TLS to ensure secure connection
        connection.starttls()

        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=reciever_email,
            msg="Subject:ISS Overhead Notifier\n\nLook above ISS is visible in the sky"
        )


# These are the parameters we need to pass during api call
parameters = {
    # Lats and Longs for your location 
    "lat":MY_LAT,
    "lng":MY_LNG,
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
sunrise = int(sunrise.split("T")[1].split(":")[0])
sunset = int(sunset.split("T")[1].split(":")[0])
curr_time = curr_time.hour


# Our next task is if it's dark and location of iss is near our viewpoint 
# Then send us an email
if (sunset < curr_time < sunrise):
    # Then only start looking if ISS is above us or not

    # Getting location from ISS Location API
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()

    iss_data = iss_response.json()
    iss_lat = float(iss_data["iss_position"]["latitude"])
    iss_lng = float(iss_data["iss_position"]["longitude"])

    # Checking if ISS is +- 5 deg around us 
    if (MY_LAT-5 < iss_lat < MY_LAT+5 and MY_LNG-5 < iss_lng < MY_LNG+5):
        # Send and email to notify
        sendsms("crueser123@gmail.com")

