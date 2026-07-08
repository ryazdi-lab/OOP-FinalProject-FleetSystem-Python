
from models.vehicle import Vehicle
from models.car import Car
from models.motorcycle import Motorcycle
from models.truck import Truck
#main file to create vehicles and demonstrate polymorphism
def run_fleet_simulation(fleet: list[Vehicle]) -> None:
    for v in fleet:
        v.display_info()
        print(f"هزینه روزانه:: {v.calculate_daily_cost():.2f}")
        v.perform_maintenance()
        print("-" * 40)

if __name__ == "__main__":
    fleet: list[Vehicle] = [
        Car("12A345", "Toyota", 2020, 150.0, 4),
        Motorcycle("45B678", "Honda", 2022, 100.0, "بنزینی"),
        Truck("TRK-99", "Volvo", 2018, 300.0, 10)
    ]
    run_fleet_simulation(fleet) 
    # verified Vehicle subclasses and polymorphism behavior 