from abc import ABC, abstractmethod
from project.baked_food.baked_food import BakedFood
from project.drink.drink import Drink
from project.validator import Validator


class Table(ABC):
    def __init__(self, table_number, capacity):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        Validator.check_for_negative_or_zero_value(value, "Capacity has to be greater than 0!")
        self.__capacity = value

    @property
    @abstractmethod
    def table_number(self):
        pass

    @table_number.setter
    def table_number(self, value):
        pass

    def reserve(self, number_of_people: int):
        self.number_of_people = number_of_people
        self.is_reserved = True

    def order_food(self, baked_food: BakedFood):
        self.food_orders.append(baked_food)

    def order_drink(self, drink: Drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        food_bill = sum(x.price for x in self.food_orders)
        drink_bill = sum(y.price for y in self.drink_orders)
        total = food_bill + drink_bill
        return total

    def clear(self):
        self.drink_orders = []
        self.food_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    def free_table_info(self):
        if not self.is_reserved:
            result = f"Table: {self.table_number}\n" + \
                     f"Type: {self.__class__.__name__}\n" + \
                     f"Capacity: {self.capacity}"
            return result
