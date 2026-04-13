class Person:
    def __init__(self,name):
        self.name=name

    def greet(self):
        print("Good morning ",self.name)
    def goodBye(self):
        print("Good Bye ",self.name)
p=Person("Pratham")
p.greet()
p.goodBye()

p1=Person("Mihir")
p1.greet()
p1.goodBye()
