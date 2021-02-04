from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class ConcreteComponentA(Component):
    def accept(self, visitor):
        visitor.visit_component_a(self)

    def some_operatiion_a(self):
        return 'A'


class ConcreteComponentB(Component):
    def accept(self, visitor):
        visitor.visit_component_b(self)

    def additional_method_b(self):
        return 'B'


class Visitor(ABC):
    @abstractmethod
    def visit_component_a(self, component):
        pass

    @abstractmethod
    def visit_component_b(self, component):
        pass


class Visitor1(Visitor):
    def visit_component_a(self, component):
        print(f"{component.some_operatiion_a()} + Visitor1")

    def visit_component_b(self, component):
        print(f"{component.additional_method_b()} + Visitor1")


class Visitor2(Visitor):
    def visit_component_a(self, component):
        print(f"{component.some_operatiion_a()} + Visitor2")

    def visit_component_b(self, component):
        print(f"{component.additional_method_b()} + Visitor2")



def client_code(components, visitor):
    for component in components:
        component.accept(visitor)


if __name__ == '__main__':
    components = [ConcreteComponentA(), ConcreteComponentB()]

    v1 = Visitor1()
    client_code(components, v1)
    print('')
    v2 = Visitor2()
    client_code(components, v2)
