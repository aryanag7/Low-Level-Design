class Car:
    def __init__(self, brand, model, color, engine, sunroof):
        self.brand = brand
        self.model = model
        self.color = color
        self.engine = engine
        self.sunroof = sunroof

    def display(self):
        print(f"{self.color} {self.brand} {self.model} with {self.engine} engine "
              f"{'with sunroof' if self.sunroof else 'no sunroof'}")



car1 = Car("Toyota", "Camry", "Red", "Hybrid", True)
car2 = Car("Toyota", "Camry", "Red", "Hybrid", False)


car1.display()
car2.display()


"""
Without Builder Pattern:

1. Too many constructor arguments — order matters and is error-prone. (need to pass all parameters in the correct order as well as remember what each parameter means)

2. Hard to understand which value corresponds to which field when reading the code.

3. Can't easily skip optional fields without creating multiple overloaded constructors.

4. Code becomes difficult to maintain and extend as object complexity grows.





"""

