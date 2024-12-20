# Creating a Daemon Thread in Python

import threading 
from time import sleep

# function to be executed in a new thread
def run():
   # get the current thread
   thread = threading.current_thread()
   # is it a daemon thread?
   print(f'Daemon thread: {thread.daemon}')

# Create a new thread and set it as daemon
thread = threading.Thread(target=run, daemon=True)

# start the thread
thread.start()

print('Is Main Thread is Daemon thread:', threading.current_thread().daemon)

# Block for a short time to allow the daemon thread to run
sleep(0.5)