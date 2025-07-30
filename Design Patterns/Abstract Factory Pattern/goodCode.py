from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Maruti(Vehicle):
    def start(self):
        print("Starting Maruti car...")

    def stop(self):
        print("Stopping Maruti car...")

class Toyota(Vehicle):
    def start(self):
        print("Starting Toyota car...")

    def stop(self):
        print("Stopping Toyota car...")




class VehicleFactory(ABC):
    @abstractmethod
    def create_vehicle(self):
        pass


class MarutiFactory(VehicleFactory):
    def create_vehicle(self):
        return Maruti()

class ToyotaFactory(VehicleFactory):
    def create_vehicle(self):
        return Toyota()



class FactoryProvider:
    def get_factory(brand: str):
        if brand == "maruti":
            return MarutiFactory()
        elif brand == "toyota":
            return ToyotaFactory()
        else:
            raise ValueError("Unknown brand")

def main():
    brand = "toyota"  # Change to "toyota" to test with Toyota factory

    factory = FactoryProvider.get_factory(brand)  # Factory Provider


    vehicle = factory.create_vehicle() # Product from brand-specific factory

    vehicle.start()
    vehicle.stop()

if __name__ == "__main__":
    main()




"""
Abstract Factory Pattern – Good Code Example

This code demonstrates the use of the Abstract Factory Pattern to create vehicles based on different brands (Maruti, Toyota).

Key Benefits:

1. Decouples Object Creation from Usage:
   - The main function does not depend on specific classes like Maruti or Toyota.
   - It only depends on the abstract Vehicle interface and factory abstraction.

2. Follows SOLID Principles:
   - Single Responsibility: Each factory is responsible only for creating one brand of vehicle.
   - Open/Closed: New brands can be added by creating new factory and vehicle classes without modifying existing code.

3. Clean Factory Selection:
   - A separate FactoryProvider handles the logic of selecting the appropriate factory based on the brand.

4. Easy to Extend:
   - To support a new brand (e.g., Ford), simply:
     - Create a new Ford class (implements Vehicle)
     - Create a FordFactory class (implements VehicleFactory)
     - Add a new condition to FactoryProvider

This pattern is ideal when multiple families (brands) produce objects that share the same interface but have different implementations.
"""





#If we want to extend the code to include specific models for Maruti, we can do so as follows:
# Assuming we have specific models for Maruti in a separate module called maruti_models.py
# maruti_models.py

# from maruti_models import Baleno, Swift
# from factory import VehicleFactory

class MarutiFactory(VehicleFactory):
    def __init__(self):
        self._models = {
            "hatchback": Baleno,
            "sedan": Swift,
        }

    def create(self, model_type: str):
        if model_type not in self._models:
            raise ValueError(f"Model type '{model_type}' not available in Maruti")
        return self._models[model_type]()


