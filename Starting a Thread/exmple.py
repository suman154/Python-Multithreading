from threading import Thread
from time import sleep


def my_function(arg):
    for i in range(arg):
        sleep(1)
        print('This is a function')

thread = Thread(target=my_function, args=(10,))
thread.start()
print("Thread finished...exiting")
