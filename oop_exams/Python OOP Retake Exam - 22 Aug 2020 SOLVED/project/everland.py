from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    @property
    def total_population(self):
        return sum(room.members_count for room in self.rooms)

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = sum(room.total_expenses for room in self.rooms)
        return f'Monthly consumption: {total_consumption:.2f}$'

    def pay(self):
        room_results = [self.__pay_for__room(room) for room in self.rooms]
        return '\n'.join(room_results)

    def status(self):
        rooms_results = [str(room) for room in self.rooms]
        result = [
            f'Total population: {self.total_population}',
            *rooms_results,
        ]

        return '\n'.join(result)

    def __pay_for__room(self, room: Room):
        if room.budget < room.total_expenses:
            self.__remove_room(room)
            return f'{room.family_name} does not have enough budget and must leave the hotel.'

        room.budget -= room.total_expenses
        return f'{room.family_name} paid {room.total_expenses:.2f}$ and have {room.budget:.2f}$ left.'

    def __remove_room(self, room):
        self.rooms.remove(room)
