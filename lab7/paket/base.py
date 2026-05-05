from abc import ABC, abstractmethod

class BasePremise(ABC):
    @abstractmethod
    def total_area(self) -> float:
        pass

    @abstractmethod
    def total_heat(self) -> float:
        pass

    def __str__(self):
        return f"Area: {self.total_area():.2f}, Heat: {self.total_heat():.2f}"

    def __repr__(self):
        return f"<{self.__class__.__name__}>"