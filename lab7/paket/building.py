from .base import BasePremise
from .apartment import Apartment

class Building(BasePremise):
    def __init__(self):
        self._apartments: list[Apartment] = []

    @property
    def apartments(self):
        return self._apartments

    def add_apartment(self, apartment: Apartment):
        self._apartments.append(apartment)

    def total_area(self) -> float:
        return sum(a.total_area() for a in self.apartments)

    def total_heat(self) -> float:
        return sum(a.total_heat() for a in self.apartments)

    def __len__(self):
        return len(self.apartments)

    def __str__(self):
        return f"Building with {len(self)} apartments"

    def __repr__(self):
        return f"Building({len(self)} apartments)"