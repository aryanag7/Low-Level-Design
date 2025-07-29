from abc import ABC, abstractmethod

# Vehicle - Common interface
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass



# Car - Concrete class
class Car(Vehicle):
    def start(self):
        print("Car is starting...")

    def stop(self):
        print("Car is stopping...")


# Truck - Concrete class
class Truck(Vehicle):
    def start(self):
        print("Truck is starting...")

    def stop(self):
        print("Truck is stopping...")



# client code
def main():
    vehicle_type = "car"  # or "truck"

    if vehicle_type == "car":
        vehicle = Car()   # directly creates a Car
    elif vehicle_type == "truck":
        vehicle = Truck() # directly creates a Truck
    else:
        raise ValueError("Invalid vehicle type")

    vehicle.start()
    vehicle.stop()

if __name__ == "__main__":
    main()


"""
 Issues in this code (before using Factory Pattern):

1. Tight Coupling:
   - The client code directly depends on specific classes like Car and Truck.
   - Any change in these classes requires changes in the client code.

2. Violates Open/Closed Principle:
   - Adding a new vehicle (e.g., Bike) requires modifying the main logic.
   - Code is not closed for modification.

3. Object Creation Logic is Repeated:
   - Same 'if-elif' blocks are needed everywhere an object is created.
   - If creation becomes complex (e.g., requires extra setup), every place must be updated.

4. Hard to Test:
   - No abstraction/interface used — cannot mock or swap implementations easily.

5. Poor Scalability:
   - Each new type increases complexity in the main code.
   - Makes the code harder to maintain and error-prone.
"""
