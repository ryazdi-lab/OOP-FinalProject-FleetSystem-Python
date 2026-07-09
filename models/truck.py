from datetime import date

from models.vehicle import Vehicle
from models.mixins import Insurable

TRUCK_CARGO_SURCHARGE_PER_TON = 15.0
TRUCK_INSURANCE_BASE_RATE = 0.025
TRUCK_MAX_INSURABLE_AGE_YEARS = 20
TRUCK_MAINTENANCE_LOAD_THRESHOLD_TONS = 8.0


class Truck(Vehicle, Insurable):
    """کامیون: تحت قرارداد اجاره بلندمدت است، نه اجاره روزانه؛ فقط بیمه‌پذیر."""

    def __init__(
        self,
        plate_number: str,
        brand: str,
        year: int,
        base_daily_rate: float,
        cargo_capacity_tons: float,
    ) -> None:
        super().__init__(plate_number, brand, year, base_daily_rate)
        self.cargo_capacity_tons = cargo_capacity_tons

    @property
    def cargo_capacity_tons(self) -> float:
        return self._cargo_capacity_tons

    @cargo_capacity_tons.setter
    def cargo_capacity_tons(self, value: float) -> None:
        if value <= 0:
            raise ValueError("ظرفیت بار باید مثبت باشد.")
        self._cargo_capacity_tons = value

    # --- Abstraction (Vehicle) ---
    def calculate_daily_cost(self) -> float:
        return self.base_daily_rate + (self.cargo_capacity_tons * TRUCK_CARGO_SURCHARGE_PER_TON)

    def get_vehicle_type(self) -> str:
        return "کامیون"

    def perform_maintenance(self) -> None:
        if self.cargo_capacity_tons >= TRUCK_MAINTENANCE_LOAD_THRESHOLD_TONS:
            print(f"بازرسی سیستم ترمز و تعلیق سنگین کامیون {self.plate_number} انجام شد.")
        else:
            print(f"سرویس دوره‌ای استاندارد کامیون {self.plate_number} انجام شد.")

    # --- Insurable ---
    def calculate_insurance_premium(self) -> float:
        base = self.base_daily_rate * 30 * TRUCK_INSURANCE_BASE_RATE
        cargo_factor = 1 + (self.cargo_capacity_tons / 10)
        return round(base * cargo_factor, 2)

    def is_eligible_for_coverage(self) -> bool:
        return (date.today().year - self.year) <= TRUCK_MAX_INSURABLE_AGE_YEARS