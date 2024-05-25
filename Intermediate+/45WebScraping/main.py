# To scrape top 100 movies from https://www.empireonline.com/movies/features/best-movies-2/

from os import write
from types import resolve_bases
from bs4 import BeautifulSoup
import requests

# Getting response and html data
response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
response.raise_for_status()
# Html data 
html_data = response.text

# Making soup 
soup = BeautifulSoup(html_data, "html.parser")

# Getting the movie titles
movie_title_tags = soup.find_all("h3", class_="listicleItem_listicle-item__title__BfenH")

with open("top100_movie_list.txt", "w") as movie_list:
    for i in range(1, len(movie_title_tags)+1):
        movie_list.write(f"{movie_title_tags[-i].getText()}\n")
    