from models.vehicle_insurable import VehicleInsurable


class Truck(VehicleInsurable):
    def perform_maintenance(self) -> None:
        print("checking transmission... changing tires")
