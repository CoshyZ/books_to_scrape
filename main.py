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