from models.car import Car
from models.motorcycle import Motorcycle
from models.truck import Truck


def main() -> None:
    vehicles = [
        Car("IR-PLATE-001", "Tesla", 2023, 50, 4, True),
        Car("IR-PLATE-002", "Toyota", 2022, 40, 4, False),
        Motorcycle("IR-PLATE-003", "Harley", 2021, 30, 1200, True),
        Motorcycle("IR-PLATE-004", "Honda", 2023, 25, 471, False),
        Truck("IR-PLATE-005", "Ford", 2022, 60, 3.5, True),
        Truck("IR-PLATE-006", "Volvo", 2021, 70, 5.0, False),
    ]

    print("=" * 60)
    print("FLEET MANAGEMENT SYSTEM - POLYMORPHISM DEMO")
    print("=" * 60)

    rental_days = 3

    for vehicle in vehicles:
        vehicle.display_info()
        print(f"Daily cost: ${vehicle.calculate_daily_cost():.2f}")
        print(f"Rental cost for {rental_days} days: ${vehicle.calculate_rent(rental_days):.2f}")

        # Rentable methods
        print(f"Available for rent: {vehicle.is_available()}")
        if vehicle.is_available():
            vehicle.rent()
            print("✓ Rented successfully")
            vehicle.return_vehicle()
            print("✓ Returned successfully")

        # Insurable methods
        print(f"Insurance premium: ${vehicle.calculate_insurance_premium():.2f}")
        print(f"Coverage: {vehicle.get_coverage_details()}")

        vehicle.perform_maintenance()
        print("-" * 40)

    total_daily_cost = sum(v.calculate_daily_cost() for v in vehicles)
    print(f"\nTotal daily cost for all vehicles: ${total_daily_cost:.2f}")
    print("=" * 60)


if __name__ == "__main__":
    main()