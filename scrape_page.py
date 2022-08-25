import requests
from bs4 import BeautifulSoup
import re

#Url du site web
#product_page_url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"

def scrape_book_infos(url):
    #Récupérer le contenu de l'url
    response = requests.get(url)
    #Le dictionnaire contenant les infos
    infos = {}
    infos['product_page_url'] = url

    #Methode Fancy pour récupérer les datas et les classer ensuite dans le dictionnaire
    if response.ok:
        response.encoding = 'UTF-8'
        soup = BeautifulSoup(response.text, 'html.parser')

        infos['UPC'] = soup.find(text='UPC').findNext('td').text
        infos['title'] = soup.find('li', class_='active').text
        infos['price_including_tax'] = soup.find(text='Price (incl. tax)').findNext('td').text
        infos['price_excluding_tax'] = soup.find(text='Price (excl. tax)').findNext('td').text
        infos['number_available'] = [int(s) for s in re.findall(r'-?\d+\.?\d*', soup.find(text='Availability').findNext('td').text)]
        infos['product_description'] = soup.find(text='Product Description').findNext('p').text
        infos['category'] = soup.find('a', text='Books').findNext('a').text
        infos['review_rating'] = soup.find('p', {'class' : 'star-rating'}).attrs['class'][1]
        infos['image_url'] = soup.find('img').attrs['src'].replace('../../','http://books.toscrape.com/')
    else:
        print("L'url spécifié est incorrecte")
        exit(1)
    return infos


book_infos = scrape_book_infos("http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html")
print(book_infos)