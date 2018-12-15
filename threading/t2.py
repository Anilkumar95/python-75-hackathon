import time
from threading import Thread

def insane(i):
    print ("thread %d sleeping for 7 seconds" % i)
    time.sleep(7)
    print ("thread %d gonna ke up "% i)

for i in range(10):
    t = Thread(target=insane, args=(i,))
    t.start()
