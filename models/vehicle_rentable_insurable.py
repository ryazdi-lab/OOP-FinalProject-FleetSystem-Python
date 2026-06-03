from models.vehicle_insurable import VehicleInsurable
from models.vehicle_rentable import VehicleRentable
from typing import Any


class VehicleRentableInsurable(VehicleRentable, VehicleInsurable):
    def __init__(self, plate_number: str, brand: str, year: int, base_daily_rate: float, daily_rent: float, insurance_premium_multiplier: float, coverage_eligibility: bool, **kwargs: Any):
        super().__init__(plate_number, brand, year, base_daily_rate, daily_rent=daily_rent,
                         insurance_premium_multiplier=insurance_premium_multiplier, coverage_eligibility=coverage_eligibility, **kwargs)
