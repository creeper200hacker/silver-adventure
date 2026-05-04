import threading

def task1():
    for i in range(1, 4):
        print("task1:", i)

def task2():
    for i in range(1, 4):
        print("task2:", i)

print("Последовательное выполнение:")
task1()
task2()

print("Параллельное выполнение через потоки:")
thread1 = threading.Thread(target=task1)
thread2 = threading.Thread(target=task2)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
