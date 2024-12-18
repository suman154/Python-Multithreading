import threading
import time

exitFlag = 0

class MyThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        super().__init__()  # Call the parent class initializer
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("Starting " + self.name)
        self.print_time(self.name, self.counter, 5)
        print("Exiting " + self.name)

    @staticmethod
    def print_time(threadName, delay, counter):
        while counter:
            if exitFlag:
                break
            time.sleep(delay)
            print("%s: %s" % (threadName, time.ctime(time.time())))
            counter -= 1


# Create new threads
thread1 = MyThread(1, "Thread-1", 1)
thread2 = MyThread(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()

# Wait for all threads to complete
thread1.join()
thread2.join()

print("Exiting Main Thread")
