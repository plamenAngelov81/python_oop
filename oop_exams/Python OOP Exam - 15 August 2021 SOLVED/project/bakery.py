from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable
from project.validator import Validator


class Bakery:
    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.check_for_empty_strings(value, "Name cannot be empty string or white space!")
        self.__name = value

    def find_food_by_name(self, food_name):
        for food in self.food_menu:
            if food.name == food_name:
                return food
        return None

    def find_table_by_number(self, table_number):
        for table in self.tables_repository:
            if table.table_number == table_number:
                return table
        return None

    def find_drink_by_name(self, drink_name):
        for drink in self.drinks_menu:
            if drink.name == drink_name:
                return drink
        return None

    def add_food(self, food_type: str, name: str, price: float):
        if food_type not in ["Bread", "Cake"]:
            return
        for food in self.food_menu:
            if food.name == name:
                raise Exception(f"{food.__class__.__name__} {name} is already in the menu!")
        if food_type == "Bread":
            new_food = Bread(name, price)
            self.food_menu.append(new_food)

        elif food_type == "Cake":
            new_food = Cake(name, price)
            self.food_menu.append(new_food)
        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        if drink_type not in ["Tea", "Water"]:
            return

        for drink in self.drinks_menu:
            if drink.name == name:
                raise Exception(f"{drink_type} {name} is already in the menu!")

        if drink_type == "Tea":
            new_drink = Tea(name, portion, brand)
            self.drinks_menu.append(new_drink)
        elif drink_type == "Water":
            new_drink = Water(name, portion, brand)
            self.drinks_menu.append(new_drink)
        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if table_type not in ["InsideTable", "OutsideTable"]:
            return

        for table in self.tables_repository:
            if table.table_number == table_number:
                raise Exception(f"Table {table_number} is already in the bakery!")

        if table_type == "InsideTable":
            new_table = InsideTable(table_number, capacity)
            self.tables_repository.append(new_table)
        elif table_type == "OutsideTable":
            new_table = OutsideTable(table_number, capacity)
            self.tables_repository.append(new_table)
        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        for table in self.tables_repository:
            if not table.is_reserved and number_of_people <= table.capacity:
                table.reserve(number_of_people)
                return f"Table {table.table_number} has been reserved for {number_of_people} people"
        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *food_names):
        table = self.find_table_by_number(table_number)
        if table is None:
            return f"Could not find table {table_number}"

        ordered_foods = f"Table {table_number} ordered:\n"
        skip_foods = f"{self.name} does not have in the menu:\n"

        for food_name in food_names:
            food = self.find_food_by_name(food_name)
            if food is None:
                skip_foods += food_name + "\n"
            else:
                table.order_food(food)
                ordered_foods += str(food) + "\n"
        return ordered_foods.strip() + "\n" + skip_foods.strip()

    def order_drink(self, table_number: int, *drink_names):
        table = self.find_table_by_number(table_number)
        if table is None:
            return f"Could not find table {table_number}"

        ordered_drinks = f"Table {table_number} ordered:" + "\n"
        skipped_drinks = f"{self.name} does not have in the menu:" + "\n"

        for drink_name in drink_names:
            drink = self.find_drink_by_name(drink_name)

            if drink is None:
                skipped_drinks += drink_name + "\n"
            else:
                table.order_drink(drink)
                ordered_drinks += str(drink) + "\n"

        return ordered_drinks.strip() + "\n" + skipped_drinks.strip()

    def leave_table(self, table_number: int):
        table = self.find_table_by_number(table_number)
        bill = table.get_bill()
        self.total_income += bill
        table.clear()
        result = f"Table: {table_number}\n" + f"Bill: {bill:.2f}"
        return result

    def get_free_tables_info(self):
        result = ""
        for table in self.tables_repository:
            if not table.is_reserved:
                result += table.free_table_info() + "\n"
        return result.strip()

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"

