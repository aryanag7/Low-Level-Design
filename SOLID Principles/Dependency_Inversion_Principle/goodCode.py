from abc import ABC, abstractmethod

# abstraction
class Juicer(ABC):
    @abstractmethod
    def extract(self):
        pass


class OrangeJuicer(Juicer):
    def extract(self):
        return "orange juice"

class AppleJuicer(Juicer):
    def extract(self):
        return "apple juice"


class JuiceMachine:
    def __init__(self, juicer: Juicer):
        self.juicer = juicer  # depends on abstraction, not specific class

    def make_juice(self):
        return self.juicer.extract()


jm1 = JuiceMachine(OrangeJuicer())
print(jm1.make_juice())  # orange juice

jm2 = JuiceMachine(AppleJuicer())
print(jm2.make_juice())  # apple juice

"""
Term	Meaning
High-level class:- 	The one that performs the action (e.g., makes juice)
Low-level class:- 	The tool used to perform the action (e.g., OrangeJuicer)
Abstraction:- 	The interface that connects the high-level class to the tool
Details:- 	The inner working of the tool (low-level class implementation)




Good design: JuiceMachine depends on the Juicer interface, not on a specific tool.

The actual juicer (e.g., OrangeJuicer) is passed in from outside,
so the high-level logic is decoupled from low-level implementation.

This follows DIP and allows easy extension, testing, and swapping of tools.


"""