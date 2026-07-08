from models.vehicle import Vehicle
from models.mixins import Rentable

class Car(Vehicle, Rentable):
    def __init__(self, license_plate: str, brand: str, year: int, base_rate: float, doors: int = 4):
        super().__init__(license_plate, brand, year, base_rate)
        self.doors = doors
        self._reserved = False
        self._base_rate = base_rate
        self._brand = brand
        self._license_plate = license_plate

    def calculate_daily_cost(self) -> float:
        age_factor = 1 + (2026 - self.year) / 100
        return round(self._base_rate * age_factor * 1.2, 2)

    def get_vehicle_type(self) -> str:
        return "خودروی سواری"

    def perform_maintenance(self) -> None:
        print(f"  خودروی {self._brand} با پلاک ({self._license_plate}) به تعویض روغن و برسی ترمزها نیاز دارد.")

    def calculate_rent(self, days: int) -> float:
        return round(self.calculate_daily_cost() * days * 1.1, 2)

    def reserve(self) -> None:
        if not self._reserved:
            self._reserved = True
            print(f"✅ خودروی {self._brand} با پلاک ({self._license_plate}) رزرو شد.")
        else:
            print(f"⚠️ خودروی {self._brand} قبلاً رزرو شده است.")

    def return_vehicle(self) -> None:
        if self._reserved:
            self._reserved = False
            print(f" خودروی {self._brand} با پلاک ({self._license_plate}) برگردانده شد.")
        else:
            print(f" خودروی {self._brand} در حال حاضر رزرو نیست.")