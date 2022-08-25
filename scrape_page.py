import requests
from bs4 import BeautifulSoup
import re
from img import download_image

def scrape_book_infos(url, name_category):
    #Récupérer le contenu de l'url
    try:
        response = requests.get(url)
    except IOError:
        print("Invalid URL")
        exit(1)

    #Le dictionnaire contenant les infos
    infos = {}
    infos['product_page_url'] = url

    #Methode Fancy pour récupérer les datas et les classer ensuite dans le dictionnaire
    if response.ok:
        response.encoding = 'UTF-8'
        soup = BeautifulSoup(response.text, 'html.parser')

        infos['universal_product_code'] = soup.find(text='UPC').findNext('td').text
        infos['title'] = soup.find('li', class_='active').text
        infos['price_including_tax'] = soup.find(text='Price (incl. tax)').findNext('td').text
        infos['price_excluding_tax'] = soup.find(text='Price (excl. tax)').findNext('td').text
        infos['number_available'] = [int(s) for s in re.findall(r'-?\d+\.?\d*', soup.find(text='Availability').findNext('td').text)]
        if soup.find(text='Product Description'):
            infos['product_description'] = soup.find(text='Product Description').findNext('p').text
        else:
            infos['product_description'] = ''
        infos['category'] = soup.find('a', text='Books').findNext('a').text
        infos['review_rating'] = soup.find('p', {'class' : 'star-rating'}).attrs['class'][1]
        infos['image_url'] = soup.find('div', class_='item active').findNext('img').attrs['src'].replace('../../','http://books.toscrape.com/')

        path = name_category + '/'
        #Télécharger l'image du livre
        download_image(infos['image_url'], path + infos['title'].replace(' ', '_').replace(',','').replace('.','').replace('#','').replace(':','').replace('/', ' '))
    else:
        print("L'url spécifié est incorrecte")
        exit(1)
    return infos