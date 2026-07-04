from models.vehicle import Vehicle
from models.mixins import Rentable, Insurable


class Car(Vehicle, Rentable, Insurable):
    CURRENT_YEAR = 2026
    NEW_CAR_YEAR_LIMIT = 5
    NEW_CAR_EXTRA_RATE = 0.20
    OLD_CAR_EXTRA_RATE = 0.10
    INSURANCE_RATE = 0.10
    MIN_INSURANCE_YEAR = 2010

    def __init__(self,plate_number: str,brand: str,year: int,base_daily_rate: float) -> None:
        super().__init__(plate_number, brand, year, base_daily_rate)
        self._is_reserved = False

    #-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    def calculate_daily_cost(self) -> float:
        year_difference = self.CURRENT_YEAR - self.year

        # if Car is newer than 5 Years it costs 20% More and if it is Older it Costs 10% More
        if year_difference <= self.NEW_CAR_YEAR_LIMIT:
            return self.base_daily_rate + self.base_daily_rate * self.NEW_CAR_EXTRA_RATE
        else:
            return self.base_daily_rate + self.base_daily_rate * self.OLD_CAR_EXTRA_RATE
        
    #-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    # Get Vehicle Type(Just Return "Car")

    def get_vehicle_type(self) -> str:
        return "car"
    
    #-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    # Calculate Rent Using: days * Daily Cost
    def calculate_rent(self, days: int) -> float:
        rent = days * self.calculate_daily_cost()
        return rent
    
    #-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    def perform_maintenance(self) -> None:
        print(f"Oil,Tires,Brakes and Motor of the {self.brand} Are Checked")

    #-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    # Reserving Car
    def reserve(self) -> None:
        if not self._is_reserved:
            print("This Car Now Got Reserved!")
            self._is_reserved = True
        else:
            print("This Car is Already Reserved!")
        return
    
    #-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    # Return Back Car and Give Total Rent Cost
    def return_vehicle(self, actual_days: int) -> None:
        if self._is_reserved:
            total_rent = self.calculate_rent(actual_days)
            self._is_reserved = False
            print(f"The Car Got Returned! The Total Cost of Rent is {total_rent}")
        else:
            print("This Car is not Reserved at All!")
        return
    
    #-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    # Calcuمate Insurance Premium
    def calculate_insurance_premium(self) -> float:
        insurance_cost = self.calculate_daily_cost() * self.INSURANCE_RATE
        return insurance_cost
    
    #-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    # if Car Newer Than 2010, Its Eligible For Coverage
    def is_eligible_for_coverage(self) -> bool:
        if self.year >= self.MIN_INSURANCE_YEAR:
            return True
        else:
            return False