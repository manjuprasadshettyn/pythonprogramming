# Threads
from threading import Thread

class Mythread(Thread):
    def __init__(self):
        Thread.__init__(self,name="My Thread")
    def run(self):
        print("Hello,my name is %s" %self.getName())

process=Mythread()
process.setName("First Thread") #set the name of the thread
process.start()
if process.isAlive()==True:
    print("Thread is alive\n")
else:
    print("Thread is not alive")
