# print(ord('A'))
#
# print(ord('2'))
#
# print(ord('a'))
#
# print(ord('@'))

import urllib.request, urllib.parse, urllib.error

url = urllib.request.urlopen('file:///C:/Users/sarth/OneDrive/Desktop/index1.html')

for line in url:
    print(line.decode().strip())
