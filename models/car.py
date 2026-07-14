from models.vehicle_rentable_insurable import VehicleRentableInsurable


class Car(VehicleRentableInsurable):
    def perform_maintenance(self) -> None:
        print("changing engine oil... checking the headlights...")
