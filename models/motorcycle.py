"""
Motorcycle class implementation for Fleet Management System.
"""
from models.vehicle import Vehicle
from models.mixins import Rentable, Insurable


class Motorcycle(Vehicle, Rentable, Insurable):
    """
    Motorcycle class with rental and insurance capabilities.
    """
    
    def __init__(
        self,
        brand: str,
        model: str,
        year: int,
        daily_rental_price: float,
        insurance_premium: float,
        engine_cc: int
    ):
        super().__init__(brand, model, year)
        
        self._daily_rental_price = daily_rental_price
        self._insurance_premium = insurance_premium
        self._engine_cc = engine_cc
        self._is_rented = False
        self._is_insured = True
        
        self._validate_engine()
    
    def _validate_engine(self) -> None:
        """Validate engine displacement."""
        if not (50 <= self._engine_cc <= 2000):
            raise ValueError("Engine displacement must be between 50cc and 2000cc")
    
    # Vehicle abstract methods
    def start_engine(self) -> str:
        return f"🏍️ {self.get_info()}: Engine roars to life!"
    
    def stop_engine(self) -> str:
        return f"🏍️ {self.get_info()}: Engine shut down. Kickstand deployed."
    
    def calculate_fuel_efficiency(self) -> float:
        """
        Fuel efficiency decreases with larger engines.
        """
        if self._engine_cc < 200:
            return 35.0
        elif self._engine_cc < 500:
            return 25.0
        elif self._engine_cc < 1000:
            return 18.0
        else:
            return 12.0
    
    # Rentable methods
    def rent(self, days: int) -> float:
        if days <= 0:
            raise ValueError("Rental days must be positive")
        if self._is_rented:
            raise ValueError(f"{self.get_info()} is already rented")
        
        self._is_rented = True
        total_cost = self._daily_rental_price * days
        
        # Motorcycles get 10% discount for 5+ days
        if days >= 5:
            total_cost *= 0.90
        
        return round(total_cost, 2)
    
    def return_vehicle(self) -> str:
        if not self._is_rented:
            raise ValueError(f"{self.get_info()} is not currently rented")
        
        self._is_rented = False
        return f"✅ {self.get_info()} returned. Helmet checked in!"
    
    def is_available(self) -> bool:
        return not self._is_rented
    
    # Insurable methods
    def calculate_insurance(self) -> float:
        """Insurance is higher for powerful motorcycles."""
        if self._engine_cc > 1000:
            multiplier = 1.8
        elif self._engine_cc > 600:
            multiplier = 1.4
        elif self._engine_cc < 200:
            multiplier = 0.7
        else:
            multiplier = 1.0
        
        return round(self._insurance_premium * multiplier, 2)
    
    def get_insurance_details(self) -> dict:
        return {
            "vehicle_type": "Motorcycle",
            "brand": self._brand,
            "model": self._model,
            "engine_cc": self._engine_cc,
            "base_premium": self._insurance_premium,
            "final_premium": self.calculate_insurance(),
            "is_insured": self._is_insured
        }
    
    # Properties
    @property
    def engine_cc(self) -> int:
        return self._engine_cc
    
    @engine_cc.setter
    def engine_cc(self, value: int) -> None:
        self._engine_cc = value
        self._validate_engine()
    
    @property
    def daily_rental_price(self) -> float:
        return self._daily_rental_price
    
    def get_info(self) -> str:
        return f"Motorcycle: {self._brand} {self._model} ({self._engine_cc}cc)"