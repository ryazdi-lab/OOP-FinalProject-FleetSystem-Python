from abc import abstractmethod
import datetime
from models.vehicle import Vehicle
from models.mixins import Rentable, Insurable


class Car(Vehicle, Rentable, Insurable):
    def __init__(
        self,
        plate_number: str,
        brand: str,
        year: int,
        base_daily_rate: float,
        seats: int,
    ):
        super().__init__(plate_number, brand, year, base_daily_rate)
        self.seats = seats
        self.is_reserved = False

    @property
    def seats(self) -> int:
        return self._seats

    @seats.setter
    def seats(self, value: int) -> None:
        if value < 2:
            raise ValueError("تعداد صندلی نامعتبر است.")
        self._seats = value

    def calculate_daily_cost(self) -> float:
        return self.base_daily_rate + (self.seats * 10)

    def get_vehicle_type(self) -> str:
        return "Car"

    def perform_maintenance(self) -> None:
        print(f"{self.brand} maintenance completed.")

    def calculate_rent(self, days: int) -> float:
        return self.calculate_daily_cost() * days

    def reserve(self) -> None:
        self.is_reserved = True

    def return_vehicle(self, actual_days: int) -> None:
        self.is_reserved = False

    def calculate_insurance_premium(self) -> float:
        return self.base_daily_rate * 0.15

    def is_eligible_for_coverage(self) -> bool:
        return (datetime.date.today().year - self.year) <= 15