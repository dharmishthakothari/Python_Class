from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def greet(self):
        pass
    def goodBye(self):
        print("Good Bye ")
class B(A):
    
    def greet(self):
        print("Good Morning ")
b=B()
b.greet()
