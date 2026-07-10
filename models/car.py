from datetime import date 
from .vehicle import Vehicle
from .mixins import Rentable, Insurable

class Car(Vehicle, Rentable, Insurable):
    def __init__(self, plate_number: str, brand: str, year: int, base_daily_rate: float):
        super().__init__(plate_number, brand, year, base_daily_rate)


    def get_vehicle_type(self) -> str:
        return "Car"
    

    def calculate_daily_cost(self) -> float:
        age = date.today().year - self.year

        if age <= 4:
            return self.base_daily_rate * 1.20
        elif age >= 30:
            return self.base_daily_rate * 1.55
        else:
            return self.base_daily_rate * 1.08
    

    def perform_maintenance(self) -> None:
        print(f"{self.brand} maintenance completed.")


    def calculate_rent(self, days: int) -> float:
        age = date.today().year - self.year

        if age <= 4:
            return self.base_daily_rate * days * 1.50
        elif age >= 30:
            return self.base_daily_rate * days * 1.75
        else: 
            return self.base_daily_rate * days * 1.25


    def reserve(self) -> None:
        print(f"{self.brand} reserved successfully.")
    

    def return_vehicle(self, actual_days: int) -> None:
        print(f"{self.brand} returned after {actual_days} day(s).")


    def calculate_insurance_premium(self) -> float: 
        age = date.today().year - self.year

        if age <= 4:
            return self.base_daily_rate * 1.50
        elif age >= 30:
            return self.base_daily_rate * 1.75
        else: 
            return self.base_daily_rate * 1.25
    
    
    def is_eligible_for_coverage(self) -> bool:
        return self.year >= 1995