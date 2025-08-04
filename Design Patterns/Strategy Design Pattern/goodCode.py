from abc import ABC, abstractmethod

# Strategy Interface
class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

# Concrete Strategy 1: Credit Card Payment
class CreditCardPayment(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing credit card payment of {amount}$")

# Concrete Strategy 2: PayPal Payment
class PayPalPayment(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of {amount}$")

# The Context Class
class PaymentProcessor:
    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method  # Initial strategy
    
    def set_payment_method(self, payment_method: PaymentMethod):
        self.payment_method = payment_method  # Change behavior dynamically
    
    def execute_payment(self, amount):
        self.payment_method.process_payment(amount)  # Use the current strategy

# Client Code
amount = 100.0

# Initially using Credit Card
processor = PaymentProcessor(CreditCardPayment())
processor.execute_payment(amount)

# Dynamically change to PayPal
processor.set_payment_method(PayPalPayment())
processor.execute_payment(amount)

"""
The context object (PaymentProcessor) interacts with the strategy object (CreditCardPayment, PayPalPayment) to perform the task (payment processing).

The context doesn't create new objects for every strategy, but it interacts with different strategies by calling the process_payment() method.

Even though the context object (PaymentProcessor) is the same, it communicates with different objects (strategies) to execute different behaviors.
"""


"""
Good Code (With Strategy Pattern):

The Strategy Pattern solves the problem by dynamically changing the payment behavior of an existing object without having to create new ones.

Instead of creating a new object each time a payment method changes, we swap the strategy (payment method) inside the same object.

This approach allows for dynamic behavior: We can change the payment method at runtime by calling the set_payment_method() method.

The PaymentProcessor object itself remains the same, but the behavior changes based on the strategy we pass to it.

The Strategy Pattern promotes flexibility and scalability: Adding a new payment method requires only creating a new strategy class (like BitcoinPayment), without modifying existing code.

This is more efficient than creating new objects every time and provides a much cleaner, maintainable code structure. The system can easily be extended with new strategies without changing the existing client code.
"""


"""
USE CASE:- Tax Calculation Strategy:
- Uses the Strategy Pattern to dynamically calculate taxes based on country, state, product type, and customer type.
- Each tax rule (e.g., USA, Canada, GST) is encapsulated in its own strategy, making the system flexible and maintainable.
- The order class can easily swap tax strategies at runtime, allowing for dynamic and context-specific tax calculations.
- Adding new tax strategies (e.g., for different countries or product types) is simple without modifying existing code.

- Sorting Strategy:
- Uses the Strategy Pattern to sort a list of items based on different criteria (e.g., by price, by rating).
- Each sorting strategy (e.g., PriceSortStrategy, RatingSortStrategy) implements a common interface, allowing the context (e.g., ItemList) to use any sorting strategy dynamically.
- The context can easily switch between sorting strategies at runtime, providing flexibility in how items are sorted.
- Adding new sorting strategies (e.g., by name, by date) is straightforward without altering existing code.
"""
