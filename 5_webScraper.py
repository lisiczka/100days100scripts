# A simple way to get some data from Facebook without using it's paid API.
# "Requests" and "BeutifulSoup" are the libraries made for such tasks.
# Data mining and it's autoamtion is fun and challenging the same time.
# Websites like FB try to prevent such actions by randomizing HTML tags.
# Here come regular expressions that help us selecting the desireable content.

import requests
import re
from bs4 import BeautifulSoup

# FB event we are interested in:
r = requests.get("https://www.facebook.com/events/382289025896960/")
soup = BeautifulSoup(r.text, "html.parser")


# getting event name 
name = soup.find("h1", id="seo_h1_tag").contents
full_name = ((str(name))[2:-2])
print("Event name:\n", full_name)

# getting event date
date = soup.find("div", id="title_subtitle").contents
event_date = (str(date[0])[18:44])
print("Event date:\n", event_date)
