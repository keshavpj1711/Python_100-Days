# Here we will scrape a live website
# Website we will be scraping: https://news.ycombinator.com/news

from bs4 import BeautifulSoup
import requests 

response = requests.get("https://news.ycombinator.com/news")

html_data = response.text
soup = BeautifulSoup(html_data, "html.parser")
# html_data = soup.prettify()

# Getting the titles and links of all the top articles

# Getting hold of titles
titles = soup.select(".titleline a")
for i in titles:
    print(i)
