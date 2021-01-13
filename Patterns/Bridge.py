from abc import ABC, abstractmethod


class Fuel(ABC):
    @abstractmethod
    def get_fuel(self):
        pass


class DieselFuel(Fuel):
    def get_fuel(self):
        return 'Diesel fuel is slower then petrol'


class PetrolFuel(Fuel):
    def get_fuel(self):
        return 'Petrol fuel is faster then diesel'


class Vehicle(ABC):
    @abstractmethod
    def model(self):
        pass

    @abstractmethod
    def max_speed(self):
        pass


class Car(Vehicle):
    def __init__(self, rolling, digit, fuel):
        self.rolling = rolling
        self.fuel = fuel
        self.okt_digit = digit

    def model(self):
        return f"Model BMW"

    def max_speed(self):
        speed = int(self.rolling / self.okt_digit)
        return f'Speed = {speed} km/h. {self.fuel.get_fuel()}'


class Moto(Vehicle):
    def __init__(self, rolling, digit, fuel):
        self.rolling = rolling
        self.fuel = fuel
        self.okt_digit = digit

    def model(self):
        return "Model Suzuki"

    def max_speed(self):
        speed = int(self.rolling / self.okt_digit)
        return f'Speed = {speed} km/h. {self.fuel.get_fuel()}'


car = Car(1500, 4, DieselFuel())
print(car.model())
print(car.max_speed())

print('\n')

moto = Moto(3000, 2, PetrolFuel())
print(moto.model())
print(moto.max_speed())
