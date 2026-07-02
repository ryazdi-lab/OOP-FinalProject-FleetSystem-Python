from models.vehicle import Vehicle
from models.car import Car
from models.motorcycle import Motorcycle
from models.truck import Truck


def run_fleet_simulation(fleet: list[Vehicle]) -> None:
    for vehicle in fleet:
        vehicle.display_info()
        print(f"Daily cost: {vehicle.calculate_daily_cost():.2f}")
        vehicle.perform_maintenance()

        if hasattr(vehicle, "calculate_insurance_premium"):
            print(
                f"Insurance: "
                f"{vehicle.calculate_insurance_premium():.2f}"
            )

        print("-" * 40)


if __name__ == "__main__":
    fleet: list[Vehicle] = [
        Car("12345", "mazda", 2020, 150.0),
        Motorcycle("67890", "pride", 2022, 90.0),
        Truck("TRK-99", "Peugeot", 2019, 300.0),
    ]

    run_fleet_simulation(fleet)