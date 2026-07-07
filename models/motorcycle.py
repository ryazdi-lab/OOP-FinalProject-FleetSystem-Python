from models.vehicle import Vehicle
from models.mixins import Rentable


class Motorcycle(Vehicle, Rentable):
    def __init__(
        self,
        plate_number: str,
        brand: str,
        year: int,
        base_daily_rate: float,
        engine_cc: int,
    ):
        super().__init__(plate_number, brand, year, base_daily_rate)
        self.engine_cc = engine_cc
        self.is_reserved = False

    @property
    def engine_cc(self) -> int:
        return self._engine_cc

    @engine_cc.setter
    def engine_cc(self, value: int) -> None:
        if value <= 0:
            raise ValueError("حجم موتور نامعتبر است.")
        self._engine_cc = value

    def calculate_daily_cost(self) -> float:
        return self.base_daily_rate + (self.engine_cc / 100)

    def get_vehicle_type(self) -> str:
        return "Motorcycle"

    def perform_maintenance(self) -> None:
        print(f"{self.brand} motorcycle maintenance completed.")

    def calculate_rent(self, days: int) -> float:
        return self.calculate_daily_cost() * days

    def reserve(self) -> None:
        self.is_reserved = True

    def return_vehicle(self, actual_days: int) -> None:
        self.is_reserved = False