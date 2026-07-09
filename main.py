from models.vehicle import Vehicle
from models.car import Car
from models.motorcycle import Motorcycle
from models.truck import Truck


def run_fleet_simulation(fleet: list[Vehicle]) -> None:
    for v in fleet:
        # چندریختی: هر شیء متد خودش را اجرا می‌کند، بدون isinstance/type()
        v.display_info()
        print(f"هزینه روزانه: {v.calculate_daily_cost():.2f}")
        v.perform_maintenance()

        # duck typing: بررسی وجود متد به‌جای بررسی نوع کلاس
        if hasattr(v, "calculate_rent"):
            print(f"اجاره ۵ روزه: {v.calculate_rent(5):.2f}")
        if hasattr(v, "calculate_insurance_premium"):
            eligible = "بله" if v.is_eligible_for_coverage() else "خیر"
            print(f"حق بیمه ماهانه: {v.calculate_insurance_premium():.2f} | واجد شرایط بیمه: {eligible}")

        print("-" * 40)


def test_car_rental_age_limit() -> None:
    print("تست محدودیت سنی اجاره خودرو:")
    old_car = Car("OLD-01", "Peugeot", 2000, 80.0, seat_count=4)
    try:
        old_car.reserve()
        print("خطا: این خط نباید اجرا شود!")
    except RuntimeError as e:
        print(f"رزرو رد شد (همان‌طور که انتظار می‌رفت): {e}")
    print("-" * 40)


if __name__ == "__main__":
    fleet: list[Vehicle] = [
        Car("12345", "Toyota", 2020, 150.0, seat_count=5),
        Truck("TRK-99", "Volvo", 2018, 300.0, cargo_capacity_tons=10),
        Motorcycle("MC-01", "Honda", 2022, 40.0, engine_cc=250),
    ]
    run_fleet_simulation(fleet)
    test_car_rental_age_limit()