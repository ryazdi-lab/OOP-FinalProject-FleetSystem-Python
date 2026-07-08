from models.mixins import Insurable
from models.vehicle import Vehicle

class Truck(Vehicle,Insurable):

    def calculate_daily_cost(self) -> float:
        return self.base_daily_rate*self.year/1000

    def get_vehicle_type(self) -> str:
        return "Truck"

    def perform_maintenance(self) -> None:
        print(f"{self.brand}:checking the load ... checking the tire pressure and engine oil... ready to ignite")

    def calculate_insurance_premium(self) -> float:
        if self.is_eligible_for_coverage():
            return self.calculate_daily_cost()*0.5
        else:
            return 0

    def is_eligible_for_coverage(self) -> bool:
        return self.year >= 2000
