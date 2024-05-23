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




