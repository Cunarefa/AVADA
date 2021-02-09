from abc import ABC, abstractmethod


class Abstract(ABC):
    @abstractmethod
    def request(self):
        pass


class Real(Abstract):
    def request(self):
        print('It is a RealClass implementation')


class Proxy(Abstract):
    _lis = [1, 2, 3]

    def __init__(self):
        self._real = Real()

    def request(self):
        if self.some(1):
            print('Proxy implementation at first...')
            self._real.request()
        else:
            raise IndexError('Index isn\'t in list')

    def some(self, i):
        return i in self._lis


if __name__ == '__main__':
    p = Proxy()
    p.request()
