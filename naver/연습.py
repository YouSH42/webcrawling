import requests
from bs4 import BeautifulSoup

def now_Val(구멍) :
    data = requests.get(f'https://finance.naver.com/item/sise.naver?code={구멍}')
    soup = BeautifulSoup(data.content,'html.parser')
    # print(soup.find_all('strong', id = "_nowVal")[0].text)
    return soup.find_all('strong', id = "_nowVal")[0].text

종목들 = ['005930', '066575', '005380', '035720', '034220', '003490']
f = open('prac.txt','w')

for i in 종목들 :
    f.write(now_Val(i) + '\n')
f.close()