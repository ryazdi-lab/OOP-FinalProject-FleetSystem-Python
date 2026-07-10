from .vehicle import Vehicle
from .mixins import Rentable, Insurable


class Car(Vehicle, Rentable, Insurable):
    def __init__(self, plate_number: str, brand: str, year: int, base_daily_rate: float, door_count: int):
        super().__init__(plate_number, brand, year, base_daily_rate)
        self.door_count = door_count
        self._reserved_status = False

    @property
    def door_count(self) -> int:
        return self._door_count

    @door_count.setter
    def door_count(self, value: int) -> None:
        if value < 2:
            raise ValueError("تعداد درب‌ها نمی‌تواند کمتر از ۲ باشد.")
        self._door_count = value

    def calculate_daily_cost(self) -> float:
        return self.base_daily_rate + (self.door_count * 45000)

    def get_vehicle_type(self) -> str:
        return "خودرو سواری"

    def perform_maintenance(self) -> None:
        print(f"انجام سرویس دوره‌ای خودرو {self.brand} با پلاک {self.plate_number}...")

    def calculate_rent(self, days: int) -> float:
        if days <= 0:
            raise ValueError("مدت اجاره باید بیشتر از صفر باشد.")
        return days * self.calculate_daily_cost()

    def reserve(self) -> None:
        if self._reserved_status:
            print(f"خودرو {self.brand} قبلاً رزرو شده است.")
        else:
            self._reserved_status = True
            print(f"خودرو {self.brand} با موفقیت رزرو شد.")

    def return_vehicle(self, actual_days: int) -> None:
        self._reserved_status = False
        total_cost = self.calculate_rent(actual_days)
        print(f"خودرو بازگردانده شد. هزینه کل: {total_cost}")

    def calculate_insurance_premium(self) -> float:
        return 1200000 if self.year >= 2021 else 2200000

    def is_eligible_for_coverage(self) -> bool:
        return self.year >= 1998