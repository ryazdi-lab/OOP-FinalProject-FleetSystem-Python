from models.vehicle import Vehicle
from models.mixins import Rentable, Insurable


class Truck(Vehicle, Rentable, Insurable):
    REFRIGERATOR_MULTIPLIER = 1.15
    BASE_INSURANCE_RATE = 0.04
    REFRIGERATOR_INSURANCE_BONUS = 1.1

    def __init__(
        self,
        plate_number: str,
        brand: str,
        year: int,
        base_daily_rate: float,
        cargo_capacity: float,
        has_refrigerator: bool,
        insurance_coverage: float = 15000,
    ):
        super().__init__(plate_number, brand, year, base_daily_rate)
        self.cargo_capacity = cargo_capacity
        self.has_refrigerator = has_refrigerator
        self.insurance_coverage = insurance_coverage
        self._is_rented = False
        self._is_reserved = False

    def calculate_daily_cost(self) -> float:
        if self.has_refrigerator:
            return self.base_daily_rate * self.REFRIGERATOR_MULTIPLIER
        return self.base_daily_rate

    def get_vehicle_type(self) -> str:
        return "Truck"

    def perform_maintenance(self) -> None:
        print(f"Maintenance performed on {self.brand} Truck")

    def calculate_insurance_premium(self) -> float:
        base = self.insurance_coverage * self.BASE_INSURANCE_RATE
        if self.has_refrigerator:
            base *= self.REFRIGERATOR_INSURANCE_BONUS
        return base

    def calculate_rent(self, days: int) -> float:
        return self.calculate_daily_cost() * days

    def is_eligible_for_coverage(self) -> bool:
        return self.cargo_capacity >= 2.0

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
        return f"Coverage: ${self.insurance_coverage} - {'with' if self.has_refrigerator else 'without'} refrigerator"

    def calculate_rental_cost(self, days: int) -> float:
        return self.calculate_daily_cost() * days

    def reserve(self) -> None:
        if self._is_reserved:
            raise ValueError("Vehicle is already reserved")
        self._is_reserved = True

    def __str__(self) -> str:
        return f"Truck: {self.brand} ({self.year}) - {self.cargo_capacity} tons"