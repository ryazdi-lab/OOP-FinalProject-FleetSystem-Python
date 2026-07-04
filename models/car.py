from datetime import date

from .vehicle import Vehicle
from .mixins import Rentable, Insurable

DAILY_OPERATING_COST: float = 8.0
VALID_DOOR_COUNTS: tuple[int, ...] = (2, 3, 4, 5)
INSURANCE_PREMIUM_RATE: float = 0.03
MAX_INSURABLE_AGE_YEARS: int = 15


class Car(Vehicle, Rentable, Insurable):
    def __init__(
        self,
        plate_number: str,
        brand: str,
        year: int,
        base_daily_rate: float,
        num_doors: int,
        insurance_value: float,
    ) -> None:
        super().__init__(plate_number, brand, year, base_daily_rate)
        self.num_doors = num_doors
        self.insurance_value = insurance_value
        self._is_reserved: bool = False

    @property
    def num_doors(self) -> int:
        return self._num_doors

    @num_doors.setter
    def num_doors(self, value: int) -> None:
        if value not in VALID_DOOR_COUNTS:
            raise ValueError("Door count must be between 2 and 5.")
        self._num_doors = value

    @property
    def insurance_value(self) -> float:
        return self._insurance_value

    @insurance_value.setter
    def insurance_value(self, value: float) -> None:
        if value < 0:
            raise ValueError("Insurance value cannot be negative.")
        self._insurance_value = value

    @property
    def is_reserved(self) -> bool:
        return self._is_reserved

    def calculate_daily_cost(self) -> float:
        return DAILY_OPERATING_COST

    def get_vehicle_type(self) -> str:
        return "Car"

    def perform_maintenance(self) -> None:
        print(f"Maintenance completed for car {self.plate_number}.")

    def calculate_rent(self, days: int) -> float:
        if days <= 0:
            raise ValueError("Days must be positive.")
        return self.base_daily_rate * days

    def reserve(self) -> None:
        if self._is_reserved:
            raise RuntimeError(f"Car {self.plate_number} is already reserved.")
        self._is_reserved = True

    def return_vehicle(self, actual_days: int) -> None:
        if not self._is_reserved:
            raise RuntimeError(f"Car {self.plate_number} was not reserved.")
        if actual_days <= 0:
            raise ValueError("Actual days must be positive.")
        self._is_reserved = False

    def calculate_insurance_premium(self) -> float:
        return self.insurance_value * INSURANCE_PREMIUM_RATE

    def is_eligible_for_coverage(self) -> bool:
        age: int = date.today().year - self.year
        return age <= MAX_INSURABLE_AGE_YEARS
