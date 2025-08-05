class SmartHomeController:
    def turn_on_device(self, device_type):
        if device_type == "AirConditioner":
            print("Sending Bluetooth command to turn on AC")
            # Bluetooth logic here
        elif device_type == "SmartLight":
            print("Sending Wi-Fi command to turn on Light")
            # Wi-Fi logic here
        elif device_type == "CoffeeMachine":
            print("Sending Zigbee signal to turn on Coffee Machine")
            # Zigbee protocol here
        elif device_type == "SecurityCamera":
            print("Calling custom API to activate Security Camera")
            # Custom HTTP API call

# ------------------------ OR ---------------------------------------

# Legacy or vendor-provided classes
class BluetoothAirConditioner:
    def bluetooth_power_on(self):
        print("AC is now ON via Bluetooth")

    def bluetooth_power_off(self):
        print("AC is now OFF via Bluetooth")

class ZigbeeCoffeeMachine:
    def zigbee_on(self):
        print("Coffee Machine ON via Zigbee")

    def zigbee_off(self):
        print("Coffee Machine OFF via Zigbee")


class SmartHomeController:
    def __init__(self):
        self.ac = BluetoothAirConditioner()
        self.coffee = ZigbeeCoffeeMachine()

    def turn_on_all_devices(self):
        self.ac.bluetooth_power_on()
        self.coffee.zigbee_on()

    def turn_off_all_devices(self):
        self.ac.bluetooth_power_off()
        self.coffee.zigbee_off()


"""
❌ Issues in this approach (even with classes):

1. Controller must know the internal methods of each device (like `bluetooth_power_on`, `zigbee_on`).
2. Code is tightly coupled — can't swap a Zigbee Coffee Machine for a Wi-Fi one without rewriting controller logic.
3. Adding a new device = adding new properties and method calls to the controller.
4. Violates SRP (controller handles device-specific logic) and OCP (not closed to modification).
5. No abstraction or flexibility — all devices have different method names and structures.
"""
