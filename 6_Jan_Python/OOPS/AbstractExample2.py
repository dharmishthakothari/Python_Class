from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def getArea(self):
        return 0
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def getArea(self):
        return self.length*self.width

class Square(Shape):
    pass


r=Rectangle(2,3)
print(f"Area of Rectangle {r.getArea()}")

s=Square()

print(f"Area of Square {s.getArea()}")
