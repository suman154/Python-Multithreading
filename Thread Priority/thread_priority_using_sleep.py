# Setting the Thread Priority Using Sleep()

import threading
import time

class DummyThread(threading.Thread):
   def __init__(self, name, priority):
      threading.Thread.__init__(self)
      self.name = name
      self.priority = priority

   def run(self):
      name = self.name
      time.sleep(1.0 * self.priority)
      print(f"{name} thread with priority {self.priority} is running")

# Creating threads with different priorities
t1 = DummyThread(name='Thread-1', priority=4)
t2 = DummyThread(name='Thread-2', priority=1)

# Starting the threads
t1.start()
t2.start()

# Waiting for both threads to complete
t1.join()
t2.join()

print('All Threads are executed')