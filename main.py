from models.motorcycle import Motorcycle
from models.car import Car
from models.truck import Truck
from models.vehicle import Vehicle

def run_fleet_simulation(fleet: list[Vehicle]) -> None:
    for v in fleet:
        v.display_info()
        print(f"هزینه روزانه: {v.calculate_daily_cost():.2f}")
        v.perform_maintenance()
        print("-" * 40)

if __name__ == "__main__":
    fleet: list[Vehicle] = [
        Car("25T476","Benz",2023,600.0),
        Truck("12E500","volvo",2000,49.9),
        Motorcycle("FEE69","Yamaha",2025,5.5)
    ]
    run_fleet_simulation(fleet)