import requests
import json
import time


url = [
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1609524000000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1608811200000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1608098400000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1606672800000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1605960000000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1605242700000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1604534400000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1603821600000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1603108800000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1602396000000',
]

def 함수(구멍):
    data = requests.get(구멍)
    딕셔너리 = json.loads(data.content)
    return 딕셔너리['data'][0]['Close']
for i in url :
    함수( i )
print('완료')

# from multiprocessing.dummy import Pool as ThreadPool

# pool = ThreadPool(4)
# result = pool.map(함수, url)
# pool.close()
# pool.join()
# print(result)



# dic = json.loads(data.content)
# for i in range(200) :
#     # print(dic['data'][i]['DT'])
#     times = dic['data'][i]['DT']
#     글자시간 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(times/1000))

#     print(글자시간)
#     print(dic['data'][i]['Close']) 



#print(dic['data'][1]['Close'])

#map함수 사용법
# 리스트 = [1,2,3,4]
# def 더해주셈(x) :
#     return x + 1
# r = map(더해주셈, 리스트)
# print(list(r))
