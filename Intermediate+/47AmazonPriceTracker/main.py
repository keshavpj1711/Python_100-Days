# Functionalities i want 
# I want it to ask for the link of the products.
# Then it should store that info from in some file by also scraping the name from it.
# It should ask for user input of alert price
# Next it should check all the listed stuff in the file for the target price if reached

from typing import final
import bs4
import requests
import csv
import os
from bs4 import BeautifulSoup
import smtplib

SENDER_EMAIL = "test.user.python0520@gmail.com"
RECIEVER_EMAIL = "cruser123@gmail.com"

HEADER = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:126.0) Gecko/20100101 Firefox/126.0",
    "Accept-Language": "en-US,en;q=0.5",
}


def main():
    # Taking inputs
    product_link = input("Enter your product link: ")

    # Getting HTML data for page 
    response = requests.get(product_link, headers=HEADER)
    html_data = response.text

    # Making soup
    soup = BeautifulSoup(html_data, "html.parser")

    # Getting product name
    product_title_tag = soup.select_one("#productTitle")
    product_title = ""
    product_title_stripped = ""
    if product_title_tag is not None:
        product_title = product_title_tag.getText()
        product_title_stripped = product_title.split(", ")[0].lstrip()
    else:
        # Handle the case where the tag is not found
        print("Product title tag not found")

    # Pretiffying the product title below
    if input(
            f"Is this the product u are looking for\n{product_title_stripped}\nEnter y/n: "
            ) == "y":

        # Getting price 

        # Getting the whole number
        listed_price_tag = soup.select_one("#centerCol span .a-price-whole")
        listed_price = ""
        if listed_price_tag is not None:
            listed_price = listed_price_tag.getText()

        # In case of foriegn currency decimal is also imp
        decimal_for_foreign = soup.select_one("#centerCol span .a-price-fraction")

        final_price = 0

        # Getting currency which is to display
        price_currency_tag = soup.select_one("#centerCol span .a-price-symbol")
        price_currency = ""
        if price_currency_tag is not None:
            price_currency = price_currency_tag.getText()

        if decimal_for_foreign is None:
            final_price = float(listed_price.replace(",", ""))
            print(f"Price of the product is: {price_currency}{final_price}")
        else:
            final_price = float((listed_price+decimal_for_foreign.getText()).replace(",", ""))
            print(f"Price of the product is: {price_currency}{final_price}")

        target_price = float(input("Enter a target price to trigger Deal Alert!!: "))
        
        if final_price < target_price: 
            notify_user(product_title_stripped, product_link)

    else:
        print("ReEnter your product link")

    

        


def notify_user(product, product_link):
    sender_email = SENDER_EMAIL
    reciever_email = RECIEVER_EMAIL

    app_password = os.environ.get("app_password")

    # message that needs to be sent
    my_message = f"Subject: Deal Alert for Product \n\n{product}\nVisit Link: {product_link}"

    # Setting up smtp to send message 
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(user=f"{sender_email}", password=f"{app_password}")
        server.sendmail(
            msg=my_message, 
            from_addr=sender_email, 
            to_addrs=reciever_email)

    print("Message succesfuly sent")


main()
