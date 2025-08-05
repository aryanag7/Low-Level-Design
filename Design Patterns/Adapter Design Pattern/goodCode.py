# Target Interface
class SmartDevice:
    def turn_on(self):
        pass

    def turn_off(self):
        pass


#  Existing / Legacy / Third-party Devices (Adaptees)
# Adaptee 1: Bluetooth AC
class BluetoothAirConditioner:
    def bluetooth_power_on(self):
        print("AC powered ON via Bluetooth")

    def bluetooth_power_off(self):
        print("AC powered OFF via Bluetooth")

# Adaptee 2: Zigbee Coffee Machine
class ZigbeeCoffeeMachine:
    def zigbee_on(self):
        print("Coffee Machine ON via Zigbee")

    def zigbee_off(self):
        print("Coffee Machine OFF via Zigbee")



# Adapter for Bluetooth AC
class AirConditionerAdapter(SmartDevice):
    def __init__(self, device: BluetoothAirConditioner):
        self.device = device

    def turn_on(self):
        self.device.bluetooth_power_on()

    def turn_off(self):
        self.device.bluetooth_power_off()


# Adapter for Zigbee Coffee Machine
class CoffeeMachineAdapter(SmartDevice):
    def __init__(self, device: ZigbeeCoffeeMachine):
        self.device = device

    def turn_on(self):
        self.device.zigbee_on()

    def turn_off(self):
        self.device.zigbee_off()



class SmartHomeController:
    def __init__(self):
        self.devices = []

    def add_device(self, device: SmartDevice):
        self.devices.append(device)

    def activate_all(self):
        for device in self.devices:
            device.turn_on()

    def deactivate_all(self):
        for device in self.devices:
            device.turn_off()

if __name__ == "__main__":
    # Real devices (incompatible interfaces)
    ac = BluetoothAirConditioner()
    coffee = ZigbeeCoffeeMachine()

    # Wrap them using adapters
    ac_adapter = AirConditionerAdapter(ac)
    coffee_adapter = CoffeeMachineAdapter(coffee)

    # Use them through common interface
    controller = SmartHomeController()
    controller.add_device(ac_adapter)
    controller.add_device(coffee_adapter)

    controller.activate_all()
    controller.deactivate_all()


"""
Adapter Pattern — When and Why We Use It
We use the Adapter Pattern when we want to reuse existing code (like 3rd-party, legacy, or vendor-specific classes) in our new system, but their interfaces don't match what we expect.

Instead of modifying that old code (which might not even be possible), we wrap it inside an adapter class that converts its interface into the one our system understands.

What does "3rd-party, legacy, vendor-specific" mean?
3rd-party = Code/libraries written by someone else (like Google, AWS, etc.)

Legacy = Old code written a long time ago, often using outdated patterns

Vendor-specific = Code from a device manufacturer or company, often using their own unique method names or protocols




Adapter Pattern Used Here:

1. Provides a unified interface (`SmartDevice`) for all smart devices regardless of protocol.
2. Each device has its own Adapter class that translates its method names into standard ones.
3. Controller only depends on the SmartDevice interface — not on how individual devices work.
4. Makes it easy to add new devices or change protocols without touching controller logic.
5. Follows SO

"""

"""
 Adapter Pattern Use Case: Payment Gateway Integration

Problem:
- Our app expects a common method `process(amount)` to handle payments.
- But different payment providers (Stripe, PayPal, Razorpay) have different method names and interfaces.

Solution:
- Define a common interface `IPaymentProcessor` with `process(amount)`.
- Create an Adapter for each payment gateway to map its specific method to our standard one.

Benefit:
- Our app can switch or add payment providers easily without changing core payment logic.
"""