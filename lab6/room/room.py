class Room:
    def init(self, length: float, width: float, height: float):
        self.length = length
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.length * self.width

    def volume(self) -> float:
        return self.area() * self.height

    def heat_power(self, k: float = 40) -> float:
        # k — удельная тепловая характеристика (Вт/м³)
        return self.volume() * k