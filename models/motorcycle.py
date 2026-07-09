from datetime import date

from models.vehicle import Vehicle
from models.mixins import Rentable, Insurable

MOTORCYCLE_INSURANCE_RISK_MULTIPLIER = 0.035
MOTORCYCLE_MIN_ENGINE_CC_FOR_COVERAGE = 125
MOTORCYCLE_MAX_INSURABLE_AGE_YEARS = 10
MOTORCYCLE_HELMET_DEPOSIT = 20.0


class Motorcycle(Vehicle, Rentable, Insurable):
    """موتورسیکلت: قابل اجاره روزانه با ریسک بیمه‌ای بالاتر."""

    def __init__(
        self,
        plate_number: str,
        brand: str,
        year: int,
        base_daily_rate: float,
        engine_cc: int,
    ) -> None:
        super().__init__(plate_number, brand, year, base_daily_rate)
        self.engine_cc = engine_cc
        self._is_reserved: bool = False

    @property
    def engine_cc(self) -> int:
        return self._engine_cc

    @engine_cc.setter
    def engine_cc(self, value: int) -> None:
        if not isinstance(value, int) or value <= 0:
            raise ValueError("حجم موتور باید عددی مثبت باشد.")
        self._engine_cc = value

    # --- Abstraction (Vehicle) ---
    def calculate_daily_cost(self) -> float:
        return self.base_daily_rate

    def get_vehicle_type(self) -> str:
        return "موتورسیکلت"

    def perform_maintenance(self) -> None:
        print(f"بررسی زنجیر و روغن موتور {self.plate_number} انجام شد.")

    # --- Rentable ---
    def calculate_rent(self, days: int) -> float:
        if days <= 0:
            raise ValueError("تعداد روزهای اجاره باید مثبت باشد.")
        return round(self.calculate_daily_cost() * days + MOTORCYCLE_HELMET_DEPOSIT, 2)

    def reserve(self) -> None:
        if self._is_reserved:
            raise RuntimeError(f"موتورسیکلت {self.plate_number} از قبل رزرو شده است.")
        self._is_reserved = True
        print(f"رزرو موتورسیکلت {self.plate_number} ثبت شد.")

    def return_vehicle(self, actual_days: int) -> None:
        if not self._is_reserved:
            raise RuntimeError(f"موتورسیکلت {self.plate_number} در حال اجاره نیست.")
        self._is_reserved = False
        print(f"موتورسیکلت {self.plate_number} پس از {actual_days} روز بازگردانده شد.")

    # --- Insurable ---
    def calculate_insurance_premium(self) -> float:
        return round(self.base_daily_rate * 30 * MOTORCYCLE_INSURANCE_RISK_MULTIPLIER, 2)

    def is_eligible_for_coverage(self) -> bool:
        age_ok = (date.today().year - self.year) <= MOTORCYCLE_MAX_INSURABLE_AGE_YEARS
        engine_ok = self.engine_cc >= MOTORCYCLE_MIN_ENGINE_CC_FOR_COVERAGE
        return age_ok and engine_ok