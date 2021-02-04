from collections.abc import Iterator, Iterable
from typing import List, Any


class WordsCollection(Iterable):
    def __init__(self, collection: List[Any] = []):
        self.collection = collection

    def __iter__(self):
        return AlfaIterator(self.collection)

    def get_reverse_iterator(self):
        return AlfaIterator(self.collection, True)

    def add_item(self, item):
        self.collection.append(item)


class AlfaIterator(Iterator):
    _position = None
    _reverse = False

    def __init__(self, collection, reverse: bool = False):
        self.collection = collection
        self.reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        try:
            value = self.collection[self._position]
            self._position += -1 if self.reverse else 1
        except IndexError:
            raise StopIteration()

        return value


if __name__ == "__main__":
    collection = WordsCollection()
    collection.add_item("First")
    collection.add_item("Second")
    collection.add_item("Third")

    print("Straight traversal:")
    print("\n".join(collection))
    print(" ")

    print("Reverse traversal:")
    print("\n".join(collection.get_reverse_iterator()))
