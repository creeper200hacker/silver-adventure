import threading

counter = 0
lock = threading.Lock()

def increase():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1

threads = [threading.Thread(target=increase) for _ in range(5)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

print("Counter:", counter)
