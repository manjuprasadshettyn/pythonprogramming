# Two threads
from threading import Thread,Lock
import time

class TwoThread(Thread):
    def __init__(self,ThreadId,name,counter):
        Thread.__init__(self)
        self.ThreadId=ThreadId
        self.name=name
        self.counter=counter

            
    def run(self):
        print("\nStarting" + self.name)
        threadLock.acquire()
        while self.counter:
            time.sleep(1)
            print("%s:%s" %(self.name,time.ctime(time.time())))
            self.counter-=1
        threadLock.release()
        print("\nExiting" +self.name)

threadLock=Lock()
threads=[]

thread1=TwoThread(1,"Thread-1",10)
thread2=TwoThread(2,"Thread-2",10)
thread1.start()
thread2.start()
threads.append(thread1)
threads.append(thread2)
for t in threads:
    t.join()
print("\nExiting main thread")
