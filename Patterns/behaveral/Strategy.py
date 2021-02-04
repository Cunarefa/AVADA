from abc import ABC, abstractmethod


class Context:
    def __init__(self, strategy):
        self._strategy = strategy

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        self._strategy = strategy

    def some_logic(self):
        print("Context: Sorting data using the strategy")
        result = self._strategy.do_somthing(['a', 'b', 'c', 'd', 'e'])
        print(",".join(result))


class AbstractAlgorithm(ABC):
    @abstractmethod
    def do_somthing(self, data):
        pass


class Algorithm_1(AbstractAlgorithm):
    def do_somthing(self, data):
        return reversed(data)


class Algorithm_2(AbstractAlgorithm):
    def do_somthing(self, data):
        return sorted(data)


if __name__ == '__main__':
    con = Context(Algorithm_1())
    con.some_logic()
    print('')
    con.strategy = Algorithm_2()
    con.some_logic()
