from multiprocessing import Process

def calculate_sum(name):
    result = sum(range(1, 100001))
    print(name, result)

if __name__ == "__main__":
    process1 = Process(target=calculate_sum, args=("Process-1",))
    process2 = Process(target=calculate_sum, args=("Process-2",))
    process1.start()
    process2.start()
    process1.join()
    process2.join()
