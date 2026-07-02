from models.vehicle import Vehicle
from models.mixins import  Insurable

class Motorcycle(Vehicle, Insurable):
    def __init__(self, plate_number: str, brand: str, year: int, base_daily_rate: float):
        super().__init__(plate_number, brand, year, base_daily_rate)

    def calculate_daily_cost(self) -> float:
        return self.base_daily_rate * 0.9

    def get_vehicle_type(self) -> str:
        return "Motorcycle"

    def perform_maintenance(self) -> None:
        print("\nMotorcycle is checking...")
        print("Lights -> checked!")
        print("Brake Pads -> repaired!")
        print("Mirrors -> checked!")
        print("Chain tension -> adjusted!")
        print("Tire Pressure -> checked!")
        print("Done! The Motorcycle is good to go.")

    def calculate_insurance_premium(self) -> float:
        return self.calculate_daily_cost() * 0.2

    def is_eligible_for_coverage(self) -> bool:
        return self.year >= 2000
from models.vehicle import Vehicle
from models.mixins import Rentable


class Motorcycle(Vehicle, Rentable):
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
        self._reserved = False

    def calculate_daily_cost(self) -> float:
        return self.base_daily_rate * 0.90

    def get_vehicle_type(self) -> str:
        return "Motorcycle"

    def perform_maintenance(self) -> None:
        print("بررسی زنجیر، لاستیک و روغن موتور سیکلت.")

    def calculate_rent(self, days: int) -> float:
        return self.calculate_daily_cost() * days

    def reserve(self) -> None:
        self._reserved = True
        print(f"{self.plate_number} رزرو شد.")

    def return_vehicle(self, actual_days: int) -> None:
        self._reserved = False
        cost = self.calculate_rent(actual_days)
        print(f"موتورسیکلت بازگردانده شد. هزینه نهایی: {cost:.2f}")