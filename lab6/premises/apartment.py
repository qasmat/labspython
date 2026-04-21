from .room import Room

class Apartment:
    def __init__(self):
        self.rooms: list[Room] = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def total_area(self) -> float:
        return sum(room.area() for room in self.rooms)

    def total_heat(self) -> float:
        return sum(room.heat_power() for room in self.rooms)