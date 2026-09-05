import requests
from bs4 import BeautifulSoup

class PriceTracer:
    def __init__(self,url):
        self.url = url
        self.user_agent={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.3'}
        self.response = requests.get(self.url,headers=self.user_agent)
        self.soup = BeautifulSoup(self.response.text,'lxml')

    def product_title(self):
        title=self.soup.find('span',{'id':'productTitle'})
        if title is not None:
            return title.text.strip()
        else:
            return 'tag not found'

    def product_price(self):
        price=self.soup.find('span',{'id':'priceblock_ourprice'})
        if price is not None:
            return price.text.strip()
        else:
            return 'cannot fetch'


device = PriceTracer(url='https://www.amazon.in/iPhone-16-128-GB-Ultramarine/dp/B0DGJ7TGDR/ref=sr_1_1_sspa?crid=1HHGZBPSLGG5T&dib=eyJ2IjoiMSJ9.pN1itJsmZpMcWidfLn9TQ-kHWpGpHYOjYiDw_1CVU7u7ZODuH2w-5Ek0eJZb3CWc-G9HTkxoNQBGyWeGG-H3uraloBLu0mLB8SgjUQBsSqbE1U2ZKBj6EtVD4EPhTi1eNJhUHQ91ORGr2UyAzWZ9VbplHatZqLWWykn7c9jY2eAsGOFPy5Auhe7QWm8cb50DjNowNzqtjIW8KQVv9bbqQHZuRPD4AJ8eoU9rCVJAz2E.jVOuuZpjL04eYPM7pZE-QjvIodiS_t5wCmm68XRwQvM&dib_tag=se&keywords=iphone&qid=1788609671&sprefix=iphone%2Caps%2C294&sr=8-1-spons&aref=GYsv72ZAxV&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1')

print(device.product_title())
print(device.product_price())

samsung = PriceTracer(url='https://www.amazon.in/Samsung-Moonlight-Storage-Upgrades-Lag-free/dp/B0G81TPT89/ref=sr_1_2?crid=1TXLGER5S859S&dib=eyJ2IjoiMSJ9.U1CJl4Z7HX-oiX2qJIfcphtMFBhePBU5lFTbOL7W7TADW2BQs71wekgdSeCPX_FF4hLxtwMAGEldcrVOZO9w14u9BIVi8tJbsLYCZwUDF_gSudxqlv1vQ-DUU04tqDldmhlXN6hXN23Ri5VzG26pAVm-JzBnS65ArNR5EUFyb1UJP4pPOgoAMbNOTFAKqsKdx8BL6RqAIOP4AQKHDmxxxrWQNO5yeinXE2ss4N0F7aE.qQo-2FpS9iovc72UNDeiZWWy5WIa2aAZzQ7uZKEwpfY&dib_tag=se&keywords=samsung&qid=1788610848&sprefix=samsung%2Caps%2C281&sr=8-2&th=1')
print(samsung.product_title())
print(samsung.product_price())