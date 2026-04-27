class Person:
    def __init__(self,name):
        self.name=name

    def greet(self):
        print("Good Afternoon ",self.name)
    def bye(self):
        print("Good Bye ",self.name)
        
p1=Person("nandini")
p1.greet()
p1.bye()
p2=Person("Dharmishtha")
p2.greet()


p2.bye()