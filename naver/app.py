import requests
from bs4 import BeautifulSoup

d = requests.get('https://finance.naver.com/item/sise.naver?code=067160')

soup = BeautifulSoup(d.content,'html.parser')
print(soup.find_all('strong', id="_nowVal")[0].text)

