"""
Abstract base class for all vehicles in the Fleet Management System.
"""
from abc import ABC, abstractmethod


class Vehicle(ABC):
    """
    Abstract base class representing a generic vehicle.
    All vehicle types must inherit from this class.
    """
    
    def __init__(self, brand: str, model: str, year: int):
        self._brand = brand
        self._model = model
        self._year = year
        self._validate_year()
    
    def _validate_year(self) -> None:
        current_year = 2026
        if not (1900 <= self._year <= current_year):
            raise ValueError(f"Year must be between 1900 and {current_year}")
    
    @abstractmethod
    def start_engine(self) -> str:
        pass
    
    @abstractmethod
    def stop_engine(self) -> str:
        pass
    
    @abstractmethod
    def calculate_fuel_efficiency(self) -> float:
        pass
    
    @abstractmethod
    def get_info(self) -> str:
        pass
    
    @property
    def brand(self) -> str:
        return self._brand
    
    @property
    def model(self) -> str:
        return self._model
    
    @property
    def year(self) -> int:
        return self._year
    
    @year.setter
    def year(self, value: int) -> None:
        self._year = value
        self._validate_year()
    
    def __str__(self) -> str:
        return self.get_info()