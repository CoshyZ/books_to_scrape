import requests
from bs4 import BeautifulSoup
import re

def category(url_category, list_of_book):
    #Récupérer le contenu de l'url
    try:
        response = requests.get(url_category)
    except IOError:
        print("Invalid URL")
        exit(1)

    #Methode Fancy pour récupérer les datas et les classer ensuite dans le dictionnaire
    if response.ok:
        response.encoding = 'UTF-8'
        soup = BeautifulSoup(response.text, 'html.parser')
        url_book = soup.findAll('article', class_='product_pod')
        for line in url_book:
            row = line.find('h3').find('a')
            list_of_book.append(row.attrs['href'].replace('../../../', 'http://books.toscrape.com/catalogue/'))
        if soup.find('li', class_='next'):
            number = len(url_category) - 1
            while number >= 0:
                if (url_category[number]) == '/':
                    break
                url_category = url_category.rstrip(url_category[-1])
                number = number - 1
            url_category = url_category + soup.find('li', class_='next').find('a').attrs['href']
            category(url_category, list_of_book)
    else:
        print("L'url spécifié est incorrecte")
        exit(1)

    return list_of_book