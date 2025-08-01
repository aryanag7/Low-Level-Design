class Robot:
    def __init__(self, name, color, battery_level):
        self.name = name
        self.color = color
        self.battery_level = battery_level

    def describe(self):
        return f"Robot {self.name} ({self.color}), Battery: {self.battery_level}%"

# Manually creating different robots
robot1 = Robot("Robot1", "Red", 100)
robot2 = Robot("Robot2", "Blue", 80)

print(robot1.describe())  # Robot Robot1 (Red), Battery: 100%
print(robot2.describe())  # Robot Robot2 (Blue), Battery: 80%





# -------------------- OR --------------------------------



#FACTORY DESIGN PATTERN EXAMPLE
# Step 1: Define the Robot class with attributes
class Robot:
    def __init__(self, name, color, task):
        self.name = name
        self.color = color
        self.task = task

    def describe(self):
        return f"{self.name} is a {self.color} robot assigned to {self.task}."

# Step 2: Robot Factory to create new robot instances
class RobotFactory:
    def create_robot(self, name, color, task):
        # Create a new Robot with the provided configurations
        return Robot(name, color, task)

# Step 3: Usage
robot_factory = RobotFactory()

# Creating robots with different tasks using the factory
robot1 = robot_factory.create_robot("Robot1", "Red", "cleaning")
robot2 = robot_factory.create_robot("Robot2", "Blue", "cooking")
robot3 = robot_factory.create_robot("Robot3", "Green", "assembly")

# Describing the robots
print(robot1.describe())  # Robot1 is a Red robot assigned to cleaning.
print(robot2.describe())  # Robot2 is a Blue robot assigned to cooking.
print(robot3.describe())  # Robot3 is a Green robot assigned to assembly.


# This code does not utilize the Prototype Design Pattern, leading to code duplication.



"""
Bad Code (Without Prototype Pattern):
- In this example, we are manually creating each new Robot instance by specifying all its attributes (e.g., name, color, battery level).
- This approach is inefficient, especially when object creation is complex and requires a lot of steps or resources.
- Every time we create a new robot, we must manually initialize it from scratch, which is repetitive and leads to unnecessary resource usage.
- Additionally, if robots share similar configurations, we are repeating the same initialization process multiple times, which is not optimal.

"""