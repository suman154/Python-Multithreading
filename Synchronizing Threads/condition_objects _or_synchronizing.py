# Condition Objects for Synchronizing Python Threads
import threading

counter = 0  

# Consumer function
def consumer(cv):
   global counter
   with cv:
      print("Consumer is waiting")
      cv.wait()  # Wait until notified by increment
      print("Consumer has been notified. Current Counter value:", counter)

# increment function
def increment(cv, N):
   global counter
   with cv:
      print("increment is producing items")
      for i in range(1, N + 1):
         counter += i  # Increment counter by i
        
      # Notify the consumer 
      cv.notify()  
      print("Increment has finished")

# Create a Condition object
cv = threading.Condition()

# Create and start threads
consumer_thread = threading.Thread(target=consumer, args=[cv])
increment_thread = threading.Thread(target=increment, args=[cv, 5])

consumer_thread.start()
increment_thread.start()

consumer_thread.join()
increment_thread.join()

print("The Final Counter Value:", counter)