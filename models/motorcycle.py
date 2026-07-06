from models.vehicle import Vehicle
from models.mixins import Rentable


class Motorcycle(Vehicle, Rentable):
    def __init__(
        self,
        vehicle_id: str,
        brand: str,
        model: str,
        year: int,
        rental_rate: float
    ) -> None:
        super().__init__(vehicle_id, brand, model, year)
        self._rental_rate = rental_rate

    @property
    def rental_rate(self) -> float:
        return self._rental_rate

    def calculate_rental_cost(self, hours: int) -> float:
        return self._rental_rate * hours

    def get_description(self) -> str:
        return (
            f"Motorcycle ID: {self.vehicle_id}, "
            f"Brand: {self.brand}, "
            f"Model: {self.model}, "
            f"Year: {self.year}, "
            f"Hourly Rate: {self.rental_rate}"
        )
