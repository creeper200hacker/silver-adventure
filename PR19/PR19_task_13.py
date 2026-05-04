import threading
import time

def background_task():
    while True:
        print("Фоновый поток работает")
        time.sleep(1)

daemon = threading.Thread(target=background_task, daemon=True)
daemon.start()

time.sleep(3)
print("Основная программа завершена")
