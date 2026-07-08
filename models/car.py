from models.mixins import Insurable,Rentable
from models.vehicle import Vehicle

class Car(Vehicle,Rentable,Insurable):

    def calculate_daily_cost(self) -> float:
        return self.base_daily_rate*self.year/1000

    def get_vehicle_type(self) -> str:
        return "Car"

    def perform_maintenance(self) -> None:
        print(f"{self.brand}: Checking engine oil and tire pressure... Ready to hit the road!")

    def calculate_rent(self, days: int) -> float:
            return self.calculate_daily_cost()*days

    def reserve(self) -> None:
        print(f"{self.brand} has been reserved")

    def return_vehicle(self, actual_days: int) -> None:
        print(f"the {self.brand} has been returned , with total cost {self.calculate_rent(actual_days)}")


    def calculate_insurance_premium(self) -> float:
        if self.is_eligible_for_coverage():
            return self.calculate_daily_cost()*0.1
        else:
            return 0

    def is_eligible_for_coverage(self) -> bool:
        return self.year >= 2010
