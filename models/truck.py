from .vehicle import Vehicle
from .mixins import Insurable

class Truck(Vehicle, Insurable):
    def __init__(self, brand: str, model: str, year: int, capacity: int):
        super().__init__(brand, model, year)
        self._capacity = capacity

    def get_insurance_quote(self) -> float:
        return 1000.0 + (self._capacity * 0.5)

    def get_description(self) -> str:
        return f"Truck: {self.brand} {self.model} ({self.year}) - Capacity: {self._capacity}kg"
