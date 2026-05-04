import queue
import threading

tasks = queue.Queue()

for i in range(1, 6):
    tasks.put(i)

def worker():
    while not tasks.empty():
        item = tasks.get()
        print("Обработано:", item)
        tasks.task_done()

thread = threading.Thread(target=worker)
thread.start()
tasks.join()
thread.join()
