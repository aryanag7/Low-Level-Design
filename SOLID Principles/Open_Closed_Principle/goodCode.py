from abc import ABC, abstractmethod

class BakeryItem(ABC):
    @abstractmethod
    def bake(self):
        pass

class Bread(BakeryItem):
    def bake(self):
        print("Baking bread.")

class Cake(BakeryItem):
    def bake(self):
        print("Baking cake.")

#manager
class Bakery:
    def bake_item(self, item: BakeryItem):
        item.bake()


bakery = Bakery()

bread = Bread()
cake = Cake()


bakery.bake_item(bread)
bakery.bake_item(cake)


"""
Open-Closed Principle (OCP): The Open-Closed Principle’s main idea is to minimize the frequency and impact of changes by promoting extensions instead of modifications, not to eliminate changes altogether.

Bad Code:
- Adding new functionality requires modifying existing code.
- Risky, can break existing functionality.

Good Code:
- Existing code remains unchanged (closed for modification).
- New functionality added through extension (open for extension).
- Safer, more maintainable, and flexible for growth.
"""

"""
Bakery class:

- Follows Open-Closed Principle.
- Accepts any BakeryItem (e.g., Bread, Cake, Pastry).
- Calls the bake() method without knowing the specific type.
- New items can be added by extending BakeryItem — no change needed in this class.
"""


"""
ABC and @abstractmethod (from abc module):

- ABC: Marks a class as an abstract base class.
- @abstractmethod: Forces child classes to implement the method.
- Prevents instantiation of incomplete classes.
- Useful for creating a common interface across related classes.
"""
