"""نقطهٔ ورود برنامه و نمایش چندریختی (Polymorphism).

کل گزارش‌گیری روی یک آرایهٔ عمومی ``list[Vehicle]`` انجام می‌شود؛
هیچ‌جا از ``isinstance`` یا ``type()`` برای تصمیم‌گیری استفاده نشده است.
برای قابلیت‌های اختیاری (اجاره/بیمه) از duck typing با ``hasattr``
استفاده می‌کنیم.
"""

from models import Vehicle, Car, Motorcycle, Truck


def build_fleet() -> list[Vehicle]:
    """ساخت یک ناوگان نمونه."""
    return [
        Car("Toyota", "Corolla", 2021, 800_000_000, num_doors=4),
        Motorcycle("Honda", "CBR", 2022, 300_000_000, engine_cc=650),
        Truck("Volvo", "FH16", 2019, 3_000_000_000, cargo_capacity=20),
    ]


def print_report(fleet: list[Vehicle]) -> None:
    print("=" * 60)
    print("گزارش ناوگان".center(60))
    print("=" * 60)

    total_maintenance = 0.0
    for vehicle in fleet:  # ← چندریختی: بدون isinstance/type
        print(vehicle.describe())
        total_maintenance += vehicle.calculate_maintenance_cost()

        # قابلیت بیمه (اختیاری) — تشخیص با duck typing نه نوع کلاس
        if hasattr(vehicle, "calculate_insurance"):
            print(f"    بیمهٔ سالانه : {vehicle.calculate_insurance():,.0f} تومان")

        # قابلیت اجاره (اختیاری)
        if hasattr(vehicle, "calculate_rental_cost"):
            weekly = vehicle.calculate_rental_cost(7)
            print(f"    اجارهٔ ۷ روزه: {weekly:,.0f} تومان (با تخفیف بلندمدت)")
        else:
            print("    اجاره       : این وسیله قابل اجاره نیست")

        print("-" * 60)

    print(f"جمع هزینهٔ نگهداری سالانهٔ ناوگان: {total_maintenance:,.0f} تومان")
    print("=" * 60)


def main() -> None:
    fleet = build_fleet()
    print_report(fleet)


if __name__ == "__main__":
    main()
