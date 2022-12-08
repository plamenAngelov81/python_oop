from abc import ABC, abstractmethod

from project.auto_checker import Checker


class Astronaut(ABC):
    BREATHE = 10

    @abstractmethod
    def __init__(self, name, oxygen):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        Checker.check_for_empty_strings(value, "Astronaut name cannot be empty string or whitespace!")
        self.__name = value

    def breathe(self):
        self.oxygen -= self.BREATHE

    def increase_oxygen(self, amount: int):
        self.oxygen += amount
