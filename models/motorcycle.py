from datetime import date
from .vehicle import Vehicle
from .mixins import Rentable

class Motorcycle(Vehicle, Rentable):
    def __init__(self, plate_number: str, brand: str, year: int, base_daily_rate: float):
        super().__init__(plate_number, brand, year, base_daily_rate)

    
    def get_vehicle_type(self) -> str:
        return "Motorcycle"
    

    def calculate_daily_cost(self) -> float:
        age = date.today().year - self.year

        if age <= 6:
            return self.base_daily_rate * 0.95
        elif age >= 15:
            return self.base_daily_rate * 0.40
        else:
            return self.base_daily_rate * 0.70
        

    def perform_maintenance(self) -> None:
        print(f"{self.brand} maintenance completed.")

    
    def calculate_rent(self, days: int) -> float:
        age = date.today().year - self.year

        if age <= 6:
            return self.base_daily_rate * days * 1.40
        elif age >= 15:
            return self.base_daily_rate * days * 1.10
        else:
            return self.base_daily_rate * days * 1.25
        

    def reserve(self) -> None:
        print(f"{self.brand} reserved successfully.")
    

    def return_vehicle(self, actual_days: int) -> None:
        print(f"{self.brand} returned after {actual_days} day(s).")



        