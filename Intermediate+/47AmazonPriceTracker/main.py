# Functionalities i want 
    # I want it to ask for the link of the products.
    # Then it should store that info from in some file by also scraping the name from it. 
    # It should ask for user input of alert price 
    # Next it should check all the listed stuff in the file for the target price if reached

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
    product_title = product_title_tag.getText()
    
    if input(
        f"Is this the product u are looking for\n{product_title}\nEnter y/n: "
        ) == "y":   
        # Getting price 
        listed_price_tag = soup.select_one("#centerCol span .a-price-whole")
        listed_price = listed_price_tag.getText()
        price_currency_tag = soup.select_one("#centerCol span .a-price-symbol")
        price_currency = price_currency_tag.getText()
        print(f"Price of the product is: {price_currency}{listed_price}")
    
    else: 
        print("ReEnter your product link")

main()