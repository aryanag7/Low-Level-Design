class TrafficLight:
    def __init__(self):
        self.state = "red"  # Initial state is red

    def change_state(self):
        if self.state == "red":
            self.state = "green"  # Red to Green
        elif self.state == "green":
            self.state = "yellow"  # Green to Yellow
        elif self.state == "yellow":
            self.state = "red"  # Yellow to Red
        else:
            print("Invalid state")
        
        print(f"The traffic light is now {self.state}")

# Client code
light = TrafficLight()

# Simulate changing the state of the traffic light
light.change_state()  # Red -> Green
light.change_state()  # Green -> Yellow
light.change_state()  # Yellow -> Red


"""
State Pattern - Issues in Traditional Approach:
- **Increased Complexity with Multiple States**: In the traditional approach
managing multiple states using **if-else** or **switch** statements becomes cumbersome as the number of states grows. Each state introduces **additional conditionals** that must be checked and handled explicitly.
- **Hard to Manage State Transitions**: Handling **state transitions** directly within the object can lead to complex logic. The object needs to manage not only its current state but also the logic to transition between states, making the code harder to maintain and extend.
- **Violation of Open/Closed Principle**: The object must be modified every time a new state is added. This leads to **tight coupling** between the object and its states, as the behavior and transitions need to be explicitly handled within the object.
- **Difficulty in Extending**: Adding new states or changing the behavior for existing states requires modifying the core object, which can introduce bugs and complicate testing. With more states, the code becomes **less maintainable** and **more prone to errors**.
"""