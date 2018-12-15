import time
from threading import Thread

def sleepMe(i):
    print("Thread %i gonna to sleep for 8 seconds." % i)
    time.sleep(8)
    print("Thread %i woke up." % i)

for i in range(10):
    th = Thread(target=sleepMe, args=(i, ))
    th.start()
