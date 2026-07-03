from models.vehicle import Vehicle
from models.Car import Car
from models.Motor import Motorcycle
from models.Truck import Truck

def run_fleet_simulation(fleet) -> None:
    for v in fleet:
        v.display_info()
        print(f"هزینه روزانه: {v.calculate_daily_cost():.2f}")
        v.perform_maintenance()
        print("-" * 40)

if __name__ == "__main__":
    fleet = [ 
        Car("12345", "Toyota", 2020, 150.0),
        Motorcycle("M-101", "Honda", 2022,80.0),
        Truck("TRK-99", "Volvo", 2018, 300.0)
    ]
    run_fleet_simulation(fleet)