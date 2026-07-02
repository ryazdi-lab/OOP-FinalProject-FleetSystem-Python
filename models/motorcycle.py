from models.vehicle import Vehicle
from models.mixins import Rentable


class Motorcycle(Vehicle, Rentable):
    def __init__(
        self,
        plate_number: str,
        brand: str,
        year: int,
        base_daily_rate: float,
    ) -> None:
        super().__init__(plate_number, brand, year, base_daily_rate)
        self._reserved = False

    def calculate_daily_cost(self) -> float:
        return self.base_daily_rate * 0.90

    def get_vehicle_type(self) -> str:
        return "Motorcycle"

    def perform_maintenance(self) -> None:
        print("Motorcycle maintenance completed.")

    def calculate_rent(self, days: int) -> float:
        if days <= 0:
            raise ValueError("Days must be positive.")
        return self.calculate_daily_cost() * days

    def reserve(self) -> None:
        self._reserved = True
        print("Motorcycle reserved.")

    def return_vehicle(self, actual_days: int) -> None:
        self._reserved = False
        print(
            f"Motorcycle returned. Total cost: "
            f"{self.calculate_rent(actual_days):.2f}"
        )