import requests
from bs4 import BeautifulSoup

data = requests.get('https://s.search.naver.com/p/blog/search.naver?where=blog&sm=tab_pge&api_type=1&query=%EC%82%AC%EA%B3%BC&rev=44&start=1&dup_remove=1&post_blogurl=&post_blogurl_without=&nso=&nlu_query=%7B%22r_category%22%3A%2232+21%22%7D&dkey=0&source_query=&nx_search_query=%EC%82%AC%EA%B3%BC&spq=0&_callback=viewMoreContents')

soup = BeautifulSoup(data.text.replace('\\',''), 'html.parser')
리스트 = soup.select('a.api_txt_lines')
print(리스트[0]['href'])
print(리스트[1].text)
print(리스트[2].text)

data = requests.get('https://s.search.naver.com/p/blog/search.naver?where=blog&sm=tab_pge&api_type=1&query=%EC%82%AC%EA%B3%BC&rev=44&start=31&dup_remove=1&post_blogurl=&post_blogurl_without=&nso=&nlu_query=%7B%22r_category%22%3A%2232+21%22%7D&dkey=0&source_query=&nx_search_query=%EC%82%AC%EA%B3%BC&spq=0&_callback=viewMoreContents')