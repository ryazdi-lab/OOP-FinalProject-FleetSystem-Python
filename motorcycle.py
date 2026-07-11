from models.vehicle import Vehicle
from models.mixins import Rentable, Insurable


class Motorcycle(Vehicle, Rentable, Insurable):
    def __init__(
        self,
        plate_number: str,
        brand: str,
        year: int,
        base_daily_rate: float,
        engine_volume: int = 150,
    ):
        super().__init__(plate_number, brand, year, base_daily_rate)
        self.engine_volume = engine_volume

    def calculate_daily_cost(self) -> float:
        return self.base_daily_rate + (self.engine_volume * 0.02)

    def get_vehicle_type(self) -> str:
        return "Motorcycle"

    def perform_maintenance(self) -> None:
        print("Motorcycle maintenance completed.")

    def calculate_rent(self, days: int) -> float:
        return self.calculate_daily_cost() * days

    def reserve(self) -> None:
        print("Motorcycle reserved.")

    def return_vehicle(self, actual_days: int) -> None:
        print(f"Motorcycle returned after {actual_days} days.")

    def calculate_insurance_premium(self) -> float:
        return self.base_daily_rate * 0.10

    def is_eligible_for_coverage(self) -> bool:
        return self.year >= 2000