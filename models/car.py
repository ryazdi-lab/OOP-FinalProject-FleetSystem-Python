from models.vehicle import Vehicle
from models.mixins import Rentable, Insurable

class Car(Vehicle, Rentable, Insurable):
    CAR_MULTIPLIER = 1.2
    INSURANCE_RATE = 0.1

    def __init__(self, plate_number: str, brand: str, year: int, base_daily_rate: float, doors: int = 4):
        super().__init__(plate_number, brand, year, base_daily_rate)
        self.doors = doors

    @property
    def doors(self) -> int:
        return self._doors

    @doors.setter
    def doors(self, value: int) -> None:
        if value not in [2, 3, 4, 5]:
            raise ValueError("تعداد درب ها باید بین ۲ تا ۵ باشد.")
        self._doors = value

    def calculate_daily_cost(self) -> float:
        return self.base_daily_rate * self.CAR_MULTIPLIER

    def get_vehicle_type(self) -> str:
        return "خودرو"

    def perform_maintenance(self) -> None:
        print(f" سرویس خودرو {self.brand} - تعویض روغن و بررسی ترمزها")

    def calculate_rent(self, days: int) -> float:
        if days <= 0:
            raise ValueError("تعداد روز باید مثبت باشد")
        return self.calculate_daily_cost() * days

    def reserve(self) -> None:
        print(f" خودرو {self.brand} با پلاک {self.plate_number} رزرو شد.")

    def return_vehicle(self, actual_days: int) -> None:
        print(f" خودرو {self.brand} پس داده شد. مدت استفاده: {actual_days} روز")

    def calculate_insurance_premium(self) -> float:
        return self.base_daily_rate * self.INSURANCE_RATE

    def is_eligible_for_coverage(self) -> bool:
        return self.year >= 2005
