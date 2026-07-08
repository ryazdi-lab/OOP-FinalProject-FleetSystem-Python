from .mixins import Rentable, Insurable
from datetime import date
from .vehicle import Vehicle



# چون در پروژه از زبان فارسی به عنوان زبان نمایشی استفاده شده متن های نمایشی مدل ها هم از فارسی استفاده شده

class Car(Vehicle, Rentable, Insurable):
    def __init__(self, plate_number, brand, year, base_daily_rate):
        super().__init__(plate_number, brand, year, base_daily_rate)

    def calculate_daily_cost(self) -> float:
        this_year = date.today().year
        car_age = this_year - self.year
        if car_age <= 3:
            return self.base_daily_rate * 1.2
        elif 3 < car_age <= 10:
            return self.base_daily_rate * 1
        else:
            return self.base_daily_rate * 0.8

    def get_vehicle_type(self) -> str:
        return "ماشین"

    def perform_maintenance(self) -> None:
        print("ماشین سرویس شد و موتور خودرو چک شد")

    def calculate_rent(self, days: int) -> float:
        return self.calculate_daily_cost() * days

    def reserve(self) -> None:
        print(f"خودرو !\t{self.brand}-{self.year} رزرو شد")

    def return_vehicle(self, actual_days: int) -> None:
        print(f"خودرو پس از {actual_days} روز تحویل داده شد")

    def calculate_insurance_premium(self) -> float:
        if not self.is_eligible_for_coverage():
            return 0
        return self.calculate_daily_cost() * 0.1

    def is_eligible_for_coverage(self) -> bool:
        current_year = date.today().year
        return current_year - self.year <= 20


class Motorcycle(Vehicle, Rentable, Insurable):
    def __init__(self, plate_number, brand, year, base_daily_rate, engine_cc: int):
        super().__init__(plate_number, brand, year, base_daily_rate)
        self.engine_cc = engine_cc
        
    @property
    def engine_cc(self) -> int:
        return self._engine_cc

    @engine_cc.setter
    def engine_cc(self, value: int) -> None:
        if value <= 40 or value > 1100:
            raise ValueError("حجم موتور معتبر نیست")
        self._engine_cc = value

    def calculate_daily_cost(self) -> float:
        return self.base_daily_rate + (self.engine_cc / 100)

    def get_vehicle_type(self) -> str:
        return "موتورسیکلت"

    def perform_maintenance(self) -> None:
        print("زنجیرها و تایرهای موتورسیکلت چک شد.")

    def calculate_rent(self, days: int) -> float:
        return self.calculate_daily_cost() * days

    def reserve(self) -> None:
        print(f"موتورسیکلت با مشخصات !\t{self.brand}-{self.year}: {self.engine_cc} رزرو شد.")

    def return_vehicle(self, actual_days: int) -> None:
        print(f"موتورسیکلت بعد از {actual_days} روز تحویل داده شد.")

    def calculate_insurance_premium(self) -> float:
        if not self.is_eligible_for_coverage():
            return 0
        return self.calculate_daily_cost() * 0.1

    def is_eligible_for_coverage(self) -> bool:
        current_year = date.today().year
        return current_year - self.year <= 20


class Truck(Vehicle, Insurable):
    def __init__(self, plate_number, brand, year, base_daily_rate, number_of_wheels:int):
        super().__init__(plate_number, brand, year, base_daily_rate)
        self.number_of_wheels = number_of_wheels

    @property
    def number_of_wheels(self) -> int:
        return self._number_of_wheels

    @number_of_wheels.setter
    def number_of_wheels(self, value: int) -> None:
        if not isinstance(value, int):
            raise ValueError("چرخ های کامیون باید یک عدد طبیعی باشد!")
        if value < 4 or value > 20:
            raise ValueError("تعداد چرخ های کامیون درست نمیباشد")
        self._number_of_wheels = value

    def calculate_daily_cost(self) -> float:
        return self.base_daily_rate + (self.number_of_wheels * 8)

    def get_vehicle_type(self) -> str:
        return "کامیون"

    def perform_maintenance(self) -> None:
        print("ترمزها و کابین کامیون چک شد.")

    def calculate_insurance_premium(self) -> float:
        if not self.is_eligible_for_coverage():
            return 0
        return self.calculate_daily_cost() * 0.1

    def is_eligible_for_coverage(self) -> bool:
        current_year = date.today().year
        return current_year - self.year <= 20