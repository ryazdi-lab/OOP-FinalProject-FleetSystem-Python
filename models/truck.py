from models.vehicle import Vehicle
from models.mixins import Rentable, Insurable


class Truck(Vehicle, Rentable, Insurable):
    def __init__(
        self,
        plate_number: str,
        brand: str,
        year: int,
        base_daily_rate: float,
    ) -> None:
        super().__init__(plate_number, brand, year, base_daily_rate)
        self._reserved = False

    def calculate_daily_cost(self) -> float:
        return self.base_daily_rate * 1.30

    def get_vehicle_type(self) -> str:
        return "Truck"

    def perform_maintenance(self) -> None:
        print("Truck maintenance completed.")

    def calculate_rent(self, days: int) -> float:
        if days <= 0:
            raise ValueError("Days must be positive.")
        return self.calculate_daily_cost() * days

    def reserve(self) -> None:
        self._reserved = True
        print("Truck reserved.")

    def return_vehicle(self, actual_days: int) -> None:
        self._reserved = False
        print(
            f"Truck returned. Total cost: "
            f"{self.calculate_rent(actual_days):.2f}"
        )

    def calculate_insurance_premium(self) -> float:
        return self.base_daily_rate * 0.25

    def is_eligible_for_coverage(self) -> bool:
        return self.year >= 2005