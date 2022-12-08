from project.client import Client
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.meal import Meal
from project.meals.starter import Starter


class FoodOrdersApp:
    receipt_id = 0

    def __init__(self):
        self.menu = []
        self.clients_list = []

    def register_client(self, client_phone_number: str):
        for client in self.clients_list:
            if client.phone_number == client_phone_number:
                raise Exception("The client has already been registered!")
        new_client = Client(client_phone_number)
        self.clients_list.append(new_client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        possible_meals = {"Starter": Starter, "MainDish": MainDish, "Dessert": Dessert}
        for meal in meals:
            if meal.__class__.__name__ in possible_meals:
                self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        result = ""
        for meal in self.menu:
            result += meal.details() + "\n"
        return result.strip()

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        client = None
        current_client = self.find_client_by_phone_num(client_phone_number)
        if current_client is None:
            new_client = Client(client_phone_number)
            self.clients_list.append(new_client)
            client = new_client
        else:
            client = current_client

        meal_types = {"Starter": Starter, "MainDish": MainDish, "Dessert": Dessert}

        for meal_name, meal_quantity in meal_names_and_quantities.items():
            meal = self.find_meal_by_name(meal_name)

            if meal is None:
                raise Exception(f"{meal_name} is not on the menu!")

            if meal.quantity < meal_quantity:
                raise Exception(f"Not enough quantity of {meal.__class__.__name__}: {meal_name}!")

        for meal_name, meal_quantity in meal_names_and_quantities.items():
            meal = self.find_meal_by_name(meal_name)
            meal_price = meal.price
            meal_to_add = meal_types[meal.__class__.__name__](meal_name, meal_price, meal_quantity)
            client.shopping_cart.append(meal_to_add)
            meal.quantity -= meal_quantity
            client.bill += meal.price * meal_quantity

        result = []
        for meal in client.shopping_cart:
            current_name = meal.name
            result.append(current_name)
        return f"Client {client_phone_number} successfully ordered {', '.join(result)} for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client = self.find_client_by_phone_num(client_phone_number)
        if len(client.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")

        for meal in client.shopping_cart:
            current_quantity = meal.quantity
            for i in range(len(self.menu)):
                if meal.name == self.menu[i].name:
                    self.menu[i].quantity += current_quantity
        client.bill = 0
        client.shopping_cart = []
        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):

        client = self.find_client_by_phone_num(client_phone_number)
        if len(client.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")
        total_paid_money = client.bill
        client.bill = 0
        client.shopping_cart = []
        self.receipt_id += 1
        return f"Receipt #{self.receipt_id} with total amount of {total_paid_money:.2f} was successfully paid for " \
               f"{client_phone_number}."

    def __str__(self):
        result = f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."
        return result

    def find_client_by_phone_num(self, phone_number):
        for client in self.clients_list:
            if client.phone_number == phone_number:
                return client
        return None

    def find_meal_by_name(self, meal_name):
        for meal in self.menu:
            if meal.name == meal_name:
                return meal
        return None
