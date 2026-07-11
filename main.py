from models.car import Car
from models.motorcycle import Motorcycle
from models.truck import Truck
from models.vehicle import Vehicle


def run_fleet_simulation(fleet: list[Vehicle]) -> None:
    for v in fleet:
        v.display_info()
        print(f"هزینه روزانه: {v.calculate_daily_cost():.2f}")
        v.perform_maintenance()
        print("-" * 40)


def run_car_tests(car: Car) -> None:
    print("تست‌های خودرو")
    print(f"نوع وسیله: {car.get_vehicle_type()}")
    print(f"ظرفیت سرنشین: {car.passenger_capacity}")
    print(f"هزینه اجاره برای 3 روز: {car.calculate_rent(3):.2f}")

    car.reserve()
    print(f"وضعیت رزرو: {car.is_reserved}")

    car.return_vehicle(3)
    print(f"وضعیت رزرو بعد از بازگشت: {car.is_reserved}")

    print(f"حق بیمه ماهانه: {car.calculate_insurance_premium():.2f}")
    print(f"واجد شرایط بیمه: {car.is_eligible_for_coverage()}")
    print("-" * 40)


def run_motorcycle_tests(motorcycle: Motorcycle) -> None:
    print("تست‌های موتورسیکلت")
    print(f"نوع وسیله: {motorcycle.get_vehicle_type()}")
    print(f"حجم موتور: {motorcycle.engine_capacity} سی‌سی")
    print(f"هزینه اجاره برای 3 روز: {motorcycle.calculate_rent(3):.2f}")

    motorcycle.reserve()
    print(f"وضعیت رزرو: {motorcycle.is_reserved}")

    motorcycle.return_vehicle(3)
    print(f"وضعیت رزرو بعد از بازگشت: {motorcycle.is_reserved}")
    print("-" * 40)


def run_truck_tests(truck: Truck) -> None:
    print("تست‌های کامیون")
    print(f"نوع وسیله: {truck.get_vehicle_type()}")
    print(f"ظرفیت بار: {truck.load_capacity:.1f} تن")
    print(f"حق بیمه ماهانه: {truck.calculate_insurance_premium():.2f}")
    print(f"واجد شرایط بیمه: {truck.is_eligible_for_coverage()}")
    print("-" * 40)


if __name__ == "__main__":
    car = Car("12A345", "Toyota", 2020, 150.0)
    motorcycle = Motorcycle("M-204", "Honda", 2022, 80.0)
    truck = Truck("TRK-99", "Volvo", 2018, 300.0)

    # هر سه شیء داخل یک لیست از نوع Vehicle قرار می‌گیرند
    fleet: list[Vehicle] = [car, motorcycle, truck]

    print("اجرای متدهای مشترک وسایل نقلیه")
    run_fleet_simulation(fleet)

    # متدهای مخصوص هر کلاس به صورت جداگانه بررسی می‌شوند
    run_car_tests(car)
    run_motorcycle_tests(motorcycle)
    run_truck_tests(truck)
