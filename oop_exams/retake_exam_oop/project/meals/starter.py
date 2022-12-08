from project.meals.meal import Meal


class Starter(Meal):
    def __init__(self, name: str, price: float, quantity=60):
        super().__init__(name, price, quantity)

    def details(self):
        result = f"Starter {self.name}: {self.price:.2f}lv/piece"
        return result
