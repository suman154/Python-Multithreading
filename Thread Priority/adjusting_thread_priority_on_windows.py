# Adjusting Python Thread Priority on Windows

import threading
import ctypes
import time

# Constants for Windows API
w32 = ctypes.windll.kernel32
SET_THREAD = 0x20
PRIORITIZE_THE_THREAD = 1

class MyThread(threading.Thread):
   def __init__(self, start_event, name, iterations):
      super().__init__()
      self.start_event = start_event
      self.thread_id = None
      self.iterations = iterations
      self.name = name

   def set_priority(self, priority):
      if not self.is_alive():
         print('Cannot set priority for a non-active thread')
         return

      thread_handle = w32.OpenThread(SET_THREAD, False, self.thread_id)
      success = w32.SetThreadPriority(thread_handle, priority)
      w32.CloseHandle(thread_handle)
      if not success:
         print('Failed to set thread priority:', w32.GetLastError())

   def run(self):
      self.thread_id = w32.GetCurrentThreadId()
      self.start_event.wait()
      while self.iterations:
         print(f"{self.name} running")
         start_time = time.time()
         while time.time() - start_time < 1:
            pass
         self.iterations -= 1

# Create an event to synchronize thread start
start_event = threading.Event()

# Create threads
thread_normal = MyThread(start_event, name='normal', iterations=4)
thread_high = MyThread(start_event, name='high', iterations=4)

# Start the threads
thread_normal.start()
thread_high.start()

# Adjusting priority of 'high' thread
thread_high.set_priority(PRIORITIZE_THE_THREAD)

# Trigger thread execution
start_event.set()