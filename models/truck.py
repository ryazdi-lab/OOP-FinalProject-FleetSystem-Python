from models.vehicle import Vehicle
from models.mixins import Insurable


class Truck(Vehicle, Insurable):
    def __init__(self, plate_number, brand, year, base_daily_rate, capacity):
        super().__init__(plate_number, brand, year, base_daily_rate)
        self.capacity = capacity

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError("Capacity is not valid")
        self._capacity = value

    def calculate_daily_cost(self):
        cost = self.base_daily_rate + (self.capacity * 20)
        return cost

    def get_vehicle_type(self):
        return "Truck"

    def perform_maintenance(self):
        print("Truck maintenance done.")

    def calculate_insurance_premium(self):
        premium = self.calculate_daily_cost() * 0.15
        return premium

    def is_eligible_for_coverage(self):
        return self.year >= 2005
