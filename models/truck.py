"""
Truck class implementation for Fleet Management System.
"""
from models.vehicle import Vehicle
from models.mixins import Rentable


class Truck(Vehicle, Rentable):
    """
    Truck class with rental capability (no insurance in this example).
    """
    
    def __init__(
        self,
        brand: str,
        model: str,
        year: int,
        daily_rental_price: float,
        cargo_capacity_kg: float,
        number_of_axles: int
    ):
        super().__init__(brand, model, year)
        
        self._daily_rental_price = daily_rental_price
        self._cargo_capacity_kg = cargo_capacity_kg
        self._number_of_axles = number_of_axles
        self._is_rented = False
        
        self._validate_cargo()
        self._validate_axles()
    
    def _validate_cargo(self) -> None:
        """Validate cargo capacity."""
        if self._cargo_capacity_kg <= 0:
            raise ValueError("Cargo capacity must be positive")
        if self._cargo_capacity_kg > 40000:
            raise ValueError("Cargo capacity exceeds legal limit (40,000kg)")
    
    def _validate_axles(self) -> None:
        """Validate number of axles."""
        if not (2 <= self._number_of_axles <= 5):
            raise ValueError("Number of axles must be between 2 and 5")
    
    # Vehicle abstract methods
    def start_engine(self) -> str:
        return f"🚛 {self.get_info()}: Diesel engine rumbles. Air brakes released."
    
    def stop_engine(self) -> str:
        return f"🚛 {self.get_info()}: Engine off. Air brakes engaged."
    
    def calculate_fuel_efficiency(self) -> float:
        """
        Trucks are less efficient. More axles = more drag = less efficiency.
        """
        base_efficiency = 4.5  # km per liter for trucks
        
        # Efficiency decreases with more axles
        if self._number_of_axles == 2:
            return base_efficiency
        elif self._number_of_axles == 3:
            return base_efficiency * 0.85
        else:
            return base_efficiency * 0.70
    
    # Rentable methods
    def rent(self, days: int) -> float:
        if days <= 0:
            raise ValueError("Rental days must be positive")
        if self._is_rented:
            raise ValueError(f"{self.get_info()} is already rented")
        
        self._is_rented = True
        total_cost = self._daily_rental_price * days
        
        # Trucks have special weekly rate
        if days >= 7:
            weeks = days // 7
            remainder = days % 7
            total_cost = (weeks * self._daily_rental_price * 7 * 0.80) + (remainder * self._daily_rental_price)
        elif days >= 3:
            total_cost *= 0.92
        
        return round(total_cost, 2)
    
    def return_vehicle(self) -> str:
        if not self._is_rented:
            raise ValueError(f"{self.get_info()} is not currently rented")
        
        self._is_rented = False
        return f"✅ {self.get_info()} returned. Cargo bay inspected."
    
    def is_available(self) -> bool:
        return not self._is_rented
    
    # Properties
    @property
    def cargo_capacity_kg(self) -> float:
        return self._cargo_capacity_kg
    
    @cargo_capacity_kg.setter
    def cargo_capacity_kg(self, value: float) -> None:
        self._cargo_capacity_kg = value
        self._validate_cargo()
    
    @property
    def number_of_axles(self) -> int:
        return self._number_of_axles
    
    @number_of_axles.setter
    def number_of_axles(self, value: int) -> None:
        self._number_of_axles = value
        self._validate_axles()
    
    @property
    def daily_rental_price(self) -> float:
        return self._daily_rental_price
    
    def get_info(self) -> str:
        return f"Truck: {self._brand} {self._model} ({self._cargo_capacity_kg}kg capacity)"