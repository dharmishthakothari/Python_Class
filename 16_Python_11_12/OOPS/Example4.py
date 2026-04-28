class A:
    def greet(self):
        print("Hello")
class B(A):
    def goodBye(self):
        print("Good Bye ")
objB=B()

objB.greet()
objB.goodBye()