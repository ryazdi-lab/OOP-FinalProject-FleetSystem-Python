from models.vehicle import Vehicle
from models.car import Car
from models.truck import Truck
from models.motorcycle import Motorcycle

def run_fleet_simulation(fleet_: list[Vehicle]) -> None:
    for v in fleet_:
        v.display_info()
        print(f"هزینه روزانه: {v.calculate_daily_cost():.2f}")
        v.perform_maintenance()
        print("-" * 40)

if __name__ == "__main__":
    # دانشجویان اینجا اشیاء concrete را می‌سازند و به لیست اضافه می‌کنند
    fleet: list[Vehicle] = [
        Car("DA-655-QL", "Tesla", 2024, 230.0),
        Truck("HCM-6223", "DAF", 2019, 420.0),
        Motorcycle("4559 RW", "Aprilia", 2025, 110.0)
    ]
    run_fleet_simulation(fleet)
