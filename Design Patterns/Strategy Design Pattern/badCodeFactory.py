class PaymentMethod:
    def process_payment(self, amount):
        pass

class CreditCardPayment(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing credit card payment of {amount}$")

class PayPalPayment(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of {amount}$")

class PaymentFactory:
    @staticmethod
    def get_payment_method(method) -> PaymentMethod:
        if method == "credit_card":
            return CreditCardPayment()
        elif method == "paypal":
            return PayPalPayment()
        else:
            raise ValueError("Invalid payment method")

# Client Code
payment_processor = PaymentFactory.get_payment_method("credit_card")
payment_processor.process_payment(100.0)

payment_processor = PaymentFactory.get_payment_method("paypal")
payment_processor.process_payment(50.0)


"""
Bad Code (With Factory Pattern):

The Factory Pattern creates a new object every time the payment method changes, which means that if we want to switch the payment method (e.g., from PayPal to Bitcoin), we are forced to create a new object each time.

This pattern leads to inefficiency because we are creating new objects instead of Dynamically swapping behavior.

The Factory pattern doesn’t allow us to easily change the behavior dynamically. You need to create a new object each time, which can be slow and resource-intensive if object creation is complex.

The Factory pattern is static in that it doesn't allow changing the strategy of an existing object—once the object is created, the behavior is fixed unless a new object is instantiated.

You can add a new set_payment method to dynamically change the method, but it will essentially be calling the get_payment to create a new object every time, which defeats the purpose of having a dynamic strategy.

def __init__(self):
        self.payment_method = None

def change_payment_method(self, method: str) -> PaymentMethod:
        # Dynamically change payment method
        return self.get_payment_method(method) 

Not flexible: You cannot easily swap out the payment method during runtime without creating a whole new object. If you already have an object, you are unable to modify its behavior without re-instantiating it.

You cann add a new set_payment method to dynamically change the method but it will essentially be calling the get_payment to create new object everytime.
"""