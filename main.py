from models.vehicle import Vehicle
from models.car import Car
from models.truck import Truck
from models.motorcycle import Motorcycle


def run_fleet_simulation(fleet: list[Vehicle]) -> None:
    for v in fleet:
        v.display_info()
        print(f"هزینه روزانه: {v.calculate_daily_cost():.2f}")
        v.perform_maintenance()
        print("-" * 40)


if __name__ == "__main__":
    # Create a fleet to demonstrate polymorphism
    fleet: list[Vehicle] = [
        Car("12345", "Toyota", 2020, 150.0),
        Truck("TRK-99", "Volvo", 2018, 300.0),
        Motorcycle("M-55", "Honda", 2022, 80.0),
    ]

    run_fleet_simulation(fleet)
