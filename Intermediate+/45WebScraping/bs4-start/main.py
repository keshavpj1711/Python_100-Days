from bs4 import BeautifulSoup

# Opening our HTML file and reading it's contents to pass on to make soup
with open(file="website.html", mode="r") as html_file:
    contents = html_file.read()
# print(contents)

# Making of soup
soup = BeautifulSoup(contents, "html.parser")
# First we need to pass the contents and then, 
# Tell what kind of parsing we want html 
# For some websites html.parser might not work in that case 
# We might have to use lxml

# Getting title tag 
print(soup.title)
# Getting the string of title
print(soup.title.string)

# Getting hold of a single element
print(soup.select_one("p a")) 
print(soup.select_one("#name").string)
# This is basically selecting the elements like we do in CSS
# Also if you want to select more than one element we have to use 
print(soup.select(".heading"))
# [<h3 class="heading">Books and Teaching</h3>, <h3 class="heading">Other Pages</h3>]


