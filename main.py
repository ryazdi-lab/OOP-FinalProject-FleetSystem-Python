from models.vehicle import Vehicle
from models.car import Car
from models.motorcycle import Motorcycle
from models.truck import Truck

def run_fleet_simulation(fleet: list[Vehicle]) -> None:
    for v in fleet:
        v.display_info()
        print(f"هزینه روزانه: {v.calculate_daily_cost():.2f}")
        v.perform_maintenance()
        print("-" * 40)

if __name__ == "__main__":
    # دانشجویان اینجا اشیاء concrete را می‌سازند و به لیست اضافه می‌کنند
    fleet: list[Vehicle] = [
       Car("12345A", "Toyota", 2024, 500.0),
       Car("22345F", "BMW", 2017, 300.0 ),
       Car("45454Z", "Porsche", 2008, 320.0),
       Car("94785P", "Benz", 1993, 550.0),
       Motorcycle("11111H", "Honda", 2025, 167.0),
       Motorcycle("22222Y", "Yamaha", 2015, 155.0),
       Motorcycle("33333S", "Suzuki", 2011, 142.0),
       Motorcycle("44444K", "Ducati", 2002, 130.0 ),
       Truck("99999V", "Volvo", 2020, 900.0),
       Truck("88888S", "Scania", 2012, 800.0),
       Truck("77777I", "Iveco", 1999, 760.0),
       Truck("66666M", "Mack", 1990, 710.0),
    ]
    run_fleet_simulation(fleet)


    print("\n=== Rentable Vehicles ===")
    for v in fleet:
        if hasattr(v, "calculate_rent"):
            print(f"{v.get_vehicle_type()} - 7-day rent: {v.calculate_rent(7):.2f}")

    
    print("\n=== Insurable Vehicles ===")
    for v in fleet:
        if hasattr(v, "calculate_insurance_premium"):
            print(f"{v.get_vehicle_type()} Insurance premium: {v.calculate_insurance_premium():.2f}")