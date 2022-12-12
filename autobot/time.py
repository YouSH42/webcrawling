import time

a = time.time()
time.ctime(a)

a = time.localtime()
a = time.strftime('%y year %m month',a)
print(a)

import datetime
a = datetime.datetime(2022, 10, 1)
b = datetime.datetime.now()
print(b)
print(a)