class InsufficentBalance(Exception):
    pass
class Bank:
    def __init__(self,balance):
        self.__balance=balance
    
    def deposite(self,amount):
        self.__balance+=amount
    
    def getBalance(self):
        return self.__balance
    
obj1=Bank(10000)
print(f"Initial balance is {obj1.getBalance()}")
obj1.deposite(2000)
print(f"After deposit {obj1.getBalance()}")


