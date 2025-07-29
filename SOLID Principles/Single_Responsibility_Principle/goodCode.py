class Baker:
    def bake_bread(self, bread_type):
        print(f"Baking {bread_type} bread.")

class InventoryManager:
    def manage_inventory(self):
        print("Managing inventory.")

class SupplyManager:
    def order_supplies(self):
        print("Ordering baking supplies.")

class CustomerServiceRep:
    def handle_customer_service(self, customer_issue):
        print(f"Handling customer issue: {customer_issue}")

class Cleaner:
    def clean_store(self):
        print("Cleaning the bakery.")


# Create objects for each class
baker = Baker()
inventory_manager = InventoryManager()
supply_manager = SupplyManager()
customer_service_rep = CustomerServiceRep()
cleaner = Cleaner()

# Call methods on each object as required
baker.bake_bread("sourdough")
inventory_manager.manage_inventory()
supply_manager.order_supplies()
customer_service_rep.handle_customer_service("Order delayed")
cleaner.clean_store()


"""
Single Responsibility Principle (SRP):

Bad Code:
- One class handles multiple unrelated tasks.
- Modifying one task risks breaking others.
- Difficult to test and maintain.
- complex to understand if things are complex in each responsibility.

Good Code:
- Each class has a single clear responsibility.
- Easy to test, modify, and extend independently.
- Reduces bugs and improves code clarity.
- easier to understand different responsibility.
"""

