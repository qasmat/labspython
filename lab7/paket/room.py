from .base import BasePremise

class Room(BasePremise):
    def __init__(self, length: float, width: float, height: float):
        self._length = length
        self._width = width
        self._height = height

    # managed attributes
    @property
    def length(self):
        return self._length

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def total_area(self) -> float:
        return self.length * self.width

    def volume(self) -> float:
        return self.total_area() * self.height

    def total_heat(self) -> float:
        return self.volume() * 40

    def __str__(self):
        return f"Room {self.length}x{self.width}x{self.height}"

    def __repr__(self):
        return f"Room({self.length}, {self.width}, {self.height})"