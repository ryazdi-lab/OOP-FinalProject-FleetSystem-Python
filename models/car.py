from datetime import date

from models.vehicle import Vehicle
from models.mixins import Rentable, Insurable

LONG_TERM_DISCOUNT_THRESHOLD_DAYS = 7
LONG_TERM_DISCOUNT_RATE = 0.10
CAR_INSURANCE_BASE_RATE = 0.02
CAR_MAX_INSURABLE_AGE_YEARS = 15
CAR_MAX_RENTAL_AGE_YEARS = 20
CAR_MAINTENANCE_MILEAGE_INTERVAL_KM = 10000


class Car(Vehicle, Rentable, Insurable):
    """خودروی سواری: قابل اجاره روزانه و قابل بیمه."""

    def __init__(
        self,
        plate_number: str,
        brand: str,
        year: int,
        base_daily_rate: float,
        seat_count: int,
    ) -> None:
        super().__init__(plate_number, brand, year, base_daily_rate)
        self.seat_count = seat_count
        self._is_reserved: bool = False
        self._odometer_km: float = 0.0

    @property
    def seat_count(self) -> int:
        return self._seat_count

    @seat_count.setter
    def seat_count(self, value: int) -> None:
        if not isinstance(value, int) or not (2 <= value <= 9):
            raise ValueError("تعداد صندلی باید بین ۲ تا ۹ باشد.")
        self._seat_count = value

    # --- Abstraction (Vehicle) ---
    def calculate_daily_cost(self) -> float:
        return self.base_daily_rate

    def get_vehicle_type(self) -> str:
        return "خودرو سواری"

    def perform_maintenance(self) -> None:
        if self._odometer_km >= CAR_MAINTENANCE_MILEAGE_INTERVAL_KM:
            print(f"سرویس دوره‌ای خودرو {self.plate_number} انجام شد (تعویض روغن و فیلتر).")
            self._odometer_km = 0.0
        else:
            print(f"خودرو {self.plate_number} نیازی به سرویس ندارد.")

    # --- Rentable ---
    def calculate_rent(self, days: int) -> float:
        if days <= 0:
            raise ValueError("تعداد روزهای اجاره باید مثبت باشد.")
        total = self.calculate_daily_cost() * days
        if days >= LONG_TERM_DISCOUNT_THRESHOLD_DAYS:
            total *= (1 - LONG_TERM_DISCOUNT_RATE)
        return round(total, 2)

    def reserve(self) -> None:
        car_age = date.today().year - self.year
        if car_age > CAR_MAX_RENTAL_AGE_YEARS:
            raise RuntimeError(
                f"خودرو {self.plate_number} به دلیل قدمت بالای {CAR_MAX_RENTAL_AGE_YEARS} سال قابل اجاره نیست."
            )
        if self._is_reserved:
            raise RuntimeError(f"خودرو {self.plate_number} از قبل رزرو شده است.")
        self._is_reserved = True
        print(f"رزرو خودرو {self.plate_number} ثبت شد.")

    def return_vehicle(self, actual_days: int) -> None:
        if not self._is_reserved:
            raise RuntimeError(f"خودرو {self.plate_number} در حال اجاره نیست.")
        self._is_reserved = False
        self._odometer_km += actual_days * 120  # فرض: میانگین ۱۲۰ کیلومتر در روز
        print(f"خودرو {self.plate_number} پس از {actual_days} روز بازگردانده شد.")

    # --- Insurable ---
    def calculate_insurance_premium(self) -> float:
        return round(self.base_daily_rate * 30 * CAR_INSURANCE_BASE_RATE, 2)

    def is_eligible_for_coverage(self) -> bool:
        return (date.today().year - self.year) <= CAR_MAX_INSURABLE_AGE_YEARS