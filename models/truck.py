from datetime import date

from .vehicle import Vehicle
from .mixins import Rentable, Insurable

BASE_DAILY_OPERATING_COST: float = 12.0
EXTRA_COST_PER_TON: float = 1.5
KG_PER_TON: float = 1000.0
INSURANCE_PREMIUM_RATE: float = 0.04
INSURANCE_CAPACITY_FEE_PER_TON: float = 5.0
MAX_INSURABLE_AGE_YEARS: int = 20


class Truck(Vehicle, Rentable, Insurable):
    def __init__(
        self,
        plate_number: str,
        brand: str,
        year: int,
        base_daily_rate: float,
        cargo_capacity_kg: float,
        insurance_value: float,
    ) -> None:
        super().__init__(plate_number, brand, year, base_daily_rate)
        self.cargo_capacity_kg = cargo_capacity_kg
        self.insurance_value = insurance_value
        self._is_reserved: bool = False
        self._current_load_kg: float = 0.0

    @property
    def cargo_capacity_kg(self) -> float:
        return self._cargo_capacity_kg

    @cargo_capacity_kg.setter
    def cargo_capacity_kg(self, value: float) -> None:
        if value <= 0:
            raise ValueError("Cargo capacity must be positive.")
        self._cargo_capacity_kg = value

    @property
    def insurance_value(self) -> float:
        return self._insurance_value

    @insurance_value.setter
    def insurance_value(self, value: float) -> None:
        if value < 0:
            raise ValueError("Insurance value cannot be negative.")
        self._insurance_value = value

    @property
    def current_load_kg(self) -> float:
        return self._current_load_kg

    # وضعیت بار فقط از طریق این دو متد تغییر می‌کند، نه مستقیم.
    def load_cargo(self, weight_kg: float) -> None:
        if weight_kg < 0:
            raise ValueError("Weight cannot be negative.")
        if self._current_load_kg + weight_kg > self._cargo_capacity_kg:
            raise ValueError("Load exceeds truck capacity.")
        self._current_load_kg += weight_kg

    def unload_cargo(self) -> None:
        self._current_load_kg = 0.0

    def calculate_daily_cost(self) -> float:
        load_tons: float = self._current_load_kg / KG_PER_TON
        return BASE_DAILY_OPERATING_COST + (load_tons * EXTRA_COST_PER_TON)

    def get_vehicle_type(self) -> str:
        return "Truck"

    def perform_maintenance(self) -> None:
        print(f"Maintenance completed for truck {self.plate_number}.")

    def calculate_rent(self, days: int) -> float:
        if days <= 0:
            raise ValueError("Days must be positive.")
        return self.base_daily_rate * days

    def reserve(self) -> None:
        if self._is_reserved:
            raise RuntimeError(f"Truck {self.plate_number} is already reserved.")
        self._is_reserved = True

    def return_vehicle(self, actual_days: int) -> None:
        if not self._is_reserved:
            raise RuntimeError(f"Truck {self.plate_number} was not reserved.")
        if actual_days <= 0:
            raise ValueError("Actual days must be positive.")
        self._is_reserved = False

    def calculate_insurance_premium(self) -> float:
        capacity_factor: float = self.cargo_capacity_kg / KG_PER_TON
        return (self.insurance_value * INSURANCE_PREMIUM_RATE) + (
            capacity_factor * INSURANCE_CAPACITY_FEE_PER_TON
        )

    def is_eligible_for_coverage(self) -> bool:
        age: int = date.today().year - self.year
        return age <= MAX_INSURABLE_AGE_YEARS
