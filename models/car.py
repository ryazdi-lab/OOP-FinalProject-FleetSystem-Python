from models.vehicle import Vehicle
from models.mixins import Rentable, Insurable
class Car(Vehicle, Rentable, Insurable):
    def __init__(self, plate_number, brand, year, base_daily_rate, door_count):
        super().__init__(plate_number, brand, year, base_daily_rate)
        self.door_count = door_count
        self.reserved = False
    def calculate_daily_cost(self)-> float :
        return  self.base_daily_rate + (self.door_count * 20)
    def get_vehicle_type(self)->str:
        return "Car"
    def perform_maintenance(self)-> None:
        print("سرویس ماشین انجام شد.")
    def calculate_rent(self, days: int) -> float:
        return self.calculate_daily_cost() * days  
    def reserve(self) -> None:
        self.reserved = True
        print("ماشین رزرو شد")
    def return_vehicle(self, actual_days : int) -> None:
        self.reserved = False
        print(f"ماشین بعد از {actual_days} روز بازگشت داده شد")  
    def calculate_insurance_premium(self) -> float :
        return self.base_daily_rate * 0.1
    def is_eligible_for_coverage(self) -> bool:
        return self.year >= 2000   