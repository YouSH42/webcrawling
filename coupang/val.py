import requests
from bs4 import BeautifulSoup

def value1(ans) :
    data = requests.get(f'https://search.shopping.naver.com/search/all?frm=NVSHATC&origQuery={ans}&pagingIndex=2&pagingSize=20&productSet=total&query=%EC%82%AC%EA%B3%BC&sort=rel&timestamp=&viewType=list')
    soup = BeautifulSoup(data.content, 'html.parser')
    f = open('과일.txt','w')
    for i in range(5) :
        # print(soup.select('span.price_num__S2p_v')[i].text)
        f.write(soup.select('span.price_num__S2p_v')[i].text + '\n')
    f.close()

value1('사과')
