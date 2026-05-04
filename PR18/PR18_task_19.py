class MyContextManager:
    def __enter__(self):
        print("Start")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("End")


with MyContextManager():
    print("Работа внутри контекстного менеджера")
