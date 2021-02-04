from abc import ABC, abstractmethod


class Handler(ABC):
    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def handle(self, request):
        pass


class BaseHandler(Handler):
    _next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)
        return None


class Authorize(BaseHandler):
    def handle(self, request):
        if request == 'Admin':
            return f"{request} - right user"
        return super().handle(request)


class If_Admin(BaseHandler):
    def handle(self, request):
        if request == 'Henry':
            return f"{request} - It's admin"
        return super().handle(request)


class SwiftHandler(BaseHandler):
    def handle(self, request):
        if request == 'swift':
            return f"{request} - It's admin"
        return super().handle(request)


def client_code(handler):
    for user in ['Admin', 'swift', 'Henry']:
        result = handler.handle(user)
        if result:
            print(f"{result}.")
        else:
            print(f"{user} - wrong user. ")


if __name__ == '__main__':
    auth = Authorize()
    admin = If_Admin()
    swift = SwiftHandler()

    auth.set_next(admin).set_next(swift)

    client_code(auth)
    print('-' * 20)
    client_code(admin)
