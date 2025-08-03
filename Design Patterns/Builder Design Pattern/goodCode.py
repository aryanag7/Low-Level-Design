class Car:
    def __init__(self, brand=None, model=None, color=None, engine=None, sunroof=False):
        self.brand = brand
        self.model = model
        self.color = color
        self.engine = engine
        self.sunroof = sunroof

    def display(self):
        print(f"{self.color} {self.brand} {self.model} with {self.engine} engine "
              f"{'with sunroof' if self.sunroof else 'no sunroof'}")




"""
self refers to the current builder instance,
and self.car is the actual Car object that the builder is building step by step.

"""

class CarBuilder:
    def __init__(self):
        self.car = Car() #self.car is an instance of Car that will be built step by step by this self builder instance

    def set_brand(self, brand):
        self.car.brand = brand
        return self #returns builder instance for method chaining

    def set_model(self, model):
        self.car.model = model
        return self

    def set_color(self, color):
        self.car.color = color
        return self

    def set_engine(self, engine):
        self.car.engine = engine
        return self

    def set_sunroof(self, has_sunroof):
        self.car.sunroof = has_sunroof
        return self

    def build(self):
        return self.car

    def reset(self):
        self.car = Car()
        return self


def main():
    car1 = (
        CarBuilder()
        .set_brand("Toyota")
        .set_model("Camry")
        .set_color("Red")
        .set_engine("Hybrid")
        .set_sunroof(True)
        .build()
    )

    """
    Alternatively you can also do,  car = CarBuilder()\
    .set_brand("Toyota")\
    .set_model("Camry")\
    .build()
    """
  
    car2 = (
        CarBuilder()
        .set_brand("Maruti")
        .set_model("Swift")
        .set_color("Blue")
        .set_engine("Petrol")
        .set_sunroof(False)
        .build()
    )

    car1.display()
    car2.display()



if __name__ == "__main__":
    main()  




"""
Note:
Reusing the same CarBuilder instance means you're modifying
the same Car object (self.car) each time.

So if you build multiple cars using the same builder,
they will all point to the same object and reflect the latest changes.

To create different cars, use a new CarBuilder()
or reset the builder to start fresh.

Meal Order Example: 
Selecting a meal with multiple options that you can customize step by step. 
Burger with different toppings, sides, and drinks.
"""

"""
Builder Pattern Use Cases:

1. Creating a complex Car object:
  HttpRequestBuilder()
  .set_method("POST")
  .set_url("https://api.example.com/user")
  .set_headers({"Authorization": "Bearer xyz"})
  .set_body({"name": "Aryan"})
  .build()

2. Building an Email message:
   EmailBuilder()
     .set_to("aryan@example.com")
     .set_subject("Builder Pattern Example")
     .set_body("Hi Aryan, here's your summary.")

3. Constructing a SQL query:
   SqlQueryBuilder()
     .select("name, age")
     .from_table("users")
     .where("age > 18")
"""
