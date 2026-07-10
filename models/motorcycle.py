"""کلاس Motorcycle — موتورسیکلت (قابل اجاره و قابل بیمه، ریسک بالاتر)."""

from .vehicle import Vehicle
from .mixins import Rentable, Insurable


class Motorcycle(Vehicle, Rentable, Insurable):
    def __init__(
        self,
        make: str,
        model: str,
        year: int,
        base_price: float,
        engine_cc: int = 250,
    ) -> None:
        super().__init__(make, model, year, base_price)
        self.engine_cc = engine_cc

    @property
    def engine_cc(self) -> int:
        return self._engine_cc

    @engine_cc.setter
    def engine_cc(self, value: int) -> None:
        if value <= 0:
            raise ValueError("حجم موتور باید مثبت باشد")
        self._engine_cc = value

    def vehicle_type(self) -> str:
        return "موتورسیکلت"

    def wheels(self) -> int:
        return 2

    def calculate_maintenance_cost(self) -> float:
        return self.base_price * 0.03

    def daily_rental_rate(self) -> float:
        return self.base_price * 0.0015

    def risk_factor(self) -> float:
        # موتورهای پرقدرت‌تر ریسک بیمهٔ بالاتری دارند
        return 2.0 if self.engine_cc >= 600 else 1.5
