from project.auto_checker import Checker


class Planet:
    def __init__(self, name):
        self.name = name
        self.items = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Checker.check_for_empty_strings(value, "Planet name cannot be empty string or whitespace!")
        self.__name = value


