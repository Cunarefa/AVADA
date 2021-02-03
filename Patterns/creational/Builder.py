from abc import ABC, abstractmethod
from typing import Any


class Builder(ABC):
    @abstractmethod
    def tires(self):
        pass

    @abstractmethod
    def frame(self):
        pass


class BuilderMountainBike(Builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self.mountain_bike = Bike()

    def tires(self):
        self.mountain_bike.add_detail('Mountain tires')

    def frame(self):
        self.mountain_bike.add_detail('Mountain frame')

    def speedometer(self):
        self.mountain_bike.speedometer = True
        return self.mountain_bike.speedometer

    @property
    def get_product(self):
        product = self.mountain_bike
        self.reset()
        return product


class Bike:
    def __init__(self):
        self.parts = []
        self.speedometer = False

    def add_detail(self, detail: Any):
        self.parts.append(detail)

    def list_parts(self):
        print(f"Bike parts: {', '.join(self.parts)}. Speedometer: {self.speedometer}", end="")


class Director:
    def __init__(self, builder):
        self.builder = builder

    def build_popular_assembly(self):
        self.builder.tires()
        self.builder.frame()
        self.builder.speedometer()

    def build_custome(self):
        self.builder.frame()


builder = BuilderMountainBike()
dir = Director(builder)

dir.build_popular_assembly()
builder.get_product.list_parts()
