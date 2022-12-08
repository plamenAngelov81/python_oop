class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        name = f"{stars_count} stars Hotel"
        return cls(name)

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for r in self.rooms:
            if r.number == room_number:
                r.take_room(people)
                self.guests += people

    def free_room(self, room_number):
        for room in self.rooms:
            if room.number == room_number:
                self.guests -= room.guests
                room.free_room()

    def status(self):
        occupied = set()
        available = set()
        for r in self.rooms:
            if r.is_taken:
                occupied.add(r.number)
            else:
                available.add(r.number)
        return (f"Hotel {self.name} has {self.guests} total guests\n"
                f"Free rooms: {', '.join(str(x) for x in available)}\n"
                f"Taken rooms: {', '.join(str(x) for x in occupied)}")