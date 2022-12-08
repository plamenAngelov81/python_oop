class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.cars = ["M5", "Gemera"]

    def get_full_name(self):
        result = f"{self.first_name} {self.last_name}"
        return result

    def get_person_info(self):
        result = f"{self.first_name} {self.last_name} is {self.age} years old."
        return result

    def car_like(self, car_model):
        if car_model not in self.cars:
            raise Exception("I not like this car")
        return f"This {car_model} is the best"



