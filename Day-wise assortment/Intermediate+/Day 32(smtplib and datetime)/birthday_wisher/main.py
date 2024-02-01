##################### Extra Hard Starting Project ######################

# 2. Check if today matches a birthday in the birthdays.csv


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import datetime as dt
import pandas as pd
import random


def send_msg(wish, name, msg):
    # Initialising my email
    my_email = "test.user.python0520@gmail.com"
    my_password = "ezyjbzaszosbhner"

    # Creating an obj that establishes connection with the mail server
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        # Starting TLS - Transport Layer Security, it's a way of securing connection with the mail server
        # Reason: So that no one can intercept our message, since tls encrypts our message
        connection.starttls()

        # Logging in
        connection.login(user=my_email, password=my_password)
        # Sending the message
        connection.sendmail(
            from_addr=my_email,
            to_addrs="crueser123@gmail.com",
            msg=f"Subject:{wish} {name}\n\n{msg}")


# Opening and checking the file
birthday_data = pd.read_csv("birthdays.csv")
email_column = birthday_data["email"]
name_column = birthday_data["name"]
year_column = birthday_data["year"]
month_column = birthday_data["month"]
day_column = birthday_data["day"]


now = dt.datetime.now()
year = now.year
month = now.month
day = now.day


# Random Number
random_no = random.randint(1, 3)

with open(f"letter_templates/letter_{random_no}.txt") as letter_format:
    letter = letter_format.read()

for i in birthday_data:
    pass