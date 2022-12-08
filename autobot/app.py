import requests
import json
import time

data = requests.get('https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinone&type=1h')
#print(data.content)

dic = json.loads(data.content)
for i in range(200) :
    # print(dic['data'][i]['DT'])
    times = dic['data'][i]['DT']
    글자시간 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(times/1000))

    print(글자시간)
    print(dic['data'][i]['Close']) 




#print(dic['data'][1]['Close'])