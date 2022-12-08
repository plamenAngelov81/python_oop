class Flower:
    def __init__(self, name, water_requirements):
        self.name = name
        self.water_requirements = water_requirements
        self.is_happy = False

    def water(self, quantity):
        if quantity < self.water_requirements:
            self.is_happy = False
        else:
            self.is_happy = True

    def status(self):
        result = ""
        if self.is_happy:
            result += f"{self.name} is happy"
        else:
            result += f"{self.name} is not happy"

        return result


flower = Flower("Lilly", 100)
flower.water(50)
print(flower.status())
flower.water(60)
print(flower.status())
flower.water(100)
print(flower.status())
