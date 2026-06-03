from models.vehicle_rentable import VehicleRentable


class Motorcycle(VehicleRentable):
    def perform_maintenance(self) -> None:
        print("checking brakes... checking tire pressure...")
