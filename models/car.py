from datetime import date

from models.mixins import Insurable, Rentable
from models.vehicle import Vehicle


class Car(Vehicle, Rentable, Insurable):
    DAILY_COST_FACTOR = 1.10
    MONTHLY_INSURANCE_RATE = 0.08
    MAX_INSURANCE_AGE = 15
    DEFAULT_PASSENGER_CAPACITY = 5

    def __init__(
        self,
        plate_number: str,
        brand: str,
        year: int,
        base_daily_rate: float,
        passenger_capacity: int = DEFAULT_PASSENGER_CAPACITY,
    ) -> None:
        super().__init__(plate_number, brand, year, base_daily_rate)
        self.passenger_capacity = passenger_capacity
        self._is_reserved = False

    @property
    def passenger_capacity(self) -> int:
        return self._passenger_capacity

    @passenger_capacity.setter
    def passenger_capacity(self, value: int) -> None:
        if not 1 <= value <= 8:
            raise ValueError("ظرفیت سرنشین خودرو باید بین 1 تا 8 باشد.")
        self._passenger_capacity = value

    @property
    def is_reserved(self) -> bool:
        return self._is_reserved

    def calculate_daily_cost(self) -> float:
        return round(self.base_daily_rate * self.DAILY_COST_FACTOR, 2)

    def get_vehicle_type(self) -> str:
        return "Car"

    def perform_maintenance(self) -> None:
        print("سرویس خودرو: بررسی روغن، ترمزها و فشار باد تایرها")

    def calculate_rent(self, days: int) -> float:
        if days <= 0:
            raise ValueError("تعداد روزهای اجاره باید یک عدد صحیح مثبت باشد.")
        return round(self.calculate_daily_cost() * days, 2)

    def reserve(self) -> None:
        if self.is_reserved:
            print("این خودرو قبلاً رزرو شده است.")
            return

        self._is_reserved = True
        print(f"خودروی {self.plate_number} رزرو شد.")

    def return_vehicle(self, actual_days: int) -> None:
        if actual_days <= 0:
            raise ValueError("تعداد روزهای اجاره باید یک عدد صحیح مثبت باشد.")

        if not self.is_reserved:
            print("این خودرو در حال حاضر رزرو نیست.")
            return

        total_cost = self.calculate_rent(actual_days)
        self._is_reserved = False
        print(f"خودرو بازگردانده شد. هزینه نهایی: {total_cost:.2f}")

    def calculate_insurance_premium(self) -> float:
        monthly_value = self.calculate_daily_cost() * 30
        return round(monthly_value * self.MONTHLY_INSURANCE_RATE, 2)

    def is_eligible_for_coverage(self) -> bool:
        vehicle_age = date.today().year - self.year
        return vehicle_age <= self.MAX_INSURANCE_AGE
