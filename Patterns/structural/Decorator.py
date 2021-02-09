class Component:
    def execute(self):
        pass


class ConcreteComponent(Component):
    def execute(self):
        return "ConcreteComponent"


class BaseDecorator(Component):
    _component = None

    def __init__(self, component):
        self._component = component

    @property
    def component(self):
        return self._component

    def execute(self):
        return self._component.execute()


class Decorator1(BaseDecorator):
    def execute(self):
        return f'Decorator-1 ({self.component.execute()})'

    def extra(self):
        return f'Decorator-1 ({self.component.execute()} Decorator-2)'


class Decorator2(BaseDecorator):
    def execute(self):
        return f'Decorator-2 ({self.component.execute()})'

    def extra(self):
        return f'Decorator-2 ({self.component.execute()} Decorator-1)'


if __name__ == '__main__':
    simple = ConcreteComponent()
    decor_1 = Decorator1(simple)
    decor_2 = Decorator2(decor_1)
    base = BaseDecorator(decor_2)

    print("Client: Decorated component:")
    print(decor_1.execute())
    print(decor_2.extra())
