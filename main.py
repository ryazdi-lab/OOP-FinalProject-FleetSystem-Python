from models import Vehicle, Car, Motorcycle, Truck

def run_fleet_simulation(fleet: list[Vehicle]) -> None:
    print("=" * 70)
    print(" شبیه‌سازی مدیریت ناوگان حمل‌ونقل")
    print("=" * 70)

    for v in fleet:
        print(f"\n نوع وسیله: {v.get_vehicle_type()}")
        v.display_info()
        print(f" هزینه روزانه: {v.calculate_daily_cost():,} تومان")
        v.perform_maintenance()

        if hasattr(v, 'calculate_rent'):
            rent_cost = v.calculate_rent(3)
            print(f" هزینه اجاره به مدت ۳ روز: {rent_cost:,} تومان")
            v.reserve()
            v.return_vehicle()

        if hasattr(v, 'calculate_insurance_premium'):
            premium = v.calculate_insurance_premium()
            print(f" حق بیمه سالانه: {premium:,} تومان")
            if v.is_eligible_for_coverage():
                print("✅ وضعیت بیمه: پوشش کامل")
            else:
                print("⚠️ وضعیت بیمه: پوشش محدود")

        print("-" * 70)

if __name__ == "__main__":
    fleet: list[Vehicle] = [
      
        Car("۱۲-ب-۳۴۵-۶۷", "پراید ۱۱۱", 2020, 85000.0, doors=4),   

        Car("۷۹-ج-۲۲۲-۸۸", "سمند ال‌ایکس", 2017, 130000.0, doors=4), 
        Car("۵۶-د-۷۸۹-۱۰", "پژو ۲۰۶ وی۸", 2022, 160000.0, doors=4),  
        Car("۳۳-س-۱۱۱-۲۲", "دنا پلاس", 2021, 1450000.0, doors=4),     
        Car("۹۱-ص-۹۹۹-۰۰", "تارا دنده‌ای", 2023, 1750000.0, doors=4), 

   
        Motorcycle("۳۴-س-۱۲۳-۴۵", "هندا سی‌جی ۱۲۵", 2021, 55000.0, engine_cc=125), 
        Motorcycle("۹۰-ص-۵۵۵-۷۷", "مينسک ۲۰۰", 2016, 45000.0, engine_cc=200),     
        Motorcycle("۶۷-ط-۷۷۷-۱۳", "کویر ۳۰۰", 2019, 65000.0, engine_cc=300),      

        Truck("۲۳-ت-۶۶۶-۹۹", "ولوو اف‌اچ", 2018, 3200000.0, cargo_capacity_ton=25.0), 
        Truck("۴۵-ع-۷۷۷-۳۳", "کاوه کامیونت", 2021, 2200000.0, cargo_capacity_ton=8.5),
        Truck("۸۸-م-۴۴۴-۵۵", "بنز اکتروس", 2015, 4000000.0, cargo_capacity_ton=30.0),
    ]

    run_fleet_simulation(fleet)