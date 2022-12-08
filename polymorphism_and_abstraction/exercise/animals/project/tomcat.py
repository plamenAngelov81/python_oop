from my_tests.project import Cat


class Tomcat(Cat):
    def __init__(self, name, age):
        super().__init__(name, age, "Male")

    def make_sound(self):
        return "Hiss"
