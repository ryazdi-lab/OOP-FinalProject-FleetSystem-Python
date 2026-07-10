"""کلاس Car — خودروی سواری (قابل اجاره و قابل بیمه)."""

from .vehicle import Vehicle
from .mixins import Rentable, Insurable


class Car(Vehicle, Rentable, Insurable):
    def __init__(
        self,
        make: str,
        model: str,
        year: int,
        base_price: float,
        num_doors: int = 4,
    ) -> None:
        super().__init__(make, model, year, base_price)
        self.num_doors = num_doors

    @property
    def num_doors(self) -> int:
        return self._num_doors

    @num_doors.setter
    def num_doors(self, value: int) -> None:
        if value not in (2, 4, 5):
            raise ValueError("تعداد درها باید ۲، ۴ یا ۵ باشد")
        self._num_doors = value

    # پیاده‌سازی قرارداد Vehicle
    def vehicle_type(self) -> str:
        return "خودرو"

    def wheels(self) -> int:
        return 4

    def calculate_maintenance_cost(self) -> float:
        return self.base_price * 0.02

    # پیاده‌سازی قرارداد Mixinها
    def daily_rental_rate(self) -> float:
        return self.base_price * 0.001

    def risk_factor(self) -> float:
        return 1.0
