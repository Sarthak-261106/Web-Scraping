# print(ord('A'))
#
# print(ord('2'))
#
# print(ord('a'))
#
# print(ord('@'))

# import urllib.request, urllib.parse, urllib.error
#
# url = urllib.request.urlopen('file:///C:/Users/sarth/OneDrive/Desktop/index1.html')
#
# for line in url:
#     print(line.decode().strip())

import requests

url='https://en.wikipedia.org/wiki/Dog'

user={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36'
}

response = requests.get(url=url,headers=user)
print(dir(response))
print(response.request.headers)