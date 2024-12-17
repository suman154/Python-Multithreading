import threading
import time

def print_name(name, *args):
    print(name, *args)


name = "Python Multithreading"


# Create and start a new thread
thread1 = threading.Thread(target=print_name, args=(name, 2, 3))
thread2 = threading.Thread(target=print_name, args=(name, 4, 5))

thread1.start()
thread2.start()


# Wait for the threads to finish
thread1.join()
thread2.join()

print("Exiting the main thread")