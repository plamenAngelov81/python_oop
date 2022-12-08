from my_tests.project import Bird


class Owl(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    @property
    def allowed_food(self):
        return ["Meat"]

    @property
    def weight_incremental(self):
        return 0.25

    def make_sound(self):
        return "Hoot Hoot"


class Hen(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    @property
    def allowed_food(self):
        return ["Vegetable", "Fruit", "Meat", "Seed"]

    @property
    def weight_incremental(self):
        return 0.35

    def make_sound(self):
        return "Cluck"

