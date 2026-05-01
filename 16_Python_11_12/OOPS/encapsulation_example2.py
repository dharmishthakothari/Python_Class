class Bank:
    def __init__(self,name,balance):
        self.__balance=balance
        self.name=name
    def deposite(self,amount):
        self.__balance+=amount
    def withdrow(self,amount):
        self.__balance-=amount
    def getBalance(self):
        return self.__balance
b1=Bank('Dharmishtha',20000)
b1.deposite(2000)
print(b1.getBalance())