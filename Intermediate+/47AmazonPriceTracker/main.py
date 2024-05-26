# Functionalities i want 
# I want it to ask for the link of the products.
# Then it should store that info from in some file by also scraping the name from it.
# It should ask for user input of alert price
# Next it should check all the listed stuff in the file for the target price if reached

import bs4
import requests
import csv
import sys
from bs4 import BeautifulSoup

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
    if product_title_tag is not None:
        product_title = product_title_tag.getText()
    else:
        # Handle the case where the tag is not found
        print("Product title tag not found")


    # Pretiffying the product title below
    if input(
            f"Is this the product u are looking for\n{product_title.split(", ")[0].lstrip()}\nEnter y/n: "
    ) == "y":

        # Getting price 

        # Getting the whole number
        listed_price_tag = soup.select_one("#centerCol span .a-price-whole")
        listed_price = ""
        if listed_price_tag is not None:
            listed_price = listed_price_tag.getText()

        # In case of foriegn currency decimal is also imp
        decimal_for_foreign = soup.select_one("#centerCol span .a-price-fraction")

        # Getting currency which is to display
        price_currency_tag = soup.select_one("#centerCol span .a-price-symbol")
        price_currency = ""
        if price_currency_tag is not None:
            price_currency = price_currency_tag.getText()

        if decimal_for_foreign is None:
            print(f"Price of the product is: {price_currency}{listed_price}")
        else:
            print(f"Price of the product is: {price_currency}{listed_price}{decimal_for_foreign.getText()}")

    else:
        print("ReEnter your product link")


main()
