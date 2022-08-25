from scrape_page import scrape_book_infos
from export_csv import export_csv
from category import *

list_of_category = []
list_of_category = get_all_category("http://books.toscrape.com/index.html", list_of_category)

for line in list_of_category:
    list_of_book = []
    list_of_book = category(line, list_of_book)
    for url_book in list_of_book:
        book_infos = scrape_book_infos(url_book)
        export_csv(book_infos, category_name(line) + '.csv')

#http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html
#url_category = "http://books.toscrape.com/catalogue/category/books/academic_40/index.html"
#Classic category : http://books.toscrape.com/catalogue/category/books/classics_6/index.html
#Nonfiction http://books.toscrape.com/catalogue/category/books/nonfiction_13/page-3.html
#Romance category http://books.toscrape.com/catalogue/category/books/romance_8/index.html