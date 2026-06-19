from models.vehicle import Vehicle
from models.mixins import Rentable, Insurable

class Truck(Vehicle, Rentable, Insurable):
    def __init__(self, plate_number: str, brand: str, year: int, base_daily_rate: float):
        super().__init__(plate_number, brand, year, base_daily_rate)

    def calculate_daily_cost(self) -> float:
        return self.base_daily_rate * 1.6

    def get_vehicle_type(self) -> str:
        return "Truck"

    def perform_maintenance(self) -> None:
        print("\nTruck is being serviced...")
        print("Engine oil -> checked!")
        print("Air filter condition -> serviced!")
        print("Tire Inflation (all + spares) -> checked!")
        print("Air Brake pressure -> checked!")
        print("Headlights and Signals -> serviced!")
        print("Service completed! The Truck is all set and ready.")

    def calculate_rent(self, days: int) -> float:
        return self.calculate_daily_cost() * days

    def reserve(self) -> None:
        print(f"{self.get_vehicle_type()} Reserved Successfully!")

    def return_vehicle(self, actual_days: int) -> None:
        print(f"Truck Returned After {actual_days} Day, Successfully!")

    def calculate_insurance_premium(self) -> float:
        return self.calculate_daily_cost() * 0.75

    def is_eligible_for_coverage(self) -> bool:
        return self.year >= 2016