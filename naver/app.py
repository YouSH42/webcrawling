import requests
from bs4 import BeautifulSoup

d = requests.get('https://finance.naver.com/item/sise.naver?code=005930')

soup = BeautifulSoup(d.content,'html.parser')
print(soup.find_all('span', class_="tah")[5].text)

