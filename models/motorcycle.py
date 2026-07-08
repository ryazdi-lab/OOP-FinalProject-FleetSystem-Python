from models.vehicle import Vehicle
from models.mixins import Rentable, Insurable

class Motorcycle(Vehicle, Rentable, Insurable):
    def __init__(self, license_plate: str, brand: str, year: int, base_rate: float, engine_cc: int):
        super().__init__(license_plate, brand, year, base_rate)
        self.engine_cc = engine_cc
        self._reserved = False
        self._base_rate = base_rate
        self._brand = brand
        self._license_plate = license_plate

    def calculate_daily_cost(self) -> float:
        age_factor = 1 + (2026 - self.year) / 200
        return round(self._base_rate * age_factor * 1.1, 2)

    def get_vehicle_type(self) -> str:
        return "موتورسیکلت"

    def perform_maintenance(self) -> None:
        print(f" موتورسیکلت {self._brand} با پلاک ({self._license_plate}) به برسی زنجیر و تعویض روغن موتور نیاز دارد.")

    def calculate_rent(self, days: int) -> float:
        return round(self.calculate_daily_cost() * days * 1.05, 2)

    def reserve(self) -> None:
        if not self._reserved:
            self._reserved = True
            print(f"✅ موتورسیکلت {self._brand} با پلاک ({self._license_plate}) رزرو شد.")
        else:
            print(f"⚠️ موتورسیکلت {self._brand} قبلاً رزرو شده است.")

    def return_vehicle(self) -> None:
        if self._reserved:
            self._reserved = False
            print(f" موتورسیکلت {self._brand} با پلاک ({self._license_plate}) برگردانده شد.")
        else:
            print(f" موتورسیکلت {self._brand} در حال حاضر رزرو نیست.")

    def calculate_insurance_premium(self) -> float:
        return round(self._base_rate * (self.engine_cc / 100) * (1 + (2026 - self.year) / 100), 2)

    def is_eligible_for_coverage(self) -> bool:
        return self.engine_cc <= 500