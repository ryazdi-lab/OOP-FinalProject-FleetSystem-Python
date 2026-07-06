from models.vehicle import Vehicle
from models.mixins import Rentable, Insurable


class Car(Vehicle, Rentable, Insurable):
    ELECTRIC_DISCOUNT = 0.9
    STANDARD_INSURANCE_RATE = 0.035
    ELECTRIC_INSURANCE_RATE = 0.02

    def __init__(
        self,
        plate_number: str,
        brand: str,
        year: int,
        base_daily_rate: float,
        num_doors: int,
        is_electric: bool,
        insurance_coverage: float = 10000,
    ):
        super().__init__(plate_number, brand, year, base_daily_rate)
        self.num_doors = num_doors
        self.is_electric = is_electric
        self.insurance_coverage = insurance_coverage
        self._is_rented = False
        self._is_reserved = False

    def calculate_daily_cost(self) -> float:
        if self.is_electric:
            return self.base_daily_rate * self.ELECTRIC_DISCOUNT
        return self.base_daily_rate

    def get_vehicle_type(self) -> str:
        return "Car"

    def perform_maintenance(self) -> None:
        print(f"Maintenance performed on {self.brand} Car")

    def calculate_insurance_premium(self) -> float:
        if self.is_electric:
            return self.insurance_coverage * self.ELECTRIC_INSURANCE_RATE
        return self.insurance_coverage * self.STANDARD_INSURANCE_RATE

    def calculate_rent(self, days: int) -> float:
        return self.calculate_daily_cost() * days

    def is_eligible_for_coverage(self) -> bool:
        return self.year >= 2020

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
        return f"Coverage: ${self.insurance_coverage} - {'Electric' if self.is_electric else 'Standard'} rate"

    def calculate_rental_cost(self, days: int) -> float:
        return self.calculate_daily_cost() * days

    def reserve(self) -> None:
        if self._is_reserved:
            raise ValueError("Vehicle is already reserved")
        self._is_reserved = True

    def __str__(self) -> str:
        return f"Car: {self.brand} ({self.year}) - {self.num_doors} doors"