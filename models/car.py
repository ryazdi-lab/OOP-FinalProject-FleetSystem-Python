from abc import ABC, abstractmethod
from .vehicle import Vehicle

class Rentable(ABC):
    @abstractmethod
    def calculate_rent(self, days: int) -> float:
        pass
    @abstractmethod
    def reserve(self) -> None:
        pass
    @abstractmethod
    def return_vehicle(self, actual_days: int) -> None:
        pass

class Insurable(ABC):
        @abstractmethod
        def calculate_insurance_premium(self) -> float:
            pass
        @abstractmethod
        def is_english_for_coverage(self) -> bool:
            pass

class Car(Vehicle, Rentable, Insurable):
    def calculate_daily_cost(self) -> float:
        return self.base_daily_rate *1.2

    def get_vehicle_type(self) -> str:
        return "car"
    def perform_maintenance(self) -> None:
        print(f" تعمیرات ماشین انجام شد{self.brand}")
    def calculate_rent(self, days: int) -> float:
        return self.calculate_daily_cost() * days
    def reserve(self) -> None:
        print(f"ماشین رزرو شد {self.brand}")
    def return_vehicle(self, actual_days: int) -> None:
        print(f" ماشین{self.brand} بعد از {actual_days} روز برگردونده شد.")

    #حق بیمه
    def calculate_insurance_premium(self) -> float:
        return self.base_daily_rate * 0.1

    def is_english_for_coverage(self) -> bool:
        return self.year >= 2021
