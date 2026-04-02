class A:
    def greet(self):
        print("Good Morning ")
    def display(self):
        print("In display A")
class B(A):
    pass

objB=B()
objB.greet()
objB.display()

objA=A()
objA.greet()