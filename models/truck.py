from .vehicle import Vehicle
from .mixins import Rentable, Insurable


class Truck(Vehicle, Rentable, Insurable):
    def __init__(self, plate_number: str, brand: str, year: int, base_daily_rate: float, cargo_capacity: float):
        super().__init__(plate_number, brand, year, base_daily_rate)
        self.cargo_capacity = cargo_capacity
        self._rented_out = False

    @property
    def cargo_capacity(self) -> float:
        return self._cargo_capacity

    @cargo_capacity.setter
    def cargo_capacity(self, value: float) -> None:
        if value <= 0:
            raise ValueError("ظرفیت بار باید بزرگ‌تر از صفر باشد.")
        self._cargo_capacity = value

    def calculate_daily_cost(self) -> float:
        return self.base_daily_rate + (self.cargo_capacity * 220000)

    def get_vehicle_type(self) -> str:
        return "کامیون"

    def perform_maintenance(self) -> None:
        print(f"بازرسی فنی کامیون {self.brand} با پلاک {self.plate_number}...")

    def calculate_rent(self, days: int) -> float:
        if days <= 0:
            raise ValueError("تعداد روزها باید بیشتر از صفر باشد.")
        return days * self.calculate_daily_cost()

    def reserve(self) -> None:
        if self._rented_out:
            print(f"کامیون {self.brand} قبلاً رزرو شده است.")
        else:
            self._rented_out = True
            print(f"کامیون {self.brand} با موفقیت رزرو شد.")

    def return_vehicle(self, actual_days: int) -> None:
        self._rented_out = False
        total = self.calculate_rent(actual_days)
        print(f"کامیون بازگردانده شد. هزینه کل: {total}")

    def calculate_insurance_premium(self) -> float:
        return 3200000 + (self.cargo_capacity * 550000)

    def is_eligible_for_coverage(self) -> bool:
        return self.year >= 2008