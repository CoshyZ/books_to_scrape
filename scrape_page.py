# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re
import sys

#Url du site web
product_page_url = "http://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html"

#Récupérer le contenu de l'url
response = requests.get(product_page_url)

infos = {}
infos['product_page_url'] = product_page_url

if response.ok:
    response.encoding = 'UTF-8'
    soup = BeautifulSoup(response.text, 'html.parser')
    lines = soup.find_all('tr')
    for row in lines:
        if row.find('th', text = 'UPC'):
            infos['UPC'] = row.find('td').text
        if row.find('th', text = 'Price (excl. tax)'):
            infos['price_excluding_tax'] = row.find('td').text
        if row.find('th', text = 'Price (incl. tax)'):
            infos['price_including_tax'] = row.find('td').text
        if row.find('th', text = 'Availability'):
            infos['number_available'] = [int(s) for s in re.findall(r'-?\d+\.?\d*', row.find('td').text)]

print(infos)