# Завдання 4: Принцип інтерфейсу користувача (Interface Segregation Principle - ISP)

# Розробіть інтерфейс "Мережевий принтер" (NetworkPrinter), який включає методи для друку, сканування та копіювання. 
# Потім створіть два класи: 
# "Принтер" (Printer) та "Сканер" (Scanner), які реалізують цей інтерфейс та використовують лише ті методи, які їм потрібні. 
# Переконайтеся, що жоден з класів не має пустого методу.

from abc import ABC, abstractclassmethod

class ToPrint(ABC):
    """class ToPrint"""

    @abstractclassmethod
    def to_print(self):
        pass
class ToScan(ABC):
    """class ToScan"""

    @abstractclassmethod
    def to_scan(self):
        pass

class ToCopy(ABC):
    """class ToCopy"""

    @abstractclassmethod
    def to_copy(self):
        pass

class Printer(ToPrint):
    """class Printer"""

    def to_print(self):
        print("Printer is printing...")

class Scaner(ToScan):
    """class Scaner"""

    def to_scan(self):
        print("Scaner is scanning...")

class NetworkPrinter(ToPrint, ToScan):
    """class NetworkPrinter"""

    def to_print(self):
        print("NetworkPrinter is printing...")    
    
    def to_scan(self):
        print("NetworkPrinter is scanning...")

printer1 = Printer()
printer1.to_print()

scaner1 = Scaner()
scaner1.to_scan()

network_printer1 = NetworkPrinter()
network_printer1.to_print()
network_printer1.to_scan()