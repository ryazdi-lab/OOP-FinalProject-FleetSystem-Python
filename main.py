from models.vehicle import Vehicle
from models.car import Car
from models.truck import Truck
from models.motorcycle import Motorcycle
print("\n")

def run_fleet_simulation(fleet: list[Vehicle]) -> None:
    for v in fleet:
        v.display_info()
        print(f"هزینه روزانه: {v.calculate_daily_cost():.2f}")
        v.perform_maintenance()
        print("-" * 40)


if __name__ == "__main__":
    # دانشجویان اینجا اشیاء concrete را می‌سازند و به لیست اضافه می‌کنند
    # Car Inputs: plate_number, brand, year, base_daily_rate
    car = Car("12345", "Toyota", 2020, 150.0)
    # Truck Inputs: plate_number, brand, year, base_daily_rate, load_capacity(Tons)
    truck = Truck("TRK-99", "Volvo", 2018, 300.0, 25)
    # Motorcycle Inputs: plate_number, brand, year, base_daily_rate, engine_capacity(CC)
    motorcycle = Motorcycle("MTR-12", "Honda", 2022, 80.0, 200)

    fleet: list[Vehicle] = [
        car,
        truck,
        motorcycle,
    ]

    run_fleet_simulation(fleet)

    print("Rent Test:")
    car.reserve()
    car.return_vehicle(3)

    motorcycle.reserve()
    motorcycle.return_vehicle(2)

    print("-" * 40)

    print("Insurance Test:")
    print(f"Car Insurance: {car.calculate_insurance_premium()}")
    print(f"Truck Insurance: {truck.calculate_insurance_premium()}")

    print("-" * 40)

    print("Coverage Test:")
    print(f"Car Coverage: {car.is_eligible_for_coverage()}")
    print(f"Truck Coverage: {truck.is_eligible_for_coverage()}")