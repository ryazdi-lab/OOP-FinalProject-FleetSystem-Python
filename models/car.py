from .vehicle import Vehicle
from .mixins import Rentable, Insurable

class Car(Vehicle, Rentable, Insurable):
    def __init__(self, plate_number: str, brand: str, year: int, base_daily_rate: float, num_doors: int):
        super().__init__(plate_number, brand, year, base_daily_rate)
        self.num_doors = num_doors
        self._is_reserved = False

    @property
    def num_doors(self) -> int:
        return self._num_doors

    @num_doors.setter
    def num_doors(self, value: int) -> None:
        if value < 2:
            raise ValueError("تعداد درهای ماشین نمی‌تواند کمتر از ۲ باشد.")
        self._num_doors = value

    def calculate_daily_cost(self) -> float:
        return self.base_daily_rate + (self.num_doors * 50000)

    def get_vehicle_type(self) -> str:
        return "سواری (Car)"

    def perform_maintenance(self) -> None:
        print(f"در حال سرویس دوره‌ای ماشین {self.brand} با پلاک {self.plate_number}...")

    def calculate_rent(self, days: int) -> float:
        if days <= 0:
            raise ValueError("تعداد روزها باید مثبت باشد.")
        return days * self.calculate_daily_cost()

    def reserve(self) -> None:
        if self._is_reserved:
            print("این ماشین از قبل رزرو شده است.")
        else:
            self._is_reserved = True
            print(f"ماشین {self.brand} رزرو شد.")

    def return_vehicle(self, actual_days: int) -> None:
        self._is_reserved = False
        print(f"ماشین با موفقیت بازگردانده شد. هزینه نهایی: {self.calculate_rent(actual_days)}")

    def calculate_insurance_premium(self) -> float:
        return 1000000 if self.year > 2020 else 2000000

    def is_eligible_for_coverage(self) -> bool:
        return self.year >= 2000
