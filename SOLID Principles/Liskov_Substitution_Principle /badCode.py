from abc import ABC, abstractmethod

class BakeryItem(ABC):
    @abstractmethod
    def bake(self):
        pass


class Bread(BakeryItem):
    def bake(self):
        print("Baking bread at 180°C for 30 minutes.")

class Cake(BakeryItem):
    def bake(self):
        print("Baking cake at 160°C for 45 minutes.")

class FrozenItem(BakeryItem):
    def bake(self):
        raise NotImplementedError("Frozen items shouldn't be baked directly!")

"""
This child class breaks the promise of bake().
"""



#manager
class Bakery:
    def bake_item(self, item: BakeryItem):
        item.bake()


bakery = Bakery()

bread = Bread()
cake = Cake()
frozenitem = FrozenItem()


bakery.bake_item(bread)
bakery.bake_item(cake)

bakery.bake_item(frozenitem)
"""
It violates LSP: FrozenItem is not really a usable substitute for BakeryItem.
"""

"""
Liskov Substitution Principle Violation:

- BakeryItem is the parent class with a bake() contract.
- Bread and Cake are valid child classes — they implement bake() correctly.
- FrozenItem is a child but breaks the contract by raising an exception in bake().

Problem:
- bake_item(item: BakeryItem) expects any BakeryItem to be safely baked.
- Passing FrozenItem causes a runtime error.
- This violates LSP — child class (FrozenItem) is not a true substitute for the parent.

"""
