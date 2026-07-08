from models.vehicle import Vehicle
from models.mixins import Rentable, Insurable
#Truck class represents heavy vehicles with truck-specfic properties
class Truck(Vehicle,Rentable, Insurable):
    def __init__(self, plate_number, brand, year, base_daily_rate, load_capacity):
        super().__init__(plate_number, brand, year, base_daily_rate)
        self.load_capacity = load_capacity
        self.reserved = False
    def calculate_daily_cost(self)-> float:
        return self.base_daily_rate + (self.load_capacity * 15)
    def get_vehicle_type(self)-> str:
        return "Truck"
    def perform_maintenance(self)-> None:
        print("سرویس کامیون انجام شد.")  
    def calculate_rent(self, days: int)-> float:
        return self.calculate_daily_cost() * days
    def reserve(self) -> None:
        self.reserved =True
        print("کامیون رزرو شد")    
    def return_vehicle(self, actual_days : int) -> None:
        self.reserved = False
        print(f"کامیون بعد از {actual_days} روز بازگشت داده شد")  
    def calculate_insurance_premium(self) -> float :
        return self.base_daily_rate * 0.15
    def is_eligible_for_coverage(self) -> bool:
        return self.year >= 2000 