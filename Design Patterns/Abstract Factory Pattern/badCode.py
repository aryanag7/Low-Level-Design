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
This is a simple factory pattern:
- It centralizes object creation for different vehicle types (Car, Truck).
- The client code doesn’t need to know about concrete classes.

 But it has limitations when scaling:
- If we add different **brands** (e.g., MarutiCar, ToyotaTruck), each with its own creation logic,
  the 'if-elif' chain in this factory will grow longer and harder to manage.
- We’d be forced to write something like:

    if brand == "maruti" and type == "car":
        return MarutiCar()
    elif brand == "toyota" and type == "truck":
        return ToyotaTruck()
    ...

- This mixes **multiple families** of logic in a single factory,
  violating the Single Responsibility and Open/Closed Principles.

In such cases, it's better to upgrade to an Abstract Factory:
- Each brand (MarutiFactory, ToyotaFactory) has its own way of creating vehicles.
- The main code asks the right factory for a vehicle, without worrying about internal creation details.
"""
