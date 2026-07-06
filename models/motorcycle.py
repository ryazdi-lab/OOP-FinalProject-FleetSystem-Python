from models.vehicle import Vehicle
from models.mixins import Rentable

# Rentable Motorcycle But Not Insurable
class Motorcycle(Vehicle, Rentable):
    CURRENT_YEAR = 2026
    NEW_MOTORCYCLE_YEAR_LIMIT = 5
    NEW_MOTORCYCLE_EXTRA_RATE = 0.15
    OLD_MOTORCYCLE_EXTRA_RATE = 0.08
    ENGINE_CAPACITY_RATE = 0.03

    def __init__(
        self,
        plate_number: str,
        brand: str,
        year: int,
        base_daily_rate: float,
        engine_capacity: float
    ) -> None:
        super().__init__(plate_number, brand, year, base_daily_rate)
        # CC
        self._engine_capacity = engine_capacity
        self._is_reserved = False

    #-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    def calculate_daily_cost(self) -> float:
        year_difference = self.CURRENT_YEAR - self.year

        # if Motorcycle is newer than 5 Years it costs 15% More because newer motorcycles have better performance
        if year_difference <= self.NEW_MOTORCYCLE_YEAR_LIMIT:
            daily_cost = self.base_daily_rate + self.base_daily_rate * self.NEW_MOTORCYCLE_EXTRA_RATE
        else:
            daily_cost = self.base_daily_rate + self.base_daily_rate * self.OLD_MOTORCYCLE_EXTRA_RATE

        # Motorcycle daily cost also depends on engine capacity because higher CC usually costs more
        daily_cost += self._engine_capacity * self.ENGINE_CAPACITY_RATE

        return daily_cost

    #-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    # Get Vehicle Type(Just Return "Motorcycle")

    def get_vehicle_type(self) -> str:
        return "Motorcycle"

    #-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    # Calculate Rent Using: days * Daily Cost
    def calculate_rent(self, days: int) -> float:
        rent = days * self.calculate_daily_cost()
        return rent

    #-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    def perform_maintenance(self) -> None:
        print(f"Oil,Tires,Brakes and Chain of the {self.brand} Are Checked")

    #-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    # Reserving Motorcycle
    def reserve(self) -> None:
        if not self._is_reserved:
            print("This Motorcycle Now Got Reserved!")
            self._is_reserved = True
        else:
            print("This Motorcycle is Already Reserved!")
        return

    #-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    # Return Back Motorcycle and Give Total Rent Cost
    def return_vehicle(self, actual_days: int) -> None:
        if self._is_reserved:
            total_rent = self.calculate_rent(actual_days)
            self._is_reserved = False
            print(f"The Motorcycle Got Returned! The Total Cost of Rent is {total_rent}")
        else:
            print("This Motorcycle is not Reserved at All!")
        return