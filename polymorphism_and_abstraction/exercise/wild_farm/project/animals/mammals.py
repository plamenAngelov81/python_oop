from my_tests.project import Mammal


class Mouse(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @property
    def allowed_food(self):
        return ["Vegetable", "Fruit"]

    @property
    def weight_incremental(self):
        return 0.10

    def make_sound(self):
        return "Squeak"


class Dog(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @property
    def allowed_food(self):
        return ["Meat"]

    @property
    def weight_incremental(self):
        return 0.40

    def make_sound(self):
        return "Woof!"


class Cat(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @property
    def allowed_food(self):
        return ["Vegetable", "Meat"]

    @property
    def weight_incremental(self):
        return 0.30

    def make_sound(self):
        return "Meow"


class Tiger(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @property
    def allowed_food(self):
        return ["Meat"]

    @property
    def weight_incremental(self):
        return 1.00

    def make_sound(self):
        return "ROAR!!!"




