from models.vehicle import Vehicle
from models.mixins import Rentable, Insurable


class Car(Vehicle, Rentable, Insurable):
    def __init__(self, plate_number, brand, year, base_daily_rate, seats):
        super().__init__(plate_number, brand, year, base_daily_rate)
        self.seats = seats
        self._reserved = False

    @property
    def seats(self):
        return self._seats

    @seats.setter
    def seats(self, value):
        if value < 2:
            raise ValueError("Seats is not valid")
        self._seats = value

    def calculate_daily_cost(self):
        cost = self.base_daily_rate + (self.seats * 10)
        return cost

    def get_vehicle_type(self):
        return "Car"

    def perform_maintenance(self):
        print("Car maintenance done.")

    def calculate_rent(self, days):
        rent = self.calculate_daily_cost() * days
        return rent

    def reserve(self):
        if self._reserved:
            print("Car is already reserved.")
        else:
            self._reserved = True
            print("Car reserved.")

    def return_vehicle(self, actual_days):
        self._reserved = False
        print("Car returned after", actual_days, "days.")

    def calculate_insurance_premium(self):
        premium = self.calculate_daily_cost() * 0.1
        return premium

    def is_eligible_for_coverage(self):
        return self.year >= 2000
