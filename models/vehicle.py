"""کلاس انتزاعی پایه برای تمام وسایل نقلیه ناوگان (هستهٔ Abstraction)."""

from abc import ABC, abstractmethod
from datetime import datetime


class Vehicle(ABC):
    """
    پایهٔ انتزاعی هر وسیله نقلیه.

    این کلاس قرارداد مشترک (متدهای انتزاعی) را تعریف می‌کند و رفتار
    مشترک (توصیف، اعتبارسنجی) را در یک جا نگه می‌دارد تا از تکرار کد
    در کلاس‌های فرزند جلوگیری شود.
    """

    def __init__(self, make: str, model: str, year: int, base_price: float) -> None:
        self._make = make
        self._model = model
        # از setterها برای اعتبارسنجی مقادیر ورودی استفاده می‌کنیم
        self.year = year
        self.base_price = base_price

    # ---------- Encapsulation: property + validation ----------
    @property
    def make(self) -> str:
        return self._make

    @property
    def model(self) -> str:
        return self._model

    @property
    def year(self) -> int:
        return self._year

    @year.setter
    def year(self, value: int) -> None:
        current_year = datetime.now().year
        if value < 1900 or value > current_year + 1:
            raise ValueError(f"سال نامعتبر است: {value}")
        self._year = int(value)

    @property
    def base_price(self) -> float:
        """قیمت پایهٔ خرید وسیله نقلیه (مبنای محاسبهٔ بیمه و نگهداری)."""
        return self._base_price

    @base_price.setter
    def base_price(self, value: float) -> None:
        if value <= 0:
            raise ValueError("قیمت پایه باید بزرگ‌تر از صفر باشد")
        self._base_price = float(value)

    # ---------- Abstraction: قرارداد (بدون پیاده‌سازی) ----------
    @abstractmethod
    def vehicle_type(self) -> str:
        """نام فارسی نوع وسیله نقلیه."""

    @abstractmethod
    def wheels(self) -> int:
        """تعداد چرخ‌ها."""

    @abstractmethod
    def calculate_maintenance_cost(self) -> float:
        """هزینهٔ نگهداری سالانه؛ فرمول آن برای هر نوع وسیله متفاوت است."""

    # ---------- رفتار مشترک (قابل استفاده به‌صورت چندریختی) ----------
    def describe(self) -> str:
        """
        توصیف وسیله نقلیه با فراخوانی متدهای انتزاعی.

        این متد پایهٔ چندریختی است: بدون دانستن نوع دقیق شیء،
        رفتار مناسب هر کلاس فرزند به‌صورت خودکار اجرا می‌شود.
        """
        return (
            f"[{self.vehicle_type()}] {self.make} {self.model} ({self.year}) "
            f"| {self.wheels()} چرخ "
            f"| نگهداری سالانه: {self.calculate_maintenance_cost():,.0f} تومان"
        )

    def __str__(self) -> str:
        return self.describe()

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(make={self.make!r}, model={self.model!r}, "
            f"year={self.year}, base_price={self.base_price})"
        )
