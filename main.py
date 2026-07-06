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
    # دانشجویان اینجا اشیاء concrete را می‌سازند و به لیست اضافه می‌کنند
    fleet: list[Vehicle] = [
    Car("11A111", "Toyota", 2022, 120.0, 5),
    Truck("22B222", "Volvo", 2020, 250.0, 8),
    Motorcycle("33C333", "Honda", 2021, 80.0, 250),
]
    run_fleet_simulation(fleet)