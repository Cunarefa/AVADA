from abc import ABC, abstractmethod


class Collection(ABC):
    @abstractmethod
    def iterator(self):
        pass


class ListCollection(Collection):
    def __init__(self, collection):
        self._collection = collection

    def iterator(self):
        return ListIterator(self._collection)


class Iterator(ABC):
    def __init__(self, collection, position):
        self._collection = collection
        self._position = position

    @abstractmethod
    def current(self):
        pass

    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def has_next(self):
        pass

    def _raise_key_exception(self):
        raise self._error(f'Collection of class {self.__class__.__name__}'
                          f' does not have key "{self._position}"')


class ListIterator(Iterator):
    _error = IndexError

    def __init__(self, collection):
        super(ListIterator, self).__init__(collection, 0)

    def current(self):
        if self._position < len(self._collection):
            return self._collection[self._position]
        self._raise_key_exception()

    def next(self):
        if len(self._collection) >= self._position + 1:
            self._position += 1
            return self._collection[self._position]
        self._raise_key_exception()

    def has_next(self):
        return len(self._collection) >= self._position + 1


if __name__ == '__main__':
    lis = ListCollection([1, 2, 3, 4, 5])
    print('OUTPUT:')
    j = lis.iterator()
    print(j.current())
    j.next()
    print(j.next())
    print(j.current())
    print(j.has_next())
