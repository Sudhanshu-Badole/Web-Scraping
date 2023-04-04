import requests
from bs4 import BeautifulSoup
import pandas as pd
url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops'

r = requests.get(url)
#print(r)  #if output is response 200 that means you can get html data

soup = BeautifulSoup(r.text, "lxml")
#print(soup)
#boxes  = soup.find_all("div",class_ = "col-sm-4 col-lg-4 col-md-4")
#print(len(boxes))

name = soup.find_all("a", class_="title")
product = []
for i in name:
    product.append(i.text)



amount = []
price = soup.find_all("h4", class_ = "pull-right price")
for j in price:
    amount.append(j.text)

df = pd.DataFrame({'Name':product,'Price':amount})
print(df)