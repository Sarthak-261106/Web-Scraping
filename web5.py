# import requests
# from bs4 import BeautifulSoup
#
#
#
# def Extract(url):
#     response = requests.get(url=url).content
#     soup = BeautifulSoup(response, 'lxml')
#     tag = soup.find('id',{'id':'no-right'})
#     h=tag.find('h2')
#     print(h)
#
# Extract(url='https://en.wikipedia.org/wiki/Wikipedia')
#
# import requests
# from bs4 import BeautifulSoup
# import csv
#
# def Extract(url):
#     response = requests.get(url).content
#
#     soup = BeautifulSoup(response, features='lxml')
#
#     tag = soup.find(id='no-right')
#     h = tag.find_all('h2')
#     content = [span.text for span in h]
#
#     with open('wiki.csv','w') as csvfile:
#         csv_write = csv.writer(csvfile)
#         csv_write.writerow(content)
#
#
# Extract(url='https://en.wikipedia.org/wiki/Main_Page')

import requests
from bs4 import BeautifulSoup
import csv


def Extract(url):
    response = requests.get(url=url).content

    soup = BeautifulSoup(response, 'lxml')

    h = soup.find_all('h2')

    content = [span.text for span in h]

    with open('wiki.csv', 'w', ) as csvfile:
        csv_writer = csv.writer(csvfile)

        csv_writer.writerow(content)


Extract(url='https://en.wikipedia.org/wiki/Main_Page')