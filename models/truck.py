from models.vehicle import Vehicle
from models.mixins import Insurable

class Truck(Vehicle, Insurable):
    def __init__(self, license_plate: str, brand: str, year: int, base_rate: float, cargo_capacity_ton: float):
        super().__init__(license_plate, brand, year, base_rate)
        self.cargo_capacity_ton = cargo_capacity_ton
        self._base_rate = base_rate
        self._brand = brand
        self._license_plate = license_plate

    def calculate_daily_cost(self) -> float:
        age_factor = 1 + (2026 - self.year) / 80
        return round(self._base_rate * age_factor * 1.5, 2)

    def get_vehicle_type(self) -> str:
        return "کامیون"

    def perform_maintenance(self) -> None:
        print(f" کامیون {self._brand} با پلاک ({self._license_plate}) به برسی ترمز و روغن‌کاری نیاز دارد.")

    def calculate_insurance_premium(self) -> float:
        return round(self._base_rate * self.cargo_capacity_ton * (1 + (2026 - self.year) / 100), 2)

    def is_eligible_for_coverage(self) -> bool:
        return self.cargo_capacity_ton < 20.0