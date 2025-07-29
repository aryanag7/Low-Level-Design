from abc import ABC, abstractmethod

class OfficeMachine(ABC):
    @abstractmethod
    def print(self): pass

    @abstractmethod
    def scan(self): pass

    @abstractmethod
    def fax(self): pass



class BasicPrinter(OfficeMachine):
    def print(self):
        print("Printing document.")

    def scan(self):
        raise NotImplementedError("BasicPrinter can't scan.")

    def fax(self):
        raise NotImplementedError("BasicPrinter can't fax.")


'''
BasicPrinter is forced to implement methods it doesn’t need.

Any user of OfficeMachine now thinks all devices can scan and fax, which is misleading.

'''
