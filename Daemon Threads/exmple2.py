# Managing the Daemon Thread Attribute

from time import sleep
from threading import current_thread, Thread

# function to be executed in a new thread
def run():
    # get the current thread
    thread = current_thread()
    # is it a daemon thread?
    print(f'Daemon thread: {thread.daemon}')

# create a new thread and set it as a daemon
thread = Thread(target=run, daemon=True)

# start the new thread
thread.start()

# block for 0.5 seconds to allow the daemon thread to run
sleep(0.5)
