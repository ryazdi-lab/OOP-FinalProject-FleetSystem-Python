from models.vehicle import Vehicle
from models.car import Car
from models.motorcycle import Motorcycle
from models.truck import Truck

def start_simulation(vehicle_list: list[Vehicle]) -> None:
    for index, v in enumerate(vehicle_list, 1):
        print(f"\n========== وسیله شماره {index} ==========")
        v.display_info()        
        premium = v.calculate_insurance_premium()
        eligible = v.is_eligible_for_coverage()
        print(f"حق بیمه: {premium:,.0f} تومان")
        print(f"پوشش بیمه: {'فعال' if eligible else 'غیرفعال'}")

        days = 4
        v.reserve()
        rent_fee = v.calculate_rent(days)
        print(f"هزینه اجاره برای {days} روز: {rent_fee:,.0f} تومان")
        v.return_vehicle(days)

        daily = v.calculate_daily_cost()
        print(f"هزینه روزانه: {daily:,.0f} تومان")
        v.perform_maintenance()

        print("==========================================\n")


if __name__ == "__main__":
    fleet = [
        Car("IR-111-AA", "Renault", 2020, 480000, 4),
        Motorcycle("IR-222-BB", "Kawasaki", 2019, 190000, 300),
        Truck("IR-333-CC", "Scania", 2018, 820000, 6.5)
    ]
    start_simulation(fleet)