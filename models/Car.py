from models.vehicle import Vehicle
from models.mixins import Rentable , Insurable

class Car( Vehicle,Rentable, Insurable):
    def __init__(self,plate_number,brand:str,year:int,base_daily_rate:float):
        super().__init__(plate_number,brand,year,base_daily_rate)
    
    def get_vehicle_type(self):
        return "car"
    def calculate_daily_cost(self):
        return self.base_daily_rate * 1.15
    def perform_maintenance(self) -> None:
        print("car maintenance is starting ... ")
        print("engine oil---> checked")
        print("battery ---> checked")
        print("air filter ---> checked")
        print("tire pressure --->checked")
        print("light and signal ---> checked")
        print("brakes ---> checked")
        print("the car had been serviced")
        
    def calculate_rent(self,days:int) ->float:
        return self.calculate_daily_cost() * days
    def reserve(self) -> None:
        print ( " car Reserved successfully")
    def return_vehicle(self,actual_days:int):
        print(f"the car returned after {actual_days} days")
    def calculate_insurance_premium(self) ->float:
        return self.calculate_daily_cost() * 0.5
    def is_eligible_for_coverage(self) -> bool:
        return self.year >= 2010
            
    