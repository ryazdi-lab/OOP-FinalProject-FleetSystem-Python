from .vehicle import Vehicle
from .mixins import Rentable, Insurable


class Truck(Vehicle, Rentable, Insurable):
    def __init__(
        self,
        plate_number: str,
        brand: str,
        year: int,
        base_daily_rate: float,
        cargo_capacity_tons: float,
    ):
        super().__init__(plate_number, brand, year, base_daily_rate)
        self.cargo_capacity_tons = cargo_capacity_tons
        self._is_reserved = False

    @property
    def cargo_capacity_tons(self) -> float:
        return self._cargo_capacity_tons

    @cargo_capacity_tons.setter
    def cargo_capacity_tons(self, value: float) -> None:
        if value <= 0:
            raise ValueError("ظرفیت بار باید بزرگ‌تر از صفر باشد.")
        self._cargo_capacity_tons = value

    def calculate_daily_cost(self) -> float:
        return self.base_daily_rate + (self.cargo_capacity_tons * 200000)

    def get_vehicle_type(self) -> str:
        return "کامیون (Truck)"

    def perform_maintenance(self) -> None:
        print(f"در حال بررسی فنی کامیون {self.brand} با پلاک {self.plate_number}...")

    def calculate_rent(self, days: int) -> float:
        if days <= 0:
            raise ValueError("تعداد روزهای اجاره باید مثبت باشد.")
        return days * self.calculate_daily_cost()

    def reserve(self) -> None:
        if self._is_reserved:
            print("این کامیون از قبل رزرو شده است.")
        else:
            self._is_reserved = True
            print(f"کامیون {self.brand} با موفقیت رزرو شد.")

    def return_vehicle(self, actual_days: int) -> None:
        self._is_reserved = False
        print(f"کامیون بازگردانده شد. هزینه نهایی اجاره: {self.calculate_rent(actual_days)}")

    def calculate_insurance_premium(self) -> float:
        return 3000000 + (self.cargo_capacity_tons * 500000)

    def is_eligible_for_coverage(self) -> bool:
        return self.year >= 2010