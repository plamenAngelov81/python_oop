from project.baked_food.baked_food import BakedFood


class Cake(BakedFood):
    def __init__(self, name, price: float):
        super().__init__(name, 245, price)
