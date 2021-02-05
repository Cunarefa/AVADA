
class Facad:
    def __init__(self, subsystem1, subsystem2):
        self._subsystem1 = subsystem1 or Subsystem1()
        self._subsystem2 = subsystem2

    def execute(self):
        results = []
        results.append("Facade initializes subsystems:")
        results.append(self._subsystem1.operation_1())
        results.append(self._subsystem2.operation_1())
        results.append("Facade orders subsystems to perform the action:")
        results.append(self._subsystem1.operation_n())
        results.append(self._subsystem2.operation_z())
        return "\n".join(results)


class Subsystem1:
    def operation_1(self):
        return "System 1: Ready"

    def operation_n(self):
        return "System 1: Go!"


class Subsystem2:
    def operation_1(self):
        return "System 2: Ready"

    def operation_z(self):
        return "System 2: Go!"


def client_code(facad):
    print(facad.execute(), end="")


if __name__ == '__main__':
    sub1 = Subsystem1()
    sub2 = Subsystem2()
    facad = Facad(sub1, sub2)

    client_code(facad)