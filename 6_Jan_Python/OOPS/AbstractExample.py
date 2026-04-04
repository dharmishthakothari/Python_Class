from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def greet(self):
        return None
    def greet1(self):
        print("in non abstract method")

class B(A):
    def greet(self):
        print("Happy weekend")
objB=B()
objB.greet()