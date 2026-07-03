from abc import ABC, abstractmethod


class Rentable(ABC):
    @abstractmethod
    def rent(self, days: int) -> float:
        pass
    
    @abstractmethod
    def return_vehicle(self) -> str:
        pass
    
    @abstractmethod
    def is_available(self) -> bool:
        pass


class Insurable(ABC):
    @abstractmethod
    def calculate_insurance(self) -> float:
        pass
    
    @abstractmethod
    def get_insurance_details(self) -> dict:
        pass