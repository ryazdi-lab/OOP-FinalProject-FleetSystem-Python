from models.vehicle import Vehicle
from models.car import Car
from models.motorcycle import Motorcycle
from models.truck import Truck


def run_fleet_simulation(fleet: list[Vehicle]) -> None:
    for v in fleet:
        v.display_info()
        print(f"هزینه روزانه: {v.calculate_daily_cost():.2f}")
        v.perform_maintenance()

        # قابلیت‌های اجاره (Rentable)
        v.reserve()
        print(f"هزینه اجاره به مدت ۳ روز: {v.calculate_rent(3):.2f}")
        v.return_vehicle(3)

        # قابلیت‌های بیمه (Insurable)
        print(f"حق بیمه: {v.calculate_insurance_premium():.2f}")
        print(f"وضعیت پوشش بیمه: {'معتبر' if v.is_eligible_for_coverage() else 'نامعتبر'}")
        print("-" * 40)


if __name__ == "__main__":
    fleet: list[Vehicle] = [
        Car("IR-123-45", "Toyota", 2021, 550000, 4),
        Motorcycle("IR-678-90", "Honda", 2022, 200000, 250),
        Truck("IR-999-88", "Volvo", 2019, 850000, 5.0)
    ]
    run_fleet_simulation(fleet)