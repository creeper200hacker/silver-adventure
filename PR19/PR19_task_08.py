import queue
import threading
import time

tasks = queue.Queue()

for i in range(1, 11):
    tasks.put(i)

def worker(worker_id):
    while True:
        try:
            task = tasks.get(timeout=1)
        except queue.Empty:
            break
        print(f"Worker {worker_id} обрабатывает задачу {task}")
        time.sleep(0.5)
        tasks.task_done()

threads = [threading.Thread(target=worker, args=(i,)) for i in range(1, 4)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
