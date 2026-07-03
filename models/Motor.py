from models.vehicle import Vehicle
from models.mixins import Rentable , Insurable
class Motorcycle(Vehicle,Rentable,Insurable):
    def __init__(self,plate_number:str,brand:str,year:int,base_daily_rate:float):
        super().__init__(plate_number,brand,year,base_daily_rate)
    def get_vehicle_type(self) -> str:
        return "Motorcycle"
    def calculate_daily_cost(self) ->float:
        return self._base_daily_rate * 1.1
    def perform_maintenance(self) -> None:
        print("Motorcycle maintenance is starting")
        print("engine --->checked ")
        print("brackes ---> checked")
        print("chain ---> checked")
        print("tire ---> checked")
        print(" Motorcycle is ready")

    def calculate_rent(self,days:int) ->float:
        return self.calculate_daily_cost() * days
    def reserve(self) ->None:
        print("Motorcycle resecved successfully")
    def return_vehicle(self,actual_days:int) ->None:
        print(f"the motorcycle returned after {actual_days} days")
    def calculate_insurance_premium(self) ->float:
        return self.calculate_daily_cost()* 0.3
    def is_eligible_for_coverage(self) ->bool:
        return self.year >= 2012