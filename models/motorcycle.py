from models.mixins import Rentable
from models.vehicle import Vehicle


class Motorcycle(Vehicle, Rentable):
    DAILY_COST_FACTOR = 0.80
    DEFAULT_ENGINE_CAPACITY = 150

    def __init__(
        self,
        plate_number: str,
        brand: str,
        year: int,
        base_daily_rate: float,
        engine_capacity: int = DEFAULT_ENGINE_CAPACITY,
    ) -> None:
        super().__init__(plate_number, brand, year, base_daily_rate)
        self.engine_capacity = engine_capacity
        self._is_reserved = False

    @property
    def engine_capacity(self) -> int:
        return self._engine_capacity

    @engine_capacity.setter
    def engine_capacity(self, value: int) -> None:
        if value <= 0:
            raise ValueError("حجم موتور باید یک عدد صحیح مثبت باشد.")
        self._engine_capacity = value

    @property
    def is_reserved(self) -> bool:
        return self._is_reserved

    def calculate_daily_cost(self) -> float:
        return round(self.base_daily_rate * self.DAILY_COST_FACTOR, 2)

    def get_vehicle_type(self) -> str:
        return "Motorcycle"

    def perform_maintenance(self) -> None:
        print("سرویس موتورسیکلت: بررسی زنجیر، ترمزها و تایرها")

    def calculate_rent(self, days: int) -> float:
        if days <= 0:
            raise ValueError("تعداد روزهای اجاره باید یک عدد صحیح مثبت باشد.")
        return round(self.calculate_daily_cost() * days, 2)

    def reserve(self) -> None:
        if self.is_reserved:
            print("این موتورسیکلت قبلاً رزرو شده است.")
            return

        self._is_reserved = True
        print(f"موتورسیکلت {self.plate_number} رزرو شد.")

    def return_vehicle(self, actual_days: int) -> None:
        if actual_days <= 0:
            raise ValueError("تعداد روزهای اجاره باید یک عدد صحیح مثبت باشد.")

        if not self.is_reserved:
            print("این موتورسیکلت در حال حاضر رزرو نیست.")
            return

        total_cost = self.calculate_rent(actual_days)
        self._is_reserved = False
        print(f"موتورسیکلت بازگردانده شد. هزینه نهایی: {total_cost:.2f}")
