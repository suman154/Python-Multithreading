# Main Thread Behavior in Python


import threading
import time

def func(x):
   print('Current Thread Details:',threading.current_thread())
   for n in range(x):
      print('Internal Thread Running', n)
   print('Internal Thread Finished...')

t = threading.Thread(target=func, args=(6,))
t.start()

for i in range(3):
   print('Main Thread Running',i)
print("Main Thread Finished...")