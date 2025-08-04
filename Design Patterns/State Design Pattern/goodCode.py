from abc import ABC, abstractmethod


class TrafficLightState(ABC):
    @abstractmethod
    def next_state(self, traffic_light):
        pass


class RedState(TrafficLightState):
    def next_state(self, traffic_light):
        self.perform_additional_action()  # Additional action for Red state
        traffic_light.set_state(GreenState())  # Transition to Green
    
    def perform_additional_action(self):
        # Example: Log the state or perform additional task
        print("Logging: The traffic light is Red.")

class GreenState(TrafficLightState):
    def next_state(self, traffic_light):
        self.display_timer()
        traffic_light.set_state(YellowState())  # Transition to Yellow

    def display_timer(self):
        # Example: Display a timer showing how long the light will stay green
        print("Green light timer: 30 seconds remaining.")

class YellowState(TrafficLightState):
    def next_state(self, traffic_light):
        self.play_warning_sound() 
        traffic_light.set_state(RedState()) # Transition to Red
    
    def play_warning_sound(self):
        # Example: Play a warning sound before turning red
        print("Warning: Yellow light. Be prepared to stop!")



class TrafficLight:
    def __init__(self):
        self.currState = RedState()  # Initially, the state is Red

    def change_state(self):
        # Delegate the state transition to the current state
        self.currState.next_state(self)  # Pass the TrafficLight object to the current state

    def set_state(self,state):
        self.currState = state

    def display_state(self):
        # Display the current state
        if isinstance(self.currState, RedState):
            print("Current state: Red")
        elif isinstance(self.currState, GreenState):
            print("Current state: Green")
        elif isinstance(self.currState, YellowState):
            print("Current state: Yellow")
# Client Code
light = TrafficLight()

# Display initial state (Red)
light.display_state()

# Change state and display (Red -> Green)
light.change_state()
light.display_state()

# Change state and display (Green -> Yellow)
light.change_state()
light.display_state()

# Change state and display (Yellow -> Red)
light.change_state()
light.display_state()


"""
Good Code (Using the State Pattern):
- The State Pattern allows the **TrafficLight** object to **delegate** the responsibility of state transitions to its **state objects** (e.g., `RedState`, `GreenState`, `YellowState`).
- Each **state** is encapsulated in its own class, and it knows how to **transition** to the next state, ensuring that each state handles its own behavior and transitions.
- By delegating the state transition logic to the **state objects**, the **TrafficLight** class remains **simple** and **decoupled** from the complexities of state transitions.
- The state transition is handled by **`self.state.change_state(self)`**, where the current state (like `RedState`) updates the state of the **TrafficLight** (e.g., changing from `RedState` to `GreenState`).
- This approach ensures that the code is **modular**, **scalable**, and **easily extendable**. Adding a new state (like `BlinkingState`) is simple and does not require modifying the core `TrafficLight` logic.
- The **State Pattern** **promotes clean code** by encapsulating state-specific behavior in state classes, making the system more flexible and easier to maintain.
"""



"""
Real Use Case Example (State Pattern) - Vending Machine:
- States:
  1. **Idle State**
  2. **Payment Pending State**
  3. **Item Dispensing State**
  4. **Out of Stock State**

Examples:
1. **Vending Machine** transitions from **Idle State** to **Payment Pending State** when the user selects an item and inserts money.
2. If the machine is **Out of Stock**, it transitions to **Out of Stock State**, preventing further selections.
"""
