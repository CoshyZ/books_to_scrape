import requests

def download_image(url, filename):
    file = open(filename + '.jpg', 'wb')
    response = requests.get(url)
    file.write(response.content)
    file.close()