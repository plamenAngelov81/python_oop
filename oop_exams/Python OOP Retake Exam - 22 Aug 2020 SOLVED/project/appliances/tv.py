from project.appliances.appliance import Appliance


class TV(Appliance):
    appliance_cost = 1.5

    def __init__(self):
        super().__init__(self.appliance_cost)