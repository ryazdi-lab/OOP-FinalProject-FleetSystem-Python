from .vehicle import Vehicle
from .mixins import Rentable, Insurable

class Motorcycle(Vehicle, Rentable, Insurable):
    def __init__(self, plate_number: str, brand: str, year: int, base_daily_rate: float, engine_cc: int):
        super().__init__(plate_number, brand, year, base_daily_rate)
        self.engine_cc = engine_cc
        self._is_reserved = False

    @property
    def engine_cc(self) -> int:
        return self._engine_cc

    @engine_cc.setter
    def engine_cc(self, value: int) -> None:
        if value < 50:
            raise ValueError("حجم موتور غیرمجاز است (حداقل ۵۰ سی‌سی).")
        self._engine_cc = value

    def calculate_daily_cost(self) -> float:
        return self.base_daily_rate + (self.engine_cc * 100)

    def get_vehicle_type(self) -> str:
        return "موتورسیکلت (Motorcycle)"

    def perform_maintenance(self) -> None:
        print(f"در حال آچارکشی و تعویض روغن موتور {self.brand} با پلاک {self.plate_number}...")

    def calculate_rent(self, days: int) -> float:
        if days <= 0:
            raise ValueError("تعداد روزهای اجاره باید مثبت باشد.")
        return days * self.calculate_daily_cost()

    def reserve(self) -> None:
        if self._is_reserved:
            print("این موتور در حال حاضر رزرو شده است.")
        else:
            self._is_reserved = True
            print(f"موتورسیکلت {self.brand} با موفقیت رزرو شد.")

    def return_vehicle(self, actual_days: int) -> None:
        self._is_reserved = False
        print(f"موتورسیکلت بازگردانده شد. هزینه نهایی اجاره: {self.calculate_rent(actual_days)}")

    def calculate_insurance_premium(self) -> float:
        base_insurance = 500000
        if self.engine_cc > 250:
            base_insurance += 300000
        return base_insurance

    def is_eligible_for_coverage(self) -> bool:
        return self.year >= 2005