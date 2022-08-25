from scrape_page import scrape_book_infos
from export_csv import export_csv

while True:
    url = input("Please enter the url of the book:\n")
    if 'Exit' == url or 'exit' == url:
        break
    url.replace('\n','')
    book_infos = scrape_book_infos(url)
    export_csv(book_infos, 'books.csv')

#http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html