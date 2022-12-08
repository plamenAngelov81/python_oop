from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    BREATHE = 15

    def __init__(self, name):
        super().__init__(name, 90)

    def breathe(self):
        self.oxygen -= self.BREATHE
