from abc import ABC, abstractmethod
from datetime import date


class Vehicle(ABC):
    def __init__(self, plate_number: str, brand: str, year: int, base_daily_rate: float):
        # استفاده از Property Setter برای اعتبارسنجی اولیه
        self.plate_number = plate_number
        self.brand = brand
        self.year = year
        self.base_daily_rate = base_daily_rate

    # 🔹 Encapsulation + Validation via Properties
    @property
    def plate_number(self) -> str:
        return self._plate_number

    @plate_number.setter
    def plate_number(self, value: str) -> None:
        if not value.strip():
            raise ValueError("پلاک نمی‌تواند خالی باشد.")
        self._plate_number = value.strip().upper()

    @property
    def brand(self) -> str:
        return self._brand

    @brand.setter
    def brand(self, value: str) -> None:
        if len(value) < 2:
            raise ValueError("نام برند معتبر نیست.")
        self._brand = value.title()

    @property
    def year(self) -> int:
        return self._year

    @year.setter
    def year(self, value: int) -> None:
        current_year = date.today().year
        if not (1990 <= value <= current_year + 1):
            raise ValueError("سال ساخت معتبر نیست.")
        self._year = value

    @property
    def base_daily_rate(self) -> float:
        return self._base_daily_rate

    @base_daily_rate.setter
    def base_daily_rate(self, value: float) -> None:
        if value <= 0:
            raise ValueError("نرخ پایه باید مثبت باشد.")
        self._base_daily_rate = value

    # 🔹 Abstraction: Students MUST implement
    @abstractmethod
    def calculate_daily_cost(self) -> float: ...

    @abstractmethod
    def get_vehicle_type(self) -> str: ...

    @abstractmethod
    def perform_maintenance(self) -> None: ...

    # 🔹 Inheritance Reuse
    def display_info(self) -> None:
        print(f"[{self.get_vehicle_type()}] {self.brand} | مدل: {self.year} | نرخ پایه: {self.base_daily_rate:.2f}")
