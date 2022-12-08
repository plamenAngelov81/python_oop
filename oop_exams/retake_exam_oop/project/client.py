class Client:
    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.shopping_cart = []
        self.bill = 0

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value: str):
        if int(value[0]) != 0:
            raise ValueError("Invalid phone number!")
        if len(value) < 10:
            raise ValueError("Invalid phone number!")
        for i in value:
            if not i.isdigit():
                raise ValueError("Invalid phone number!")
        self.__phone_number = value

    # def get_meal_names(self):
    #     result = []
    #     for meal in self.shopping_cart:
    #         current_name = meal.name
    #         result.append(current_name)
    #     return f"{', '.join(result)}"

