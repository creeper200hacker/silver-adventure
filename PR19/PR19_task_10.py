import threading
from multiprocessing import Process
from time import perf_counter

def calculate():
    sum(range(1, 5_000_000))

if __name__ == "__main__":
    start = perf_counter()
    threads = [threading.Thread(target=calculate) for _ in range(2)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print("Threading:", perf_counter() - start)

    start = perf_counter()
    processes = [Process(target=calculate) for _ in range(2)]
    for process in processes:
        process.start()
    for process in processes:
        process.join()
    print("Multiprocessing:", perf_counter() - start)
