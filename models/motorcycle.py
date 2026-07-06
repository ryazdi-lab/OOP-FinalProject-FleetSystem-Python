from .vehicle import Vehicle
from .mixins import Rentable, Insurable


class Motorcycle(Vehicle, Rentable, Insurable):

    def __init__(
        self,
        plate_number: str,
        brand: str,
        year: int,
        base_daily_rate: float,
        engine_cc: int
    ):
        super().__init__(plate_number, brand, year, base_daily_rate)
        self.engine_cc = engine_cc

    def calculate_daily_cost(self) -> float:
        return self.base_daily_rate + (self.engine_cc / 20)

    def get_vehicle_type(self) -> str:
        return "Motorcycle"

    def perform_maintenance(self) -> None:
        print(f"{self.plate_number}: Motorcycle maintenance completed.")

    def calculate_rent(self, days: int) -> float:
        return self.calculate_daily_cost() * days

    def reserve(self) -> None:
        print(f"{self.plate_number} reserved.")

    def return_vehicle(self, actual_days: int) -> None:
        print(f"{self.plate_number} returned after {actual_days} days.")

    def calculate_insurance_premium(self) -> float:
        return self.base_daily_rate * 0.08

    def is_eligible_for_coverage(self) -> bool:
        return self.year >= 2005