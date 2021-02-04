from abc import ABC, abstractmethod
from random import randrange


class AbstractPublisher(ABC):
    @abstractmethod
    def add_subscriber(self, subscriber):
        pass

    @abstractmethod
    def detach(self, subscriber):
        pass

    @abstractmethod
    def notify(self):
        pass


class Publisher(AbstractPublisher):
    _subscribers = []
    _state = None

    def add_subscriber(self, subscriber):
        self._subscribers.append(subscriber)

    def detach(self, subscriber):
        self._subscribers.remove(subscriber)

    def notify(self):
        print("Publisher: Notifying observers...")
        for subscriber in self._subscribers:
            subscriber.update(self)

    def some_logic(self):
        self._state = randrange(0, 10)
        print(f"Publisher: My state has just changed to: {self._state}")
        self.notify()


class AbstractSubscriber(ABC):
    @abstractmethod
    def update(self, publisher):
        pass


class Subscriber(AbstractSubscriber):
    def update(self, publisher: Publisher):
        if publisher._state < 3:
            print("Subscriber: Reacted to the event")


class Subscriber2(AbstractSubscriber):
    def update(self, publisher):
        if publisher._state == 0 or publisher._state >= 2:
            print("Subscriber: Reacted to the event")


if __name__ == '__main__':
    publisher = Publisher()
    sub1 = Subscriber()
    sub2 = Subscriber2()

    publisher.add_subscriber(sub1)
    publisher.add_subscriber(sub2)

    publisher.some_logic()
    print('')
    publisher.some_logic()
