
import threading
import time
import random

BUFFER_SIZE = 5
buffer = []
mutex = threading.Semaphore(1)  # Mutex for mutual exclusion
full = threading.Semaphore(0)   # Semaphore to track the number of full slots
empty = threading.Semaphore(BUFFER_SIZE)  # Semaphore to track the number of empty slots

def producer():
    global buffer
    while True:
        item = random.randint(1, 100)
        empty.acquire()  # Wait if the buffer is full
        mutex.acquire()  # Acquire the mutex to access the critical section
        buffer.append(item)
        print(f"Produced {item}. Buffer: {buffer}")
        mutex.release()  # Release the mutex
        full.release()   # Signal that a slot has been filled
        time.sleep(random.uniform(0.1, 0.5))

def consumer():
    global buffer
    while True:
        full.acquire()   # Wait if the buffer is empty
        mutex.acquire()  # Acquire the mutex to access the critical section
        item = buffer.pop(0)
        print(f"Consumed {item}. Buffer: {buffer}")
        mutex.release()  # Release the mutex
        empty.release()  # Signal that a slot has been emptied
        time.sleep(random.uniform(0.1, 0.5))

# Start producer and consumer threads
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

# Wait for the threads to finish (or interrupt with Ctrl+C)
try:
    producer_thread.join()
    consumer_thread.join()
except KeyboardInterrupt:
    print("Program interrupted.")
