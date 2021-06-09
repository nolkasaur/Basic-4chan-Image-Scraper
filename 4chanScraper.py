import requests
from bs4 import BeautifulSoup
import urllib.request
import os

oURL = 'https://boards.4chan.org/b/'

print("Downloading media to Desktop/Scraped Images/...")

def do_stuff(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id='delform')
    elems = results.find_all('div', class_='thread')

    for elem in elems:
        thread_id = elem.find('a', class_='fileThumb')
        image_url = thread_id['href'][2:]
        image_name = aux = thread_id['href'].partition("/b/")[2]
        if not os.path.exists(os.path.join(os.path.join(os.environ['USERPROFILE']), "Desktop\\Scraped Images\\")):
            os.mkdir(os.path.join(os.path.join(os.environ['USERPROFILE']), "Desktop\\Scraped Images\\"))
        urllib.request.urlretrieve("https://" + image_url, os.path.join(os.path.join(os.environ['USERPROFILE']), "Desktop\\Scraped Images\\" + image_name))

print("Page 1...")
do_stuff(oURL)

for x in range(2, 11):
    print("Page {}...".format(x))
    do_stuff(oURL + str(x))

print("Done!")
