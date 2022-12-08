from abc import ABC, abstractmethod

from my_tests.project import Food


class Animal(ABC):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @property
    @abstractmethod
    def allowed_food(self):
        pass

    @property
    @abstractmethod
    def weight_incremental(self):
        pass

    @abstractmethod
    def make_sound(self):
        pass

    def feed(self, food: Food):
        food_type = food.__class__.__name__
        if food.__class__.__name__ not in self.allowed_food:
            return f"{self.__class__.__name__} does not eat {food_type}!"
        self.food_eaten += food.quantity
        self.weight += food.quantity * self.weight_incremental


class Bird(Animal, ABC):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal, ABC):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"
