from abc import ABC,abstractmethod

class Bank(ABC):
    @abstractmethod
    def getRateofInterest(self):
        return 0.0

class SBI(Bank):
    # def getRateofInterest(self):
    #     return 0.5
    pass
class ICICI(Bank):
    def getRateofInterest(self):
        return 0.35

ic=ICICI()
print("ICICI Interest ",ic.getRateofInterest())
sbi=SBI()
print("SBI ",sbi.getRateofInterest())