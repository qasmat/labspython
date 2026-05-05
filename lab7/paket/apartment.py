from .base import BasePremise
from .room import Room

class Apartment(BasePremise):
    def __init__(self):
        self._rooms: list[Room] = []

    @property
    def rooms(self):
        return self._rooms

    def add_room(self, room: Room):
        self._rooms.append(room)

    def total_area(self) -> float:
        return sum(r.total_area() for r in self.rooms)

    def total_heat(self) -> float:
        return sum(r.total_heat() for r in self.rooms)

    def __len__(self):
        return len(self.rooms)

    def __str__(self):
        return f"Apartment with {len(self)} rooms"

    def __repr__(self):
        return f"Apartment({len(self)} rooms)"