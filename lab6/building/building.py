from apartment.apartment import Apartment

class Building:
    def init(self):
        self.apartments: list[Apartment] = []

    def add_apartment(self, apartment: Apartment):
        self.apartments.append(apartment)

    def total_area(self) -> float:
        return sum(a.total_area() for a in self.apartments)

    def total_heat(self) -> float:
        return sum(a.total_heat() for a in self.apartments)