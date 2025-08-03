from abc import ABC,abstractmethod
import copy

# Prototype interface
@abstractmethod
class Prototype(ABC):
    def clone(self):
        pass

# Robot class implementing the Prototype pattern
class Robot(Prototype):
    def __init__(self, name, color, battery_level):
        self.name = name
        self.color = color
        self.battery_level = battery_level

    def clone(self):
        # Return a deep copy of the current object (the prototype)
        return copy.deepcopy(self)

    def describe(self):
        return f"Robot {self.name} ({self.color}), Battery: {self.battery_level}%"

# Create the prototype (template) robot
prototype_robot = Robot("Prototype", "Red", 100)

# Cloning the prototype to create new robots
robot1 = prototype_robot.clone()
robot2 = prototype_robot.clone()

# Customize the clones
robot1.name = "Robot1"
robot1.battery_level = 90
robot2.name = "Robot2"
robot2.battery_level = 80

print(robot1.describe())  # Robot Robot1 (Red), Battery: 90%
print(robot2.describe())  # Robot Robot2 (Red), Battery: 80%


"""
Good Code (With Prototype Pattern):
- The Prototype pattern solves the problem by allowing us to create new objects by **cloning** an existing object (the prototype).
- In this case, we create a single **prototype robot**, which serves as a template for all other robots.
- Instead of manually creating new robots from scratch, we **clone** the prototype and then **customize** the cloned robots (e.g., changing the name, color, or battery level).
- This approach is more efficient because we avoid redundant initialization steps and use the prototype to quickly create similar objects.
- The cloned objects are **independent** of the prototype, so changes to one robot do not affect the others.

"""

"""
Object creation can be considered expensive or difficult when:
1. It involves resource-intensive tasks, like loading large datasets, performing complex computations, or making network/database requests.
2. It requires **3D object creation**, such as loading textures, vertices, or other graphical resources in a graphics engine.
3. Repeating this process for each new object is inefficient and wasteful.

The Prototype pattern helps by allowing objects to be cloned from an existing prototype, skipping expensive or complex initialization steps and enabling faster and more efficient object creation.
"""
