from models.vehicle import Vehicle
from models.models import Car, Motorcycle, Truck


def run_fleet_simulation(fleet: list[Vehicle]) -> None:
    for v in fleet:
        v.display_info()
        print(f"هزینه روزانه: {v.calculate_daily_cost():.2f}")
        v.perform_maintenance()
        print("-" * 40)

if __name__ == "__main__":
    fleet: list[Vehicle] = [
        Car("3636ب55", "BMW m2", 2020, 180.0),
        Car("99jz12", "Toyota supra", 2025, 160.0),
        Motorcycle("13ج5", "Yamaha R25", 2022, 90, 250),
        Truck("TRK-99", "Volvo", 2021, 300.0, 18),
        Motorcycle("8686", "kawasaki ninja h2r", 2026, 115, 998),
        Truck("TRK-3800", "DAF", 2015, 260.0, 14),
    ]
    run_fleet_simulation(fleet)