from models.vehicle import Vehicle
from models.car import Car
from models.truck import Truck
from models.motorcycle import Motorcycle


def run_fleet_simulation(fleet: list[Vehicle]) -> None:
    for v in fleet:
        v.display_info()
        print(f"Daily cost: {v.calculate_daily_cost():.2f}")
        v.perform_maintenance()
        print("-" * 40)


if __name__ == "__main__":
    # نمونه‌های واقعی ساخته و به لیست اضافه می‌شوند
    fleet: list[Vehicle] = [
        Car("12345", "Toyota", 2020, 150.0, num_doors=4, insurance_value=20000),
        Truck("TRK-99", "Volvo", 2018, 300.0, cargo_capacity_kg=10000, insurance_value=50000),
        Motorcycle("MC-01", "Honda", 2021, 60.0, engine_cc=500, insurance_value=8000),
    ]
    run_fleet_simulation(fleet)
