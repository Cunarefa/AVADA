from abc import ABC, abstractmethod
from datetime import datetime


class Creator:
    def __init__(self):
        self._state = None

    def set_state(self, state):
        self._state = state

    def get_state(self):
        return self._state

    def save_state(self):
        return Memento(self._state)

    def restore(self, memento):
        self._state = memento.get_state()


class AbstractMemento(ABC):
    @abstractmethod
    def get_state_name(self):
        pass

    @abstractmethod
    def get_state_date(self):
        pass


class Memento(AbstractMemento):
    def __init__(self, state):
        self._state = state
        self._date = str(datetime.now())

    def get_state(self):
        return self._state

    def get_state_name(self):
        return f"{self._date} / ({self._state}...)"

    def get_state_date(self):
        return self._date


class Caretaker:
    def __init__(self, creator):
        self._mementos = []
        self._memento = None
        self._creator = creator

    def set_memento(self, memento):
        self._memento = memento

    def get_memento(self):
        return self._memento

    def add_memento(self):
        self._mementos.append(self._creator.save_state())

    def undo(self):
        if not len(self._mementos):
            return

        memento = self._mementos.pop()
        print(f"Caretaker: Restoring state to: {memento.get_state_name()}")
        try:
            self._creator.restore(memento)
        except Exception:
            self.undo()



if __name__ == '__main__':
    creator = Creator()
    care = Caretaker(creator)

    creator.set_state('On')
    print('Creator state: ', creator.get_state())
    care.set_memento(creator.save_state())
    care.add_memento()

    creator.set_state('Off')
    print('Creator state: ', creator.get_state())

    creator.restore(care.get_memento())
    print('Creator restore state:', creator.get_state())

    care.undo()


