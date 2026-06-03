from models.vehicle_generic import VehicleGeneric
from models.mixins import Rentable
from typing import Any


class VehicleRentable(VehicleGeneric, Rentable):
    def __init__(self, plate_number: str, brand: str, year: int, base_daily_rate: float, daily_rent: float, **kwargs: Any):
        super().__init__(plate_number, brand, year, base_daily_rate, **kwargs)
        self._reserved = False
        self._daily_rent = daily_rent

    @property  # reserved is changed via the reserved and return_vehicle methods so there shouldn't be a setter
    def reserved(self) -> bool:
        return self._reserved

    @property
    def daily_rent(self) -> float:
        return self._daily_rent

    @daily_rent.setter
    def daily_rent(self, value: float) -> None:
        if value > 0:
            self._daily_rent = value
        else:
            print("daily_rent must be a positive number")

    def calculate_daily_cost(self) -> float:
        return super().calculate_daily_cost() + self.calculate_rent(1)

    def calculate_rent(self, days: int) -> float:
        return days*self.daily_rent

    def reserve(self) -> None:
        if self._reserved:
            print("already reserved")
        else:
            self._reserved = True

    def return_vehicle(self, actual_days: int) -> None:
        if self._reserved:
            self._reserved = False
            print(f"cost: {self.calculate_rent(actual_days)}")
        else:
            print("can't return an unreserved vehicle")

    def display_info(self) -> None:
        super().display_info()
        print(
            f"reserved: {self.reserved} | daily rent: {self.daily_rent}")
