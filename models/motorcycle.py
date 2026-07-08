from models.vehicle import Vehicle
from models.mixins import Rentable, Insurable
class Motorcycle(Vehicle,Rentable, Insurable):
    def __init__(self, plate_number, brand, year, base_daily_rate, fuel_type):
        super().__init__(plate_number, brand, year, base_daily_rate)
        self.fuel_type = fuel_type
        self.reserved = False
    def calculate_daily_cost(self)-> float:
        return self.base_daily_rate + 30
    def get_vehicle_type(self)-> str:
        return "Motorcycle"
    def perform_maintenance(self)-> None:
        print("سرویس موتور انجام شد")  
    def calculate_rent(self, days: int)-> float:
        return self.calculate_daily_cost() * days
    def reserve(self) -> None:
        self.reserved =True
        print("موتور رزرو شد.")    
    def return_vehicle(self, actual_days : int) -> None:
        self.reserved = False
        print(f"موتور بعد از {actual_days} روز بازگشت داده شد")  
    def calculate_insurance_premium(self) -> float :
        return self.base_daily_rate * 0.8
    def is_eligible_for_coverage(self) -> bool:
        return self.year >= 2000  