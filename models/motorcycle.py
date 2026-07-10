from .vehicle import Vehicle
from .mixins import Rentable, Insurable


class Motorcycle(Vehicle, Rentable, Insurable):
    def __init__(self, plate_number: str, brand: str, year: int, base_daily_rate: float, engine_capacity: int):
        super().__init__(plate_number, brand, year, base_daily_rate)
        self.engine_capacity = engine_capacity
        self._reserved_flag = False

    @property
    def engine_capacity(self) -> int:
        return self._engine_capacity

    @engine_capacity.setter
    def engine_capacity(self, value: int) -> None:
        if value < 50:
            raise ValueError("حجم موتور باید حداقل ۵۰ سی‌سی باشد.")
        self._engine_capacity = value

    def calculate_daily_cost(self) -> float:
        return self.base_daily_rate + (self.engine_capacity * 110)

    def get_vehicle_type(self) -> str:
        return "موتورسیکلت"

    def perform_maintenance(self) -> None:
        print(f"تعویض روغن و بررسی موتورسیکلت {self.brand} با پلاک {self.plate_number}...")

    def calculate_rent(self, days: int) -> float:
        if days <= 0:
            raise ValueError("تعداد روزها باید مثبت باشد.")
        return days * self.calculate_daily_cost()

    def reserve(self) -> None:
        if self._reserved_flag:
            print(f"موتورسیکلت {self.brand} در حال حاضر رزرو است.")
        else:
            self._reserved_flag = True
            print(f"موتورسیکلت {self.brand} رزرو شد.")

    def return_vehicle(self, actual_days: int) -> None:
        self._reserved_flag = False
        cost = self.calculate_rent(actual_days)
        print(f"موتورسیکلت بازگشت داده شد. هزینه نهایی: {cost}")

    def calculate_insurance_premium(self) -> float:
        premium = 550000
        if self.engine_capacity > 250:
            premium += 350000
        return premium

    def is_eligible_for_coverage(self) -> bool:
        return self.year >= 2004