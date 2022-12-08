from project.rooms.room import Room


class AloneOld(Room):
    default_room_members_count = 1
    room_cost = 10

    def __init__(self, name: str, pension: float):
        super().__init__(name, pension, self.default_room_members_count)