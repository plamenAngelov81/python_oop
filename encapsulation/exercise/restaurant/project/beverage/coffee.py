from my_tests.project import HotBeverage


class Coffee(HotBeverage):
    MILLILITERS = 50
    PRICE = 3.50

    def __init__(self, name, caffeine):
        super().__init__(name, Coffee.PRICE, Coffee.MILLILITERS)
        self.caffeine: float = caffeine

    @property
    def caffeine(self):
        return self.__caffeine

    @caffeine.setter
    def caffeine(self, value):
        self.__caffeine = value

    