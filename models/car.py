from .vehicle import Vehicle
from .mixins import Rentable, Insurable

class Car(Vehicle, Rentable, Insurable):
    def __init__(self, brand: str, model: str, year: int, daily_rate: float):
        super().__init__(brand, model, year)
        self._daily_rate = daily_rate
        self._is_rented = False

    @property
    def daily_rate(self) -> float:
        return self._daily_rate

    def calculate_rental_cost((self, days: int) -> float):
        return self._daily_rate * days

    def get_insurance_quote((self) -> float):
        # منطق محاسبه بیمه برای ماشین: ۵٪ قیمت پایه بر اساس سال
        base_premium = 500.0
        age_factor = (2024 - self.year) * 10
        return base_premium + age_factor

    def get_description((self) -> str):
        return f"Car: {self.brand} {self.model} ({self.year}) - Rate: ${self.daily_rate}/day"
