class Shape:
    def getArea(self):
        return 0
class Rectangle(Shape):
    def __init__(self,lenght,width):
        self.lenght=lenght
        self.width=width
    def getArea(self):
        return self.lenght*self.width
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def getArea(self):
        return 3.14*self.radius**2    
obj=Rectangle(2,3)    
print(obj.getArea())
objC=Circle(3)        
print(objC.getArea())


