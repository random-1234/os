
import multiprocessing

def producer(shared_value):
    for i in range(1, 6):
        shared_value.value = i
        print(f"Produced: {i}")
        multiprocessing.Event().set()  # Signal the consumer that a new value is produced
        multiprocessing.Event().wait()  # Wait for the consumer to acknowledge

def consumer(shared_value):
    for _ in range(1, 6):
        multiprocessing.Event().wait()  # Wait for the producer to signal a new value
        print(f"Consumed: {shared_value.value}")
        multiprocessing.Event().set()  # Signal the producer that the value is consumed


shared_value = multiprocessing.Value('i', 0)  # 'i' represents the type (integer)

producer_process = multiprocessing.Process(target=producer, args=(shared_value,))
consumer_process = multiprocessing.Process(target=consumer, args=(shared_value,))

producer_process.start()
consumer_process.start()

producer_process.join()
consumer_process.join()
