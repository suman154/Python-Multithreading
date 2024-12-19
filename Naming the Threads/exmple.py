# Naming the Threads in Python
from threading import Thread
import threading
from time import sleep


def my_function_1(arg):
    for i in range(arg):
        print("Child Thread 1 running", i)
        sleep(0.5)


# Create thread objects
thread1 = Thread(target=my_function_1, args=(5,))
thread2 = Thread(target=my_function_1, args=(3,))

print(threading.active_count())

# Start the first thread and wait for it to complete
thread1.start()
thread1.join()


# Start the second thread and wait for it to complete
thread2.start()
thread2.join()