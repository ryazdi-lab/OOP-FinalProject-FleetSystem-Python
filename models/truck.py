from models.vehicle import Vehicle
from models.mixins import Rentable, Insurable


class Truck(Vehicle, Rentable, Insurable):
    def __init__(
        self,
        plate_number: str,
        brand: str,
        year: int,
        base_daily_rate: float,
        load_capacity: float,
    ):
        super().__init__(plate_number, brand, year, base_daily_rate)
        self.load_capacity = load_capacity
        self.is_reserved = False

    @property
    def load_capacity(self) -> float:
        return self._load_capacity

    @load_capacity.setter
    def load_capacity(self, value: float) -> None:
        if value <= 0:
            raise ValueError("ظرفیت بار نامعتبر است.")
        self._load_capacity = value

    def calculate_daily_cost(self) -> float:
        return self.base_daily_rate + (self.load_capacity * 5)

    def get_vehicle_type(self) -> str:
        return "Truck"

    def perform_maintenance(self) -> None:
        print(f"{self.brand} truck maintenance completed.")

    def calculate_rent(self, days: int) -> float:
        return self.calculate_daily_cost() * days

    def reserve(self) -> None:
        self.is_reserved = True

    def return_vehicle(self, actual_days: int) -> None:
        self.is_reserved = False

    def calculate_insurance_premium(self) -> float:
        return self.base_daily_rate * 0.20

    def is_eligible_for_coverage(self) -> bool:
        return self.year >= 2005