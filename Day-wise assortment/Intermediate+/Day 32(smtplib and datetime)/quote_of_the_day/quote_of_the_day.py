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


# Checking for weekday to be Wednesday
# Getting the current info
now = dt.datetime.now()
# Getting today's weekday
week_day = now.weekday()

if week_day == 2:
    print("Today's Wednesday")
    todays_quote = get_quote()
else:
    pass
