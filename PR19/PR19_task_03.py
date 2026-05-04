import threading

def print_name(name):
    for _ in range(5):
        print(name)

threads = []
for i in range(1, 4):
    thread = threading.Thread(target=print_name, args=(f"Thread-{i}",))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
