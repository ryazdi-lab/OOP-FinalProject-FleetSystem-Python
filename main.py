from models import Car, Motorcycle, Truck

def main():
    fleet = [
        Car("Toyota", "Camry", 2022, 50.0),
        Motorcycle("Honda", "CBR", 2021, 15.0),
        Truck("Volvo", "FH16", 2019, 20000)
    ]

    print("--- Fleet Management System ---")
    
    for vehicle in fleet:
        print(vehicle.get_description())
        
        if hasattr(vehicle, 'calculate_rental_cost'):
            cost = vehicle.calculate_rental_cost(3) 
            print(f"  > Rental cost for 3 units: ${cost}")
            
        if hasattr(vehicle, 'get_insurance_quote'):
            print(f"  > Insurance Quote: ${vehicle.get_insurance_quote()}")
        print("-" * 30)

if __name__ == "__main__":
    main()
