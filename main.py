from models.vehicle import Vehicle
from models.car import Car
from models.motorcycle import Motorcycle
from models.truck import Truck


def run_fleet_simulation(fleet: list[Vehicle]) -> None:
    for v in fleet:
        v.display_info()

        #  هزینه روزانه بدون پارامتر
        print(f" هزینه روزانه: {v.calculate_daily_cost():.2f}")

        # هزینه بیمه با چک کردن وجود متد
        if hasattr(v, 'calculate_insurance_premium'):
            print(f"️ حق بیمه روزانه: {v.calculate_insurance_premium():.2f}")

        #  سرویس دوره‌ای
        v.perform_maintenance()

        #  قابلیت کرایه
        if hasattr(v, 'calculate_rent'):
            rent_3_days = v.calculate_rent(3)
            print(f" کرایه ۳ روزه: {rent_3_days:.2f}")
            v.reserve()
            v.return_vehicle(3)

        print("-" * 50)


if __name__ == "__main__":
    fleet: list[Vehicle] = [
        Car("88 س 987 85", "BMW", 2022, 350.0, 4),
        Motorcycle("887799 گ 42", "Yamaha", 2023, 230.0, 2),
        Truck("23ث 335 42", "Volvo", 2021, 400.0, 2500)
    ]
    run_fleet_simulation(fleet)
