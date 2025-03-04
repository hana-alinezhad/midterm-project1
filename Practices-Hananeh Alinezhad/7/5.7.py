import threading
import time
exitFlag = 0

class Thread(threading.Thread):
    def __init__(self , threadID , name , counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print("starting" + self.name)
        print_time (self.name , self.counter , 5)
        print("Exiting" + self.name )
        
def print_time (threadName ,delay , counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s:%s" % (threadName ,time.ctime(time.time())))
        counter -= 1

thread1 = Thread(1,"Thread-1" , 1)
thread2 = Thread(2,"Thread-1" , 2)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("Exiting main Thread")