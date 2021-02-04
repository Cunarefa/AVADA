from abc import ABC, abstractmethod


class Controller(ABC):
    @abstractmethod
    def notify(self, sender, request):
        pass


class ConcreteController(Controller):
    def __init__(self, boeing, helicopter):
        self.boeing = boeing
        self.boeing.mediator = self
        self.helicopter = helicopter
        self.helicopter.mediator = self

    def notify(self, sender, request):
        if request == 'A':
            print("Mediator reacts on A and triggers following operations:")
            self.helicopter.do_c()
        elif request == 'D':
            print("Mediator reacts on D and triggers following operations:")
            self.boeing.do_b()
            self.helicopter.do_c()


class Plane:
    def __init__(self, controller: Controller = None):
        self._controller = controller

    @property
    def mediator(self):
        return self._controller

    @mediator.setter
    def mediator(self, controller):
        self._controller = controller


class Boeing(Plane):
    def do_a(self):
        print("Boeing does A.")
        self.mediator.notify(self, 'A')

    def do_b(self):
        print("Boeing does B.")
        self.mediator.notify(self, 'B')


class Helicopter(Plane):
    def do_c(self):
        print("Helicopter does C.")
        self.mediator.notify(self, 'C')

    def do_d(self):
        print("Helicopter does D.")
        self.mediator.notify(self, 'D')


if __name__ == '__main__':
    boeing = Boeing()
    helicopter = Helicopter()
    mediator = ConcreteController(boeing, helicopter)

    boeing.do_a()

