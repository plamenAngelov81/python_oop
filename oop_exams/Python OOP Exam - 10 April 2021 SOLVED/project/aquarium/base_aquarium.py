from abc import ABC, abstractmethod

from project.validator import Validator


class BaseAquarium(ABC):
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.check_for_empty_strings(value, "Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        result = sum(x.comfort for x in self.decorations)
        return result

    @abstractmethod
    def add_fish(self, fish):
        pass

    def remove_fish(self, fish):
        self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        result = f"{self.name}:\n"

        if len(self.fish) > 0:
            result += f"Fish: {' '.join(f.name for f in self.fish)}" + "\n"
        else:
            result += "Fish: none" + "\n"
        result += f"Decorations: {len(self.decorations)}\n"
        result += f"Comfort: {self.calculate_comfort()}"
        return result
