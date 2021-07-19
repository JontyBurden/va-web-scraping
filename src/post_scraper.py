from info import *
from bs4 import BeautifulSoup
import requests

URL = 'https://www.trademe.co.nz/a/marketplace/computers/peripherals/keyboards/search?search_string=mechanical%20keyboards&condition=used'

source = requests.get(URL).text

soup = BeautifulSoup(source, 'lxml')

item = soup.find('div', class_='o-card')

# link
link = item.find('a', class_='tm-marketplace-search-card__detail-section')['href']
# listing information
item_info = item.find('div', class_='tm-marketplace-search-card__details ng-star-inserted')

# listing title
title = item_info.find('div', class_='tm-marketplace-search-card__title')['aria-label']

# listing price
price = item_info.find('div', class_='tm-marketplace-search-card__footer-pricing-row')
price = price.find('div', class_='tm-marketplace-search-card__price-left')['aria-label']


# listing location
location = item_info.find('div', class_='tm-marketplace-search-card__location ng-star-inserted')['aria-label']

print(title, price, location, link)

