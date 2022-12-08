from my_tests.project import Beverage


class HotBeverage(Beverage):
    def __init__(self, name, price, milliliters: float):
        super().__init__(name, price, milliliters)
