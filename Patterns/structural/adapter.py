
class String:
    def string(self):
        return 'Some string'


class Integers:
    def integers(self):
        return 123


class Adapter(String):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def string(self):
        return str(self.adaptee.integers())


def client_code(obj):
    print("Some special type: " + obj.string())


if __name__ == '__main__':
    integer = Integers()
    adapter = Adapter(integer)

    client_code(adapter)
