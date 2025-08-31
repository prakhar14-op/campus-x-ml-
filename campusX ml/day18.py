# web_scraping
import pandas as pd
import requests
from bs4 import BeautifulSoup
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}
webpage=requests.get('https://www.ambitionbox.com/list-of-companies?campaign=desktop_nav&page=1',header=headers)

soup=BeautifulSoup(webpage)
print(soup.prettify())
