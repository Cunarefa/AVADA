import copy
from abc import ABC, abstractmethod


class Monster(ABC):
    def __init__(self):
        self.name = 'Toro'
        self.health = 100

    def __str__(self):
        return f'{self.name} have {self.health} health'

    @abstractmethod
    def clone(self):
        pass


class Demon(Monster):
    def clone(self):
        return copy.copy(self)


class Ghost(Monster):
    def clone(self):
        return copy.copy(self)


c = Demon()
p = c.clone()
print(p.__str__())
p.name = 'Bullrock'

print(p.__str__())
print(type(p))
print(c.__str__())
