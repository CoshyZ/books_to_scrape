from scrape_page import scrape_book_infos
from export_csv import export_csv
from category import category

while True:
    url = input("Please enter the url of the category:\n")
    if 'Exit' == url or 'exit' == url:
        break
    url.replace('\n','')
    list_of_book = []
    list_of_book = category(url, list_of_book)
    for url_book in list_of_book:
        book_infos = scrape_book_infos(url_book)
        export_csv(book_infos, 'books.csv')
    break

#http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html
#url_category = "http://books.toscrape.com/catalogue/category/books/academic_40/index.html"
#Classic category : http://books.toscrape.com/catalogue/category/books/classics_6/index.html
#Nonfiction http://books.toscrape.com/catalogue/category/books/nonfiction_13/page-3.html
#Romance category http://books.toscrape.com/catalogue/category/books/romance_8/index.html