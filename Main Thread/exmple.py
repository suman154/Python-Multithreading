import threading
import time

def func(x):
   time.sleep(x)
   if not threading.current_thread() is threading.main_thread():
      print('threading.current_thread() not threading.main_thread()')

t = threading.Thread(target=func, args=(0.5,))
t.start()

print(threading.main_thread())
print("Main thread finished")