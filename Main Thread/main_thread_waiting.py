# Main Thread Waiting for Other Threads

from threading import Thread
from time import sleep

def my_function_1():
   print("Worker 1 started")
   sleep(1)
   print("Worker 1 done")

def my_function_2(main_thread):
   print("Worker 2 waiting for Worker 1 to finish")
   main_thread.join()
   print("Worker 2 started")
   sleep(1)
   print("Worker 2 done")

worker1 = Thread(target=my_function_1)
worker2 = Thread(target=my_function_2, args=(worker1,))

worker1.start()
worker2.start()

for num in range(6):
   print("Main thread is still working on task", num)
   sleep(0.60)

worker1.join()
print("Main thread Completed")