
import time
import threading
from threading import Thread

def sleepMe(i):
    print("Thread %i going to sleep for 5 seconds." % i)
    time.sleep(5)
    print("Thread %i is awake now." % i)

for i in range(10):
    t = Thread(target=sleepMe, args=(i, ))
    t.start()
    print(" count: %i." % threading.active_count())
