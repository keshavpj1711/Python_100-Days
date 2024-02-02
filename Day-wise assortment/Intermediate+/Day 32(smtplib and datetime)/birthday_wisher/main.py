import smtplib
import datetime as dt
import pandas as pd
import random


def send_msg(wish, msg, email):
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
            to_addrs=f"{email}",
            msg=f"Subject:{wish}\n\n{msg}")


# Opening and checking the file
birthday_data = pd.read_csv("birthdays.csv")

# Getting today's info
now = dt.datetime.now()
year = now.year
month = now.month
day = now.day

# Iterating through rows in pandas
# Read the CSV file into a DataFrame
# df = pd.read_csv("your_file.csv")
# for index, row in df.iterrows():
#     # Access row values by column name
#     name = row['Name']
#     age = row['Age']
#     # Process the row data as needed
#     print(f"Name: {name}, Age: {age}")

for index, row in birthday_data.iterrows():

    # Random Number
    random_no = random.randint(1, 3)

    # Getting a random letter format
    with open(f"letter_templates/letter_{random_no}.txt") as letter_format:
        letter = letter_format.read()

    # Checking if today is a birthday or not
    if [day, month, year] == [row["day"], row["month"], row["year"]]:
        # Getting the name on the letter
        name = row["name"]
        letter = letter.replace("[NAME]", name)
        # print(letter)

        send_msg("Happy Birthday", letter, row["email"])

