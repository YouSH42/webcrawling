import requests
from bs4 import BeautifulSoup
# import urllib.request  이미지파일 크롤링


def now_Val(구멍) :
    data = requests.get(f'https://finance.naver.com/item/sise.naver?code={구멍}')
    soup = BeautifulSoup(data.content,'html.parser')
    print(soup.find_all('strong', id = "_nowVal")[0].text)
    print(soup.find_all('span', id = "_quant")[0].text)
    return soup.find_all('strong', id = "_nowVal")[0].text

now_Val('005930')
now_Val('066570')

# f = open('a.csv','w')
# f.write(now_Val('005930'))
# f.write(now_Val('066570'))
# f.close()


# 이미지파일 크롤링
# imige = soup.select('#img_chart_area')[0]
# print(imige['src'])
# urllib.request.urlretrieve(imige['src'], 'sise')