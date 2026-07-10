from datetime import date
from .vehicle import Vehicle 
from .mixins import Insurable

class Truck(Vehicle, Insurable):
    def __init__(self, plate_number: str, brand: str, year: int, base_daily_rate: float):
        super().__init__(plate_number, brand, year, base_daily_rate)


    def get_vehicle_type(self) -> str:
        return "Truck"
    

    def calculate_daily_cost(self) -> float:
        age = date.today().year - self.year

        if age <= 10:
            return self.base_daily_rate * 2.50
        elif age >= 35:
            return self.base_daily_rate * 2.10
        else:
            return self.base_daily_rate * 2.35
        

    def perform_maintenance(self) -> None:
        print(f"{self.brand} maintenance completed.")


    def calculate_insurance_premium(self) -> float: 
        age = date.today().year - self.year

        if age <= 10:
            return self.base_daily_rate * 2.55
        elif age >= 35:
            return self.base_daily_rate * 2.75
        else: 
            return self.base_daily_rate * 2.35
    
    
    def is_eligible_for_coverage(self) -> bool:
        return self.year >= 1986
    