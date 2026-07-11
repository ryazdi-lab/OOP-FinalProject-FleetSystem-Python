from models.vehicle import Vehicle
from models.mixins import Rentable, Insurable

# Car implementation
class Car(Vehicle, Rentable, Insurable):
    def __init__(
        self,
        plate_number: str,
        brand: str,
        year: int,
        base_daily_rate: float,
        seats: int = 5,
    ):
        super().__init__(plate_number, brand, year, base_daily_rate)
        self.seats = seats

    def calculate_daily_cost(self) -> float:
        return self.base_daily_rate + (self.seats * 10)

    def get_vehicle_type(self) -> str:
        return "Car"

    def perform_maintenance(self) -> None:
        print("Car maintenance completed.")

    def calculate_rent(self, days: int) -> float:
        return self.calculate_daily_cost() * days

    def reserve(self) -> None:
        print("Car reserved.")

    def return_vehicle(self, actual_days: int) -> None:
        print(f"Car returned after {actual_days} days.")

    def calculate_insurance_premium(self) -> float:
        return self.base_daily_rate * 0.15

    def is_eligible_for_coverage(self) -> bool:
        return self.year >= 2000
