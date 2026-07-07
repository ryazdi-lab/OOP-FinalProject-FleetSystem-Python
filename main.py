from models.vehicle import Vehicle
from models import Car, Motorcycle, Truck 
def run_fleet_simulation(fleet: list[Vehicle]) -> None:
    for v in fleet:
        v.display_info()
        print(f"هزینه روزانه: {v.calculate_daily_cost():.2f}")
        v.perform_maintenance()
        print("-" * 40)


if __name__ == "__main__":
    # دانشجویان اینجا اشیاء concrete را می‌سازند و به لیست اضافه می‌کنند
    fleet: list[Vehicle] = [
         Car("12345", "Toyota", 2020, 500, 5),
         Motorcycle("34B567", "Honda", 2021, 300, 250),
         Truck("TRK-99", "Volvo", 2018, 800, 10),
    ]
    run_fleet_simulation(fleet)