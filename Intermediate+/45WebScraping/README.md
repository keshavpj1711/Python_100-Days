# Web Scraping 

Looking through the underlying HTML code to scrape the info that we want. 
There can be many reason do so:

- The website does not have an api.
- We want to analyze some stuff about the website.
- Just to monitor for certain changes or things in the website.
- Or just to get data for ourself.

In python this is done using **Beautiful Soup**


# Working of BS

## Basic Syntax and getting started

So first of all we want to read the contents of the html file to pass to make soup.
Making soup is basically making a BeautifulSoup() object with parameters

- markup: 
    - Here we will pass the contents read from html file
- parser
    - Here we will pass what kind of parsing we need to do.
    > For some html.parser might work but for some you might have to use lxml instead by importing the lxml module

