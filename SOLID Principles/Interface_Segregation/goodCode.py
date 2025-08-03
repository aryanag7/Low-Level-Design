from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print(self): pass

class Scanner(ABC):
    @abstractmethod
    def scan(self): pass

class FaxMachine(ABC):
    @abstractmethod
    def fax(self): pass



class BasicPrinter(Printer):
    def print(self):
        print("Printing only.")

    #In this context, a client just means the code (or class) that uses another class or interface. (consumer in this case)
    
    #client here BasicPrinter not forced to implement things that it doesnt require or depend upon



class MultiFunctionPrinter(Printer, Scanner, FaxMachine):
    def print(self):
        print("Printing...")

    def scan(self):
        print("Scanning...")

    def fax(self):
        print("Faxing...")


basic = BasicPrinter()
basic.print()

pro = MultiFunctionPrinter()
pro.print()
pro.scan()
pro.fax()
