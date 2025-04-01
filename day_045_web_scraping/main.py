# Beautiful Soup Docs https://www.crummy.com/software/BeautifulSoup/bs4/doc/

# import lxml (sometimes needed if "html.parser" doesn't work)

from bs4 import BeautifulSoup

with open("website.html") as webstie:
    website_contents = webstie.read()

soup = BeautifulSoup(website_contents, "html.parser")

print(soup.title)