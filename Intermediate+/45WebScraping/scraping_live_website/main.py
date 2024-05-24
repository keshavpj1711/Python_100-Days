# Here we will scrape a live website
# Website we will be scraping: https://news.ycombinator.com/news

from bs4 import BeautifulSoup
import requests 

# So requests module is not just for getting api calls huhu!!
response = requests.get("https://news.ycombinator.com/news")

# Getting all the html data in form of text
html_data = response.text
soup = BeautifulSoup(html_data, "html.parser")
# html_data = soup.prettify()


# Getting the titles and links of all the top articles
# Along with the number of upvotes it has

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

    # Basically we are checking the presence of subline class span tag 
    # Which is actually absent if no one has upvoted the blog
    if row_entry_upvotes[i].find("span", class_="subline") == None:
        upvotes = "0 points" # Setting upvotes to zero for this
    else:
        upvotes_entry = row_entry_upvotes[i].select_one(".subline .score")
        upvotes = upvotes_entry.getText() # Getting the upvotes from the span tag in the form of text
    # print(upvotes) 

    # Getting hold of the final span element containing the blog titles with links in first anchor tag
    span = row_entry[i].select(".title .titleline")
    # print(span)
    blog_text = span[0].find('a').getText() # Since the info is present in the first anchor tag itself
    blog_link = span[0].find('a').get("href") # Getting the links from href attribute

    # Making a list to append the data in form of dictionary
    blogs_list.append(
        {
            "blog_text": blog_text,
            "blog_link": blog_link,
            "blog_upvotes": upvotes,
        }
    )
    # print(blogs_list[i])

# Printing out the outputs to confirm if its working
for i in blogs_list:
    print(i)