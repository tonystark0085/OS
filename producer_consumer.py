import threading
import time
import random
import queue

buffer_size = 5
buffer = queue.Queue(buffer_size)
lock = threading.Lock()
items_produced = 0
items_consumed = 0
max_items = 10

def producer():
    global items_produced
    while items_produced < max_items:
        item = random.randint(1, 1000)
        with lock:
            print("\nProducer is checking the buffer...")
            if buffer.full():
                print("Buffer is full. Producer is waiting...")
                time.sleep(1)
            else:
                buffer.put(item)
                print(f"Produced: {item}")
                items_produced += 1
                print(f"\nBuffer: {list(buffer.queue)}\n")
        time.sleep(random.random())

def consumer():
    global items_consumed
    while items_consumed < max_items:
        with lock:
            print("\nConsumer is checking the buffer...")
            if buffer.empty():
                print("Buffer is empty. Consumer is waiting...")
                time.sleep(1)
            else:
                item = buffer.get()
                print(f"Consumed: {item}")
                items_consumed += 1
                print(f"\nBuffer: {list(buffer.queue)}\n")
        time.sleep(random.random())

producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()

print("All items produced and consumed.")
