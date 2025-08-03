class OrangeJuicer:
    def extract(self):
        return "orange juice"

class JuiceMachine:  # High-level class
    def make_juice(self):
        juicer = OrangeJuicer()  # ❌ Fused to the tool (OrangeJuicer)
        return juicer.extract()


"""
In bad design, JuiceMachine creates and depends directly on OrangeJuicer.
This fuses high-level logic to a specific low-level tool, violating DIP.

With Dependency Inversion, JuiceMachine depends only on a Juicer interface.
The actual tool (e.g., OrangeJuicer, AppleJuicer) is injected from outside.

This makes the system flexible, testable, and loosely coupled.

To test the above code, we need to ovverride the OrangeJuicer with a mock or a different implementation at runtime.
import your_module

original = your_module.OrangeJuicer

class FakeJuicer:
    def extract(self):
        return "fake juice"

your_module.OrangeJuicer = FakeJuicer  # override
jm = your_module.JuiceMachine()
assert jm.make_juice() == "fake juice"
your_module.OrangeJuicer = original 
"""
