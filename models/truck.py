from models.vehicle import Vehicle
from models.mixins import Insurable


class Truck(Vehicle, Insurable):
    CURRENT_YEAR = 2026
    NEW_TRUCK_YEAR_LIMIT = 5
    NEW_TRUCK_EXTRA_RATE = 0.20
    OLD_TRUCK_EXTRA_RATE = 0.40
    INSURANCE_RATE = 0.25
    MIN_INSURANCE_YEAR = 2000
    LOAD_CAPACITY_RATE = 15
    def __init__(
        self,
        plate_number: str,
        brand: str,
        year: int,
        base_daily_rate: float,
        load_capacity: float
    ) -> None:
        super().__init__(plate_number, brand, year, base_daily_rate)
        # Tons
        self._load_capacity = load_capacity

    #-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    def calculate_daily_cost(self) -> float:
        year_difference = self.CURRENT_YEAR - self.year

        # if Truck is newer than 5 Years it costs 20% More and if it is Older it Costs 40% More
        # because old trucks need more maintenance and service
        if year_difference <= self.NEW_TRUCK_YEAR_LIMIT:
            daily_cost = self.base_daily_rate + self.base_daily_rate * self.NEW_TRUCK_EXTRA_RATE
        else:
            daily_cost = self.base_daily_rate + self.base_daily_rate * self.OLD_TRUCK_EXTRA_RATE

        # Truck daily cost also depends on load capacity because bigger trucks have more operational cost
        daily_cost += self._load_capacity * self.LOAD_CAPACITY_RATE

        return daily_cost
    
    #-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    # Get Vehicle Type(Just Return "Truck")

    def get_vehicle_type(self) -> str:
        return "Truck"
    
    #-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    def perform_maintenance(self) -> None:
        print(f"Oil,Tires,Brakes,Engine and Cargo System of the {self.brand} Are Checked")

    #-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    # Calculate Insurance Premium
    def calculate_insurance_premium(self) -> float:
        insurance_cost = self.calculate_daily_cost() * self.INSURANCE_RATE
        return insurance_cost
    
    #-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    # if Truck Newer Than 2000, Its Eligible For Coverage
    def is_eligible_for_coverage(self) -> bool:
        if self.year >= self.MIN_INSURANCE_YEAR:
            return True
        else:
            return False