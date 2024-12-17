import threading

def func(x):
   print('Current Thread Details:', threading.current_thread())
   for n in range(x):
      print('{} Running'.format(threading.current_thread().name), n)
   print('Internal Thread Finished...')

# Create thread objects
t1 = threading.Thread(target=func, args=(2,))
t2 = threading.Thread(target=func, args=(3,))

# Start the threads
print('Thread State: CREATED')
t1.start()
t2.start()

# Wait for threads to complete
t1.join()
t2.join()
print('Threads State: FINISHED')

# Simulate main thread work
for i in range(3):
   print('Main Thread Running', i)

print("Main Thread Finished...")