from models.vehicle import Vehicle
from models.mixins import Rentable, Insurable

class Motorcycle(Vehicle, Rentable, Insurable):
    MOTORCYCLE_DISCOUNT = 0.9
    INSURANCE_RATE = 0.08

    def __init__(self, plate_number: str, brand: str, year: int, base_daily_rate: float, cylinders: int):
        super().__init__(plate_number, brand, year, base_daily_rate)
        self.cylinders = cylinders

    @property
    def cylinders(self) -> int:
        return self._cylinders

    @cylinders.setter
    def cylinders(self, value: int) -> None:
        if not 1 <= value <= 4:
            raise ValueError("تعداد سیلندر باید بین ۱ تا ۴ باشد.")
        self._cylinders = value

    def calculate_daily_cost(self) -> float:
        return self.base_daily_rate * self.MOTORCYCLE_DISCOUNT

    def get_vehicle_type(self) -> str:
        return "موتورسیکلت"

    def perform_maintenance(self) -> None:
        print(f" سرویس موتور {self.brand} - تنظیم کاربراتور و تعویض روغن")

    def calculate_rent(self, days: int) -> float:
        if days <= 0:
            raise ValueError("تعداد روز باید مثبت باشد")
        return self.calculate_daily_cost() * days

    def reserve(self) -> None:
        print(f" موتورسیکلت {self.brand} با پلاک {self.plate_number} رزرو شد.")

    def return_vehicle(self, actual_days: int) -> None:
        print(f" موتورسیکلت {self.brand} پس داده شد. مدت استفاده: {actual_days} روز")

    def calculate_insurance_premium(self) -> float:
        return self.base_daily_rate * self.INSURANCE_RATE

    def is_eligible_for_coverage(self) -> bool:
        return self.cylinders <= 2



