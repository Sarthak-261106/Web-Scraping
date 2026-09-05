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

url='https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Comparison_of_a_wolf_and_a_pug.png/500px-Comparison_of_a_wolf_and_a_pug.png?utm_source=en.wikipedia.org&utm_campaign=parser&utm_content=thumbnail'

user={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36'
}

response = requests.get(url=url,headers=user)
# print(dir(response))

#content
pic=response.content

f=open('Comparison_of_a_wolf_and_a_pug.png','wb')
f.write(pic)
f.close()
