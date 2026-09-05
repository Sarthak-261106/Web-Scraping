import requests

url = 'file:///C:/Users/sarth/OneDrive/Desktop/index1.html'

response = requests.get(url=url)

print(response.text)

