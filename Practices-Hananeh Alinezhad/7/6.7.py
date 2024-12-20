import time
from threading import Thread
def sleeper(i):
    print("thread % d sleeps for 5seconds" % i)
    time.sleep(5)
    print("thread %d woke up " % i)
for i in range (10):
    t = Thread (target=sleeper,args=(i,))
    t.start()
    