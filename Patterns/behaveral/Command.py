from abc import ABC, abstractmethod


class Cook:
    def make_order(self, order):
        print(f"Receiver making an {order}")

    def do_wishes(self, wishes):
        print(f"Receiver done '{wishes}'")


class Order(ABC):
    @abstractmethod
    def execute(self):
        pass


class SimpleOrder(Order):
    def __init__(self, order):
        self._order = order

    def execute(self):
        print(f"The order - {self._order} - is simple. I'll make it")


class ComplexOrder(Order):
    def __init__(self, cook: Cook, order, wishes):
        self.cook = cook
        self.order = order
        self.wishes = wishes

    def execute(self):
        print(f"This order {self.order} with these wishes - '{self.wishes}' - is too hard.")
        self.cook.make_order(self.order)
        self.cook.do_wishes(self.wishes)


class Visitor:
    _take_order = None
    _pass_order = None

    def start_order(self, order):
        self._take_order = order

    def end_order(self, order):
        self._pass_order = order

    def do_somthing(self):
        if isinstance(self._take_order, SimpleOrder):
            self._take_order.execute()

        if isinstance(self._pass_order, ComplexOrder):
            self._pass_order.execute()


if __name__ == '__main__':
    visitor = Visitor()
    visitor.start_order(SimpleOrder('Simple order'))

    cook = Cook()
    visitor.end_order(ComplexOrder(cook, 'Complex order', 'Make some condiment'))

    visitor.do_somthing()
