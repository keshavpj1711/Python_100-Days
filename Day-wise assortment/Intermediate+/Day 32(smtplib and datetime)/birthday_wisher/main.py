##################### Extra Hard Starting Project ######################

# 2. Check if today matches a birthday in the birthdays.csv


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import datetime
import pandas as pd


def send_msg():
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
            msg="Subject:Hello\n\nHi, this is my first msg using the SMTP module.")


# Opening and checking the file
birthday_data = pd.read_csv("birthdays.csv")
