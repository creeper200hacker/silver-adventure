class ShoppingList:
    def __init__(self):
        self.__items = []

    def add_item(self, item):
        self.__items.append(item)

    def get_items(self):
        return self.__items

    def clear(self):
        self.__items = []


# Пример 1
shopping = ShoppingList()
shopping.add_item("apple")
shopping.add_item("banana")
print(shopping.get_items())  # ['apple', 'banana']
shopping.clear()
print(shopping.get_items())  # []
