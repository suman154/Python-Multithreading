import _thread
import time


def print_time(name, *args):
    print(name, args)


name = "Python Multithreading"
_thread.start_new_thread(print_time, (name, 2, 3))
_thread.start_new_thread(print_time, (name, 4, 5))

time.sleep(5)