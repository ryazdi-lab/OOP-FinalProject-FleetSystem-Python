from models.vehicle import Vehicle
from models.mixins import Rentable, Insurable  # Insurable اضافه شد


class Motorcycle(Vehicle, Rentable, Insurable):
    BIG_ENGINE_MULTIPLIER = 1.2

    def __init__(
        self,
        plate_number: str,
        brand: str,
        year: int,
        base_daily_rate: float,
        engine_cc: int,
        has_abs: bool,
        insurance_coverage: float = 5000,
    ):
        super().__init__(plate_number, brand, year, base_daily_rate)
        self.engine_cc = engine_cc
        self.has_abs = has_abs
        self.insurance_coverage = insurance_coverage
        self._is_rented = False
        self._is_reserved = False

    def calculate_daily_cost(self) -> float:
        if self.engine_cc > 500:
            return self.base_daily_rate * self.BIG_ENGINE_MULTIPLIER
        return self.base_daily_rate

    def get_vehicle_type(self) -> str:
        return "Motorcycle"

    def perform_maintenance(self) -> None:
        print(f"Maintenance performed on {self.brand} Motorcycle")

    def calculate_insurance_premium(self) -> float:
        if self.engine_cc > 500:
            return 500.0
        return 300.0

    def calculate_rent(self, days: int) -> float:
        return self.calculate_daily_cost() * days

    def is_eligible_for_coverage(self) -> bool:
        return self.year >= 2021

    def rent(self) -> None:
        if self._is_rented:
            raise ValueError("Vehicle is already rented")
        self._is_rented = True

    def return_vehicle(self) -> None:
        self._is_rented = False

    def is_available(self) -> bool:
        return not self._is_rented and not self._is_reserved

    def get_insurance_cost(self) -> float:
        return self.calculate_insurance_premium()

    def get_coverage_details(self) -> str:
        return f"Coverage: ${self.insurance_coverage} - {'ABS' if self.has_abs else 'No ABS'}"

    def calculate_rental_cost(self, days: int) -> float:
        return self.calculate_daily_cost() * days

    def reserve(self) -> None:
        if self._is_reserved:
            raise ValueError("Vehicle is already reserved")
        self._is_reserved = True

    def __str__(self) -> str:
        return f"Motorcycle: {self.brand} ({self.year}) - {self.engine_cc}cc"