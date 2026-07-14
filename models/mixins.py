from abc import ABC, abstractmethod


class Rentable(ABC):
    @abstractmethod
    def calculate_rent(self, days: int) -> float: ...
    @abstractmethod
    def reserve(self) -> None: ...
    @abstractmethod
    def return_vehicle(self, actual_days: int) -> None: ...


class Insurable(ABC):
    @abstractmethod
    def calculate_insurance_premium(self) -> float: ...
    @abstractmethod
    def is_eligible_for_coverage(self) -> bool: ...
