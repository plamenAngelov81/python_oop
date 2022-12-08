from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    def __init__(self, name, speed):
        super().__init__(name, speed)

    def train(self):
        if self.speed + 3 > 140:
            self.speed = 140
        else:
            self.speed += 3

    @property
    def max_speed_limit(self):
        return 140
