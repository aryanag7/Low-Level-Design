def process_payment(payment_method, amount):
    if payment_method == "credit_card":
        print(f"Processing credit card payment of {amount}$")
    elif payment_method == "paypal":
        print(f"Processing PayPal payment of {amount}$")
    elif payment_method == "bitcoin":
        print(f"Processing Bitcoin payment of {amount} BTC")
    else:
        raise ValueError("Invalid payment method")

# Client Code
process_payment("credit_card", 100.0)
process_payment("paypal", 50.0)

"""
Bad Code (With if-else):

The if-else approach is static and inflexible because each time we need to add a new payment method, we must modify the process_payment function.

This can quickly lead to a large and hard-to-maintain function as new methods are added.

It is difficult to extend: If you want to introduce a new payment method (e.g., Bitcoin), you need to change the existing code, violating the Open/Closed Principle.

This approach is not scalable: As the number of payment methods grows, the complexity of the code increases. The function becomes harder to debug and test.

Not dynamic: You cannot change the payment method dynamically at runtime. Each change requires modifying the function and rerunning the process.
"""