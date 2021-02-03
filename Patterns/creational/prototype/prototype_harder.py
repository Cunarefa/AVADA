import copy


class Prototype:
    def __init__(self):
        self._objects = {}

    def add_obj(self, name, obj):
        self._objects[name] = obj

    def remove_obj(self, name):
        del self._objects[name]

    def clone(self, name, **kwargs):
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(kwargs)
        return obj

    def __str__(self):
        return self._objects


class Some():
    def __init__(self):
        self.x = 3
        self.y = 6
        self.garbage = [1, 2, 3, [23, 5, 56]]

    def __str__(self):
        return f'{self.x} {self.y} {self.garbage}'


class Other:
    def __init__(self):
        self.flight = 307
        self.country = 'Brazil'

    def __str__(self):
        return f'Flight number {self.flight} is heading to {self.country}'


if __name__ == '__main__':
    a = Some()
    p = Prototype()
    p.add_obj('object_1', a)
    print(p.clone('object_1'))
    print(p.clone('object_1', x=9, y=7, garbage=[3, 6, 7, [64, 68, 86], 897]))

    print('\n')

    other = Other()
    p.add_obj('object_2', other)
    print(p.clone('object_2'))
    print(p.clone('object_2', flight=678, country='USA'))
