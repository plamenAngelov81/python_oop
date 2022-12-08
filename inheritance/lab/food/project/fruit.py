from my_tests.project import Food


class Fruit(Food):
    def __init__(self, name, expiration_date):
        self.name = name
        super().__init__(expiration_date)


obj = Fruit("banana", 19)
print(obj.expiration_date)
