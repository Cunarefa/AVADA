from abc import ABC, abstractmethod


class Document:
    _state = None

    def __init__(self, state):
        self.get_state(state)

    def get_state(self, state):
        print(f"Document: Transition to {type(state).__name__}")
        self._state = state
        self._state.document = self

    def request1(self):
        self._state.handle1()

    def request2(self):
        self._state.handle2()


class AbstractState(ABC):
    @property
    def document(self):
        return self._document

    @document.setter
    def document(self, document):
        self._document = document

    @abstractmethod
    def handle1(self):
        pass

    @abstractmethod
    def handle2(self):
        pass


class State_A(AbstractState):
    def handle1(self):
        print("State_A handles request1.")
        print("State_A wants to change the state of the context.")
        self.document.get_state(State_B())

    def handle2(self):
        print("State_A handles request2.")


class State_B(AbstractState):
    def handle1(self):
        print("State_B handles request1.")

    def handle2(self):
        print("State_B handles request2.")
        print("State_B wants to change the state of the context.")
        self.document.get_state(State_A())


if __name__ == '__main__':
    doc = Document(State_A())
    doc.request1()
    doc.request2()
