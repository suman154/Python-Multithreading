import threading
import queue
import time

exitFlag = 0


class MyThread(threading.Thread):
    def __init__(self, threadID, name, q, lock):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
        self.lock = lock

    def run(self):
        print("Starting " + self.name)
        self.process_data()
        print("Exiting " + self.name)

    def process_data(self):
        global exitFlag
        while not exitFlag:
            self.lock.acquire()
            if not self.q.empty():
                data = self.q.get()
                self.lock.release()
                print(f"{self.name} processing {data}")
                time.sleep(1)  # Simulate work
            else:
                self.lock.release()
                time.sleep(1)  # Avoid busy looping


# Main thread logic
threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1

# Create new threads
for tName in threadList:
    thread = MyThread(threadID, tName, workQueue, queueLock)
    thread.start()
    threads.append(thread)
    threadID += 1

# Fill the queue
queueLock.acquire()
for word in nameList:
    workQueue.put(word)  # Fixed from 'work' to 'word'
queueLock.release()

# Wait for the queue to empty
while not workQueue.empty():
    pass

# Notify threads it's time to exit
exitFlag = 1

# Wait for all threads to complete
for t in threads:
    t.join()
print("Exiting Main Thread")
