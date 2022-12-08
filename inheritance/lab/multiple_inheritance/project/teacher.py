from my_tests.project import Employee
from my_tests.project import Person


class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."


