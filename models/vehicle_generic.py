from models.vehicle import Vehicle


class VehicleGeneric(Vehicle):

    def calculate_daily_cost(self) -> float:
        return self.base_daily_rate

    def get_vehicle_type(self) -> str:
        return self.__class__.__name__
