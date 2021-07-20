from info import *
from bs4 import BeautifulSoup
import requests, csv

URL = 'https://www.trademe.co.nz/a/marketplace/computers/peripherals/keyboards/search?search_string=mechanical%20keyboards&condition=used'

source = requests.get(URL).text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('trademeListings.csv', 'w', newline='')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['listing title', 'price', 'location', 'link'])

for item in soup.find_all('tg-col', class_='l-col l-col--has-flex-contents ng-star-inserted'):

    try:

        # link
        link = item.find('a', class_='tm-marketplace-search-card__detail-section')['href']
        listing_link = f'https://www.trademe.co.nz/a/{link}'

        # listing title
        title = item.find('div', class_='tm-marketplace-search-card__title')['aria-label']

        # listing price
        price = item.find('div', class_='tm-marketplace-search-card__footer-pricing-row')
        price = price.find('div', class_='tm-marketplace-search-card__price-left')['aria-label']

        # listing location
        location = item.find('div', class_='tm-marketplace-search-card__location ng-star-inserted')['aria-label']
        
    except Exception as e:
        title = None
        price = None
        location = None

    print(title)
    print(price)
    print(location)
    print(listing_link)

    print()

    csv_writer.writerow([title, price, location, listing_link])

csv_file.close()
