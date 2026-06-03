from models.vehicle_generic import VehicleGeneric
from models.mixins import Insurable
from typing import Any


class VehicleInsurable(VehicleGeneric, Insurable):
    def __init__(self, plate_number: str, brand: str, year: int, base_daily_rate: float, insurance_premium_multiplier: float, coverage_eligibility: bool, **kwargs: Any):
        super().__init__(plate_number, brand, year, base_daily_rate, **kwargs)
        self._insurance_premium_multiplier = insurance_premium_multiplier
        self._coverage_eligibility = coverage_eligibility

    @property
    def insurance_premium_multiplier(self) -> float:
        return self._insurance_premium_multiplier

    @insurance_premium_multiplier.setter
    def insurance_premium_multiplier(self, value: float) -> None:
        if value > 0:
            self._insurance_premium_multiplier = value
        else:
            print("insurance_premium_multiplier must be a positive number")

    @property
    def coverage_eligibility(self) -> bool:
        return self._coverage_eligibility

    @coverage_eligibility.setter
    def coverage_eligibility(self, value: bool) -> None:
        self._coverage_eligibility = value

    def calculate_daily_cost(self) -> float:
        return super().calculate_daily_cost() + self.calculate_insurance_premium()/30

    def calculate_insurance_premium(self) -> float:
        return self.base_daily_rate*30*self.insurance_premium_multiplier

    # default behaviour, will suffice for most cases but can be overridden if desired
    def is_eligible_for_coverage(self) -> bool:
        return self.coverage_eligibility

    def display_info(self) -> None:
        super().display_info()
        print(
            f"insurance premium multiplier: {self.insurance_premium_multiplier} | coverage eligibility: {self.coverage_eligibility}")
