from .vehicle import Vehicle
from .mixins import Rentable, Insurable


class Truck(Vehicle, Rentable, Insurable):

    def __init__(
        self,
        plate_number: str,
        brand: str,
        year: int,
        base_daily_rate: float,
        load_capacity: float
    ):
        super().__init__(plate_number, brand, year, base_daily_rate)
        self.load_capacity = load_capacity

    def calculate_daily_cost(self) -> float:
        return self.base_daily_rate + (self.load_capacity * 20)

    def get_vehicle_type(self) -> str:
        return "Truck"

    def perform_maintenance(self) -> None:
        print(f"{self.plate_number}: Truck maintenance completed.")

    def calculate_rent(self, days: int) -> float:
        return self.calculate_daily_cost() * days

    def reserve(self) -> None:
        print(f"{self.plate_number} reserved.")

    def return_vehicle(self, actual_days: int) -> None:
        print(f"{self.plate_number} returned after {actual_days} days.")

    def calculate_insurance_premium(self) -> float:
        return self.base_daily_rate * 0.15

    def is_eligible_for_coverage(self) -> bool:
        return self.year >= 2005