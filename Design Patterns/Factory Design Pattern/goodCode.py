from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass



class Car(Vehicle):
    def start(self):
        print("Car is starting...")

    def stop(self):
        print("Car is stopping...")


class Truck(Vehicle):
    def start(self):
        print("Truck is starting...")

    def stop(self):
        print("Truck is stopping...")





class VehicleFactory:
    def get_vehicle(self, vehicle_type):
        if vehicle_type == "car":
            return Car()
        elif vehicle_type == "truck":
            return Truck()
        else:
            raise ValueError("Unknown vehicle type")
        




def main():
    factory = VehicleFactory()

    vehicle_type = "car"  # This can be dynamically set
    vehicle = factory.get_vehicle(vehicle_type)  # No direct class creation

    vehicle.start()
    vehicle.stop()

if __name__ == "__main__":
    main()



"""
 Benefits of Using Factory Pattern in This Vehicle Example:

1. Decouples Client from Specific Classes:
   - main() no longer needs to know about Car or Truck classes directly.
   - It only interacts with the factory and the Vehicle interface.

2. Centralizes Object Creation:
   - All object creation logic is moved to VehicleFactory.
   - If creation becomes complex later, only the factory needs to be updated.

3. Follows Open/Closed Principle:
   - To add a new vehicle (e.g., Bike), you just update the factory.
   - main() or client code stays untouched.

4. Improves Code Readability and Organization:
   - Client logic is cleaner and focuses only on behavior (start/stop).
   - Factory handles type decisions and object instantiation.

5. Enhances Maintainability:
   - Reduces duplication of creation logic across the codebase.
   - Changes are localized, making the codebase easier to manage.
"""
