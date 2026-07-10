"""کلاس Truck — کامیون باری (قابل بیمه، اما اجاره‌ای نیست).

نکته: Truck از Rentable ارث‌بری نمی‌کند تا نشان دهیم همهٔ وسایل
لزوماً همهٔ قابلیت‌ها را ندارند؛ در main.py این تفاوت بدون استفاده
از isinstance مدیریت می‌شود.
"""

from .vehicle import Vehicle
from .mixins import Insurable


class Truck(Vehicle, Insurable):
    def __init__(
        self,
        make: str,
        model: str,
        year: int,
        base_price: float,
        cargo_capacity: float,
    ) -> None:
        super().__init__(make, model, year, base_price)
        self.cargo_capacity = cargo_capacity

    @property
    def cargo_capacity(self) -> float:
        """ظرفیت بار بر حسب تن."""
        return self._cargo_capacity

    @cargo_capacity.setter
    def cargo_capacity(self, value: float) -> None:
        if value <= 0:
            raise ValueError("ظرفیت بار باید مثبت باشد")
        self._cargo_capacity = float(value)

    def vehicle_type(self) -> str:
        return "کامیون"

    def wheels(self) -> int:
        return 6

    def calculate_maintenance_cost(self) -> float:
        # هزینهٔ نگهداری با ظرفیت بار افزایش می‌یابد
        return self.base_price * 0.04 + self.cargo_capacity * 1_000_000

    def risk_factor(self) -> float:
        return 1.5
