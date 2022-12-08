from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    BREATHE = 5

    def __init__(self, name):
        super().__init__(name, 70)

    def breathe(self):
        self.oxygen -= self.BREATHE
