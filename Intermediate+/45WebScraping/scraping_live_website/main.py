# Here we will scrape a live website
# Website we will be scraping: https://news.ycombinator.com/news

from bs4 import BeautifulSoup
import requests 

response = requests.get("https://news.ycombinator.com/news")

html_data = response.text
soup = BeautifulSoup(html_data)
html_data = soup.prettify()

