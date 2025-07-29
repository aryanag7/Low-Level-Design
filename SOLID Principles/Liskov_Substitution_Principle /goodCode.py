from abc import ABC, abstractmethod

# Parent class for items that can be baked
class BakeryItem(ABC):
    @abstractmethod
    def bake(self):
        pass

# Parent class for items that can be frozen (different responsibility)
class FreezableItem(ABC):
    @abstractmethod
    def freeze(self):
        pass


# Valid bakery items
class Bread(BakeryItem):
    def bake(self):
        print("Baking bread at 180°C for 30 minutes.")

class Cake(BakeryItem):
    def bake(self):
        print("Baking cake at 160°C for 45 minutes.")


# Frozen item implements FreezableItem instead of BakeryItem
class FrozenPizza(FreezableItem):
    def freeze(self):
        print("Freezing pizza at -18°C.")




class Bakery:
    def bake_item(self, item: BakeryItem):
        item.bake()

class Freezer:
    def freeze_item(self, item: FreezableItem):
        item.freeze()



# Create items
bread = Bread()
cake = Cake()
pizza = FrozenPizza()

# Create managers
bakery = Bakery()
freezer = Freezer()

# Bake bakery items
bakery.bake_item(bread)
bakery.bake_item(cake)

# Freeze frozen items
freezer.freeze_item(pizza)


"""
Good Code – Follows Liskov Substitution Principle:

- BakeryItem: for items that can be baked (Bread, Cake).
- FreezableItem: separate interface for frozen items (e.g., FrozenPizza).
- Bakery manager only handles BakeryItems.
- Freezer manager handles FreezableItems.
- Each child class behaves consistently with its parent contract.
- No runtime errors; safe substitution ensured.
"""
