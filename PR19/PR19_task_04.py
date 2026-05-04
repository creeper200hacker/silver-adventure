import threading
import time

def task(name):
    for i in range(1, 4):
        print(name, i)
        time.sleep(1)

thread1 = threading.Thread(target=task, args=("Thread-1",))
thread2 = threading.Thread(target=task, args=("Thread-2",))
thread1.start()
thread2.start()
thread1.join()
thread2.join()
