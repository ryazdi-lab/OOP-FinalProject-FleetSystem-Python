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
        Motorcycle("AB666", "Honda", 1990, 100.0, 10.0),
        Motorcycle("H5R6L", "Yamaha", 1992, 200.0, 15.0),
        Car("U8UU5", "Ford", 1999, 2000.0, 150.0, 0.3, True),
        Car("SXYZ9", "Hyundai", 1998, 3000.0, 200.0, 0.2, True),
        Car("I5HUY", "BMW", 2001, 3500.0, 100.0, 0.1, True),
        Truck("BIG8Y", "Peterbilt", 2010, 8000.0, 0.4, True)
    ]
    run_fleet_simulation(fleet)
