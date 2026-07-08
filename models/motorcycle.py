from models.mixins import Rentable
from models.vehicle import Vehicle

class Car(Vehicle,Rentable):

    def calculate_daily_cost(self) -> float:
        return self.base_daily_rate*self.year/1000

    def get_vehicle_type(self) -> str:
        return "Motorcycle"

    def perform_maintenance(self) -> None:
        print(f"{self.brand}: Checking the breaks... ready to ride")

    def calculate_rent(self, days: int) -> float:
            return self.calculate_daily_cost()*(days/2)

    def reserve(self) -> None:
        print(f"{self.brand} has been reserved")

    def return_vehicle(self, actual_days: int) -> None:
        print(f"the {self.brand} has been returned , with total cost {self.calculate_rent(actual_days)}")

