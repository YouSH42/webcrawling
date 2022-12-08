import requests
from bs4 import BeautifulSoup

def value1(ans) :
    data = requests.get(f'https://search.shopping.naver.com/search/all?where=all&frm=NVSCTAB&query={ans}')
    soup = BeautifulSoup(data.content, 'html.parser')
    f = open(f'{ans}.txt','w')
    for i in range(5) :
        # print(soup.select('span.price_num__S2p_v')[i].text)
        f.write(soup.select('span.price_num__S2p_v')[i].text + '\n')
    f.close()

value1('귤')
