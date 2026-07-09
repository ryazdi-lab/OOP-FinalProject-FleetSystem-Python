from models.vehicle import Vehicle
from models.mixins import Rentable, Insurable

class Truck(Vehicle, Rentable, Insurable):
    TRUCK_MULTIPLIER = 1.5
    INSURANCE_RATE = 0.15

    def __init__(self, plate_number: str, brand: str, year: int, base_daily_rate: float, capacity: int):
        super().__init__(plate_number, brand, year, base_daily_rate)
        self.capacity = capacity

    @property
    def capacity(self) -> int:
        return self._capacity

    @capacity.setter
    def capacity(self, value: int) -> None:
        if value <= 0:
            raise ValueError("ظرفیت بار باید مثبت باشد.")
        self._capacity = value

    def calculate_daily_cost(self) -> float:
        return self.base_daily_rate * self.TRUCK_MULTIPLIER

    def get_vehicle_type(self) -> str:
        return "کامیون"

    def perform_maintenance(self) -> None:
        print(f" سرویس کامیون {self.brand} - بررسی موتور و سیستم ترمز")

    def calculate_rent(self, days: int) -> float:
        if days <= 0:
            raise ValueError("تعداد روز باید مثبت باشد")
        return self.calculate_daily_cost() * days

    def reserve(self) -> None:
        print(f" کامیون {self.brand} با پلاک {self.plate_number} رزرو شد.")

    def return_vehicle(self, actual_days: int) -> None:
        print(f" کامیون {self.brand} پس داده شد. مدت استفاده: {actual_days} روز")

    def calculate_insurance_premium(self) -> float:
        return self.base_daily_rate * self.INSURANCE_RATE

    def is_eligible_for_coverage(self) -> bool:
        return self.capacity <= 3000
