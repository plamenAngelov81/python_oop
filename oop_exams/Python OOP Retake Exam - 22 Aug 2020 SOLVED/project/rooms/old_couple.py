from project.appliances.fridge import Fridge
from project.appliances.stove import Stove
from project.appliances.tv import TV
from project.rooms.room import Room


class OldCouple(Room):
    default_room_members_count = 2
    room_cost = 15
    appliance_types = (TV, Fridge, Stove)

    def __init__(self, name: str, pension_one: float, pension_two: float):
        super().__init__(name, pension_one + pension_two, self.default_room_members_count)
        self.calculate_expenses(self.appliances)