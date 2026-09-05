import requests
from bs4 import BeautifulSoup



def Extract(url):
    response = requests.get(url=url).content
    soup = BeautifulSoup(response, 'lxml')
    tag = soup.td
    print(tag)

Extract(url='https://en.wikipedia.org/wiki/Wikipedia')