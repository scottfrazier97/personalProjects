import requests

url = "https://www.nytimes.com/"
r = requests.get(url)
r_html = r.text

from bs4 import BeautifulSoup

soup = BeautifulSoup(r_html)
title = soup.find('span','articletitle').string
print(title)