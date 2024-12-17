import threading
import time

# Create a semaphore object
sem = threading.Semaphore(0)

threads = []  # Add this to define the threads list

def worker():
    with sem:
        print('{} has started working'.format(threading.current_thread().name))
        time.sleep(2)
        print('{} has finished working'.format(threading.current_thread().name))


# Create thread objects
for i in range(5):
    t = threading.Thread(target=worker, name='Thread-{}'.format(i+1))
    threads.append(t)
    print('Thread-{} Created'.format(i+1))
    t.start()

# Wait for threads to complete
for t in threads:
    t.join()  # Correct indentation here
    print('{} has terminated'.format(t.name))

print('Main Thread Finished...')
