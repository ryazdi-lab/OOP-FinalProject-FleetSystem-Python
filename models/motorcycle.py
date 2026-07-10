from models.vehicle import Vehicle
from models.mixins import Rentable


class Motorcycle(Vehicle, Rentable):
    def __init__(self, plate_number, brand, year, base_daily_rate, engine_cc):
        super().__init__(plate_number, brand, year, base_daily_rate)
        self.engine_cc = engine_cc
        self._reserved = False

    @property
    def engine_cc(self):
        return self._engine_cc

    @engine_cc.setter
    def engine_cc(self, value):
        if value <= 0:
            raise ValueError("Engine CC is not valid")
        self._engine_cc = value

    def calculate_daily_cost(self):
        cost = self.base_daily_rate + (self.engine_cc * 0.05)
        return cost

    def get_vehicle_type(self):
        return "Motorcycle"

    def perform_maintenance(self):
        print("Motorcycle maintenance done.")

    def calculate_rent(self, days):
        rent = self.calculate_daily_cost() * days
        return rent

    def reserve(self):
        if self._reserved:
            print("Motorcycle is already reserved.")
        else:
            self._reserved = True
            print("Motorcycle reserved.")

    def return_vehicle(self, actual_days):
        self._reserved = False
        print("Motorcycle returned after", actual_days, "days.")
