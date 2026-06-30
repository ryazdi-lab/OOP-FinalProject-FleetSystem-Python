"""
Main entry point for Fleet Management System.
Demonstrates polymorphism without using isinstance() or type().
"""
from models import Car, Motorcycle, Truck


def display_vehicle_operations(vehicle) -> None:
    """
    Display all operations for a single vehicle.
    Uses hasattr() to check capabilities (polymorphism).
    """
    print(f"\n{'='*60}")
    print(f"📋 Vehicle: {vehicle.get_info()}")
    print(f"{'='*60}")
    
    # Basic vehicle operations (always available)
    print(f"▶️  {vehicle.start_engine()}")
    print(f"⛽ Fuel Efficiency: {vehicle.calculate_fuel_efficiency():.2f} km/liter")
    
    # Rental operations (if vehicle is rentable)
    if hasattr(vehicle, 'is_available'):
        print(f"\n💰 RENTAL INFORMATION:")
        print(f"   Available: {'✅ Yes' if vehicle.is_available() else '❌ No'}")
        
        if vehicle.is_available():
            try:
                # Test different rental durations
                for days in [1, 3, 7]:
                    cost = vehicle.rent(days)
                    print(f"   Rent for {days} day(s): ${cost:.2f}")
                
                # Return the vehicle (assuming we rented for 1 day)
                print(f"   {vehicle.return_vehicle()}")
                
            except ValueError as e:
                print(f"   ⚠️ Rental error: {e}")
    
    # Insurance operations (if vehicle is insurable)
    if hasattr(vehicle, 'calculate_insurance'):
        print(f"\n🛡️ INSURANCE INFORMATION:")
        print(f"   Premium: ${vehicle.calculate_insurance():.2f}")
        
        if hasattr(vehicle, 'get_insurance_details'):
            details = vehicle.get_insurance_details()
            for key, value in details.items():
                print(f"   {key.replace('_', ' ').title()}: {value}")
    
    # Stop engine
    print(f"\n🛑 {vehicle.stop_engine()}")


def main():
    """
    Main function demonstrating polymorphism.
    """
    print("\n" + "="*60)
    print("🚗 WELCOME TO FLEET MANAGEMENT SYSTEM 🚚")
    print("="*60)
    print("\n📌 Demonstrating Polymorphism (NO isinstance/type used)")
    
    # Create a list of different vehicles
    # All are subclasses of Vehicle, so polymorphism works
    fleet = [
        Car("Toyota", "Camry", 2022, 55.0, 320.0, 4, "Gasoline"),
        Car("BMW", "M2", 2024, 120.0, 450.0, 2, "Premium Gasoline"),
        Motorcycle("Yamaha", "MT-07", 2023, 45.0, 180.0, 689),
        Motorcycle("Honda", "Grom", 2025, 25.0, 100.0, 125),
        Truck("Volvo", "FH16", 2020, 180.0, 25000.0, 3),
        Truck("Mercedes", "Actros", 2021, 200.0, 32000.0, 4)
    ]
    
    # Process each vehicle polymorphically
    for vehicle in fleet:
        display_vehicle_operations(vehicle)
    
    # Demonstrate fleet statistics
    print(f"\n{'='*60}")
    print("📊 FLEET STATISTICS")
    print(f"{'='*60}")
    
    # Count available vehicles (using polymorphism)
    available_count = sum(1 for v in fleet if hasattr(v, 'is_available') and v.is_available())
    total_vehicles = len(fleet)
    
    print(f"Total Vehicles: {total_vehicles}")
    print(f"Available Vehicles: {available_count}")
    
    # Average fuel efficiency across all vehicles
    avg_efficiency = sum(v.calculate_fuel_efficiency() for v in fleet) / total_vehicles
    print(f"Average Fleet Fuel Efficiency: {avg_efficiency:.2f} km/liter")
    
    # Total potential rental income (if all rented for 1 day)
    total_rental_income = sum(
        v.daily_rental_price for v in fleet if hasattr(v, 'daily_rental_price')
    )
    print(f"Potential Daily Rental Income: ${total_rental_income:.2f}")
    
    print("\n✅ Demonstration complete. No isinstance() or type() used!")
    print("   All operations used polymorphism via hasattr() and common interfaces.\n")


if __name__ == "__main__":
    main()