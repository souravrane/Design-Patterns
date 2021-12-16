# A better idea would be to granularize these interfaces to support multifunctionality
# Making an interface that feature too many elements is not a good idea
from abc import abstractmethod


class Machine:
    def print(self, document):
        raise NotImplementedError

    def fax(self, document):
        raise NotImplementedError

    def scan(self, document):
        raise NotImplementedError


class MultiFunctionPrinter(Machine):
    # all these 3 functionalities will work as its a new printer
    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass


class OldFashionedPrinter(Machine):
    def print(self, document):
        pass

    # Operation not supported for old printers
    def fax(self, document):
        raise NotImplementedError

    # Operation not supported for old printers
    def scan(self, document):
        pass


# Following ISP
class Printer:
    @abstractmethod
    def print(self, document):
        pass


class Scanner:
    @abstractmethod
    def scan(self, document):
        pass


class MultiFunctionDevice(Printer, Scanner):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        passd


class MultiFunctionMachine(MultiFunctionDevice):
    def print(self, document):
        pass

    def scan(self, document):
        pass
