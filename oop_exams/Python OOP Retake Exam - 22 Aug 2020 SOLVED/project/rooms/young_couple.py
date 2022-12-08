from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCouple(Room):
    default_room_members_count = 2
    room_cost = 20
    appliance_types = (TV, Fridge, Laptop)

    def __init__(self, name: str, salary_one: float, salary_two: float):
        super().__init__(name, salary_one + salary_two, self.default_room_members_count)
        self.calculate_expenses(self.appliances)
