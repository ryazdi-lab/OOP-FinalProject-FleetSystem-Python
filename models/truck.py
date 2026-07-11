from datetime import date

from models.mixins import Insurable
from models.vehicle import Vehicle


class Truck(Vehicle, Insurable):
    DAILY_COST_FACTOR = 1.50
    MONTHLY_INSURANCE_RATE = 0.12
    MAX_INSURANCE_AGE = 20
    MAX_INSURABLE_CAPACITY = 30.0
    DEFAULT_LOAD_CAPACITY = 10.0

    def __init__(
        self,
        plate_number: str,
        brand: str,
        year: int,
        base_daily_rate: float,
        load_capacity: float = DEFAULT_LOAD_CAPACITY,
    ) -> None:
        super().__init__(plate_number, brand, year, base_daily_rate)
        self.load_capacity = load_capacity

    @property
    def load_capacity(self) -> float:
        return self._load_capacity

    @load_capacity.setter
    def load_capacity(self, value: float) -> None:
        if value <= 0:
            raise ValueError("ظرفیت بار باید یک عدد مثبت باشد.")
        self._load_capacity = float(value)

    def calculate_daily_cost(self) -> float:
        return round(self.base_daily_rate * self.DAILY_COST_FACTOR, 2)

    def get_vehicle_type(self) -> str:
        return "Truck"

    def perform_maintenance(self) -> None:
        print("سرویس کامیون: بررسی موتور، ترمزها و سیستم حمل بار")

    def calculate_insurance_premium(self) -> float:
        monthly_value = self.calculate_daily_cost() * 30
        return round(monthly_value * self.MONTHLY_INSURANCE_RATE, 2)

    def is_eligible_for_coverage(self) -> bool:
        vehicle_age = date.today().year - self.year
        has_valid_age = vehicle_age <= self.MAX_INSURANCE_AGE
        has_valid_capacity = self.load_capacity <= self.MAX_INSURABLE_CAPACITY
        return has_valid_age and has_valid_capacity
