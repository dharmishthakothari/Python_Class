from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def greet(self):
        print("in A->greet")
class B(A):
    def greet(self):
        print("Good Morning")
obj=B()
obj.greet()

