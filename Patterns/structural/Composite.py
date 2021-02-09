from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def draw(self):
        pass


class ProductA(Product):
    def draw(self):
        print(f"I'm product A")


class ProductB(Product):
    def draw(self):
        print(f"I'm product B")


class Composite(Product):

    def __init__(self):
        self.__products = []

    def add_item(self, item):
        self.__products.append(item)

    def remove_item(self, item):
        self.__products.remove(item)

    def draw(self):
        for component in self.__products:
            component.draw()


a = ProductA()
b = ProductB()
c = Composite()
c_big = Composite()

c.add_item(a)
c.add_item(b)

c.draw()
