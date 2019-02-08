import requests
from bs4 import BeautifulSoup
import webbrowser

url = 'https://en.wikipedia.org/wiki/Gustav_Klimt'


page = requests.get(url)
page.raise_for_status()

soup = BeautifulSoup(page.text, 'html.parser')

gallery = soup.find_all('li', attrs={'class': 'gallerybox'})

f = open('klimt_paintings.txt', 'w+')
records = []
for picture in gallery:
    title = picture.find('p').text
    image_url = picture.find('a').get('href')
    image_url = 'https://en.wikipedia.org' + image_url
    print(image_url)
    #webbrowser.open(image_url)
    record = title +' ' + image_url
    records.append(record)
i = 1
for record in records:
    f.write(str(i) + ". " +  record + "\n\n")
    i += 1
