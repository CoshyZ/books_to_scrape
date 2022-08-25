import csv
def export_csv(book_infos, file):
    #Déclaration de l'en-tête CSV
    header = ['product_page_url', 'universal_product_code', 'title', \
              'price_including_tax', 'price_excluding_tax', 'number_available', \
              'product_description', 'category', 'review_rating', 'image_url']

    try:
        with open(file):
            # Ouverture du fichier et ajout des informations du livre
            with open(file, 'a') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=header, delimiter=',')
                writer.writerow(book_infos)
    except IOError:
        # Création du fichier et écriture de l'en-tête s'il n'existait pas
        try:
            with open(file, 'w') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames = header, delimiter = ',')
                writer.writeheader()
                writer.writerow(book_infos)
        except IOError:
            print("I/O error")