# Objective: send a motivational quote via email on the current
# weekday (you can change it to Monday afterward)
# Hints
# 1. Use the datetime module to obtain the current day of the week.
# 2. Open the quotes.txt file and obtain a list of quotes.
# 3. Use the random module to pick a random quote from your list of quotes.
# 4. Use the smtplib to send the email to yourself.

import datetime as dt
import random
import smtplib


# Here we will be writing a function that returns a random quote from quote.txt
def get_quote():
    with open("quotes.txt", "r") as quotes:
        content = quotes.readlines()
        # Getting a random line from quotes.txt
        random_quote = content[random.randint(0, 101)]

        return random_quote


# Defining a function to send sms with msg as input
def send_quote(msg):
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
            msg=f"Subject:Monday Starters\n\n{msg}")


# Checking for weekday to be Wednesday
# Getting the current info
now = dt.datetime.now()
# Getting today's weekday
week_day = now.weekday()

if week_day == 0:
    todays_quote = get_quote()
    send_quote(todays_quote)
else:
    pass
