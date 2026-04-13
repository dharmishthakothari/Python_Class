from abc import ABC,abstractmethod
class Bank(ABC):
    @abstractmethod
    def getInterestRate(self):
        return 0.0
    def greet(self):
        print("Welcome to Bank")
class SBI(Bank):
    def getInterestRate(self):
        return 7.2
class Axis(Bank):
    def getInterestRate(self):
        return 6.5
obj=SBI()
print("SBI ",obj.getInterestRate())
obj1=Axis()
print("Axis ",obj1.getInterestRate())