"""
Car class implementation for Fleet Management System.
"""
from models.vehicle import Vehicle
from models.mixins import Rentable, Insurable


class Car(Vehicle, Rentable, Insurable):
    """
    Car class with rental and insurance capabilities.
    """
    
    def __init__(
        self,
        brand: str,
        model: str,
        year: int,
        daily_rental_price: float,
        insurance_premium: float,
        number_of_doors: int,
        fuel_type: str
    ):
        super().__init__(brand, model, year)
        
        # Private attributes
        self._daily_rental_price = daily_rental_price
        self._insurance_premium = insurance_premium
        self._number_of_doors = number_of_doors
        self._fuel_type = fuel_type
        self._is_rented = False
        self._is_insured = True
        
        # Validation
        self._validate_doors()
    
    def _validate_doors(self) -> None:
        """Validate number of doors."""
        if not (2 <= self._number_of_doors <= 5):
            raise ValueError("Number of doors must be between 2 and 5")
    
    # Vehicle abstract methods
    def start_engine(self) -> str:
        return f"🚗 {self.get_info()}: Engine started. Ready to drive!"
    
    def stop_engine(self) -> str:
        return f"🚗 {self.get_info()}: Engine stopped. Parking brake engaged."
    
    def calculate_fuel_efficiency(self) -> float:
        """Calculate fuel efficiency in km/liter. Smaller cars (2 doors) are more efficient."""
        base_efficiency = 12.5
        if self._number_of_doors == 2:
            return base_efficiency * 1.3
        elif self._number_of_doors == 3:
            return base_efficiency * 1.1
        return base_efficiency
    
    # Rentable methods
    def rent(self, days: int) -> float:
        if days <= 0:
            raise ValueError("Rental days must be positive")
        if self._is_rented:
            raise ValueError(f"{self.get_info()} is already rented")
        
        self._is_rented = True
        total_cost = self._daily_rental_price * days
        
        # Apply discount for long-term rental
        if days >= 7:
            total_cost *= 0.85
        elif days >= 3:
            total_cost *= 0.95
        
        return round(total_cost, 2)
    
    def return_vehicle(self) -> str:
        if not self._is_rented:
            raise ValueError(f"{self.get_info()} is not currently rented")
        
        self._is_rented = False
        return f"✅ {self.get_info()} returned successfully. Thank you!"
    
    def is_available(self) -> bool:
        return not self._is_rented
    
    # Insurable methods
    def calculate_insurance(self) -> float:
        """Calculate insurance cost based on vehicle age."""
        current_year = 2026
        age = current_year - self._year
        
        if age > 10:
            multiplier = 1.5
        elif age > 5:
            multiplier = 1.2
        elif age < 3:
            multiplier = 0.8
        else:
            multiplier = 1.0
        
        return round(self._insurance_premium * multiplier, 2)
    
    def get_insurance_details(self) -> dict:
        return {
            "vehicle_type": "Car",
            "brand": self._brand,
            "model": self._model,
            "year": self._year,
            "base_premium": self._insurance_premium,
            "final_premium": self.calculate_insurance(),
            "is_insured": self._is_insured
        }
    
    # Properties for encapsulation
    @property
    def number_of_doors(self) -> int:
        return self._number_of_doors
    
    @number_of_doors.setter
    def number_of_doors(self, value: int) -> None:
        self._number_of_doors = value
        self._validate_doors()
    
    @property
    def fuel_type(self) -> str:
        return self._fuel_type
    
    @property
    def daily_rental_price(self) -> float:
        return self._daily_rental_price
    
    def get_info(self) -> str:
        return f"Car: {self._brand} {self._model} ({self._year})"