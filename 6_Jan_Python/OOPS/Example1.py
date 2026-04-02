# create class called Car contains 
# 2 members called brandname and speed ,
#1 function called drive which 
# prints brandname and speed of the car

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def displayPerson(self):
        print(f"{self.name}-{self.age}")
    def greet(self):
        print("Good morning ",self.name)
obj=Person("dharmishtha",30)
#obj.greet()

obj1=Person("Tamanna",20)
# #obj1.greet()
obj.displayPerson()
obj1.displayPerson()

netra=Person("Netra",19)
netra.displayPerson()