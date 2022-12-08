from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    def __init__(self, name, speed):
        super().__init__(name, speed)

    def train(self):
        if self.speed + 2 > 120:
            self.speed = 120
        else:
            self.speed += 2

    @property
    def max_speed_limit(self):
        return 120
