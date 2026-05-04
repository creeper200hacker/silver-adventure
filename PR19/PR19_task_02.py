import threading

def print_numbers(name):
    for i in range(1, 6):
        print(name, i)

thread1 = threading.Thread(target=print_numbers, args=("Поток 1",))
thread2 = threading.Thread(target=print_numbers, args=("Поток 2",))
thread1.start()
thread2.start()
thread1.join()
thread2.join()
