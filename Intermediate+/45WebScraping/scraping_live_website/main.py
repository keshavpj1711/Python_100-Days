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
# So first we got span tag which includes 
# the anchor tag in which we are intrested in
row_entry = soup.find_all("tr", class_="athing")
row_entry_upvotes = soup.select("tr .subtext")
# After that we loop through the text and 
# filter out the text from the first anchor tag 
# as it contains the titles for them
blogs_list = [] # Each element will be a dict with blog_name and blog_link as keys
for i in range(len(row_entry)):

    if row_entry_upvotes[i].find("span", class_="subline") == None:
        upvotes = "0 points"
    else:
        upvotes_entry = row_entry_upvotes[i].select_one(".subline .score")
        upvotes = upvotes_entry.getText()
    # print(upvotes) 

    span = row_entry[i].select(".title .titleline")
    # print(span)
    blog_text = span[0].find('a').getText()
    blog_link = span[0].find('a').get("href")
    blogs_list.append(
        {
            "blog_text": blog_text,
            "blog_link": blog_link,
            "blog_upvotes": upvotes,
        }
    )
    print(blogs_list[i])


for i in blogs_list:
    print(i)