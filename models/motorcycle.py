from datetime import date

from .vehicle import Vehicle
from .mixins import Insurable

DAILY_OPERATING_COST: float = 4.0
INSURANCE_PREMIUM_RATE: float = 0.05
CC_NORMALIZATION_FACTOR: float = 1000.0
MAX_INSURABLE_AGE_YEARS: int = 10


# موتورسیکلت فقط Insurable است، چون در این ناوگان اجاره داده نمی‌شود.
class Motorcycle(Vehicle, Insurable):
    def __init__(
        self,
        plate_number: str,
        brand: str,
        year: int,
        base_daily_rate: float,
        engine_cc: int,
        insurance_value: float,
    ) -> None:
        super().__init__(plate_number, brand, year, base_daily_rate)
        self.engine_cc = engine_cc
        self.insurance_value = insurance_value

    @property
    def engine_cc(self) -> int:
        return self._engine_cc

    @engine_cc.setter
    def engine_cc(self, value: int) -> None:
        if value <= 0:
            raise ValueError("Engine CC must be positive.")
        self._engine_cc = value

    @property
    def insurance_value(self) -> float:
        return self._insurance_value

    @insurance_value.setter
    def insurance_value(self, value: float) -> None:
        if value < 0:
            raise ValueError("Insurance value cannot be negative.")
        self._insurance_value = value

    def calculate_daily_cost(self) -> float:
        return DAILY_OPERATING_COST

    def get_vehicle_type(self) -> str:
        return "Motorcycle"

    def perform_maintenance(self) -> None:
        print(f"Maintenance completed for motorcycle {self.plate_number}.")

    def calculate_insurance_premium(self) -> float:
        cc_factor: float = 1 + (self.engine_cc / CC_NORMALIZATION_FACTOR)
        return self.insurance_value * INSURANCE_PREMIUM_RATE * cc_factor

    def is_eligible_for_coverage(self) -> bool:
        age: int = date.today().year - self.year
        return age <= MAX_INSURABLE_AGE_YEARS
