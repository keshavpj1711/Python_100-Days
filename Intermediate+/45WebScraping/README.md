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

## Where to further improve?

Here is the documentation for bs4 which can be used to know more about syntax and stuff: 
[Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

To get more clear understanding of basics scraping a live website is a goods handson exp.
So for me the best way i learnt was by scraping different data from this news website: [LINK](https://news.ycombinator.com/news)

All of the work for scraping live website is avlbl on `./scraping_live_website/main.py`
The comments are enough to make you understand what's actually happening in the code.

# Should we scrape or not?

So reagarding the limitations of scraping a website you can visit:\
`https://domain_name_of_website.com/robots.txt`

This is basically the set of intrustions written by the website owners to tell you what you are actually allowed to do and what not.
This is actually something which you should check before scraping some website.