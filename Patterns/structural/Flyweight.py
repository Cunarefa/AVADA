import json


class Flyweight:
    def __init__(self, common_state):
        self._common_state = common_state

    def operation(self, unique_state):
        common_to_json = json.dumps(self._common_state)
        unique_to_json = json.dumps(unique_state)
        print(f"Flyweight: Displaying shared ({common_to_json}) and unique ({unique_to_json}) state.",
              end="")


class FlyweightFactory:
    _flyweights = {}

    def __init__(self, initial_flyweights):
        for state in initial_flyweights:
            self._flyweights[self.get_key(state)] = Flyweight(state)

    def get_key(self, state):
        return "_".join(sorted(state))

    def get_flyweight(self, common_state):
        key = self.get_key(common_state)

        if not self._flyweights.get(key):
            print("FlyweightFactory: Can't find a flyweight, creating new one.")
            self._flyweights[key] = Flyweight(common_state)
        else:
            print("FlyweightFactory: Reusing existing flyweight.")

        return self._flyweights[key]


def client_code(factory: FlyweightFactory, plates: str, owner: str,
                brand: str, model: str, color: str
            ):
    print("\nClient: Adding a car to database.")
    flyweight = factory.get_flyweight([brand, model, color])
    flyweight.operation([plates, owner])


if __name__ == '__main__':
    factory = FlyweightFactory([
        ["Chevrolet", "Camaro2018", "pink"],
        ["Mercedes Benz", "C500", "red"],
        ["BMW", "M5", "red"],
        ["BMW", "X6", "white"],
    ])

    client_code(factory, "CL234IR", "James Doe", "BMW", "M5", "red")
    print('')
    client_code(factory, "CL234IR", "James Doe", "BMW", "M1", "red")
    print('')



